import os
import shutil
import subprocess
from datetime import datetime, timedelta
from typing import Dict, List, Optional, Tuple, Union

import config
import requests
from util import log


class Battery:  # pylint: disable=too-many-instance-attributes, too-many-public-methods
    def __init__(self):
        self.up_records_file = config.POWER_OPTIONAL_UP_RECORDS_FILE
        self.battery_file = config.POWER_REQD_BATTERY_FILE

        self.device_volts = config.POWER_DEVICE_VOLTS
        self.device_milli_amp_hour = config.POWER_DEVICE_MILLI_AMP_HOUR

        self.battery_volts = config.POWER_BATTERY_VOLTS
        self.battery_milli_amp_hour = config.POWER_BATTERY_MILLI_AMP_HOUR
        self.battery_monthly_self_discharge_percent = (
            config.POWER_BATTERY_MONTHLY_SELF_DISCHARGE_PERCENT
        )
        self.battery_efficiency_percent = config.POWER_BATTERY_EFFICIENCY_PERCENT

        self.display_refresh_milli_watt = config.POWER_DISPLAY_REFRESH_MILLI_WATT
        self.display_refresh_volts = config.POWER_DISPLAY_REFRESH_VOLTS
        self.display_refresh_time_secs = config.POWER_DISPLAY_REFRESH_TIME_SECS
        self.display_refresh_milli_amp = (
            self.display_refresh_milli_watt / self.display_refresh_volts
        )

        self.battery_charge_time = None
        self.battery_up_days = None
        self.device_up_count = None
        self.device_up_seconds = None
        self.device_boots = 0

        self.measure()

    def measure(self) -> None:
        self.battery_charge_time = self.get_battery_charge_time()
        self.battery_up_days = self.get_battery_up_days()
        self.device_up_count, self.device_up_seconds = self.get_device_up()

    def get_uprecords(self) -> List[str]:
        if shutil.which("uprecords"):
            result = subprocess.run(
                # no ansi codes, reverse sort by time, no stats, up to 120 entries
                ["uprecords", "-a", "-B", "-s", "-m", "120"],
                stdout=subprocess.PIPE,
                check=False,
            )
        elif os.path.exists(os.path.expanduser(self.up_records_file)):
            log.warning(f"Using stored uprecords data file {self.up_records_file}")
            result = subprocess.run(
                ["cat", os.path.expanduser(self.up_records_file)],
                stdout=subprocess.PIPE,
                check=False,
            )
        else:
            log.warning(
                f"No 'uprecords' tool installed and no data file provided as {self.up_records_file}"
            )
            log.warning(
                "  Please configure 'uptimed' and 'uprecords' following docs/battery.md"
            )
            return []
        lines = []
        for line in result.stdout.decode("utf-8", errors="strict").splitlines():
            lines.append(line.rstrip())
        return lines

    def get_remote_battery_charge_time(self) -> Optional[str]:
        try:
            response = requests.get(f"{config.CONTROL_SERVER_URL}/battery", timeout=5)
            if response.ok:
                return response.text.strip()
        except Exception as expected_error:
            log.debug(f"Remote battery check: {expected_error}")
        return None

    def get_local_battery_charge_time(self) -> Optional[str]:
        if os.path.exists(os.path.expanduser(self.battery_file)):
            with open(os.path.expanduser(self.battery_file), encoding="utf-8") as f:
                return f.readline().strip()
        log.warning(
            f"Please update battery charge time by running: date > {self.battery_file}"
        )
        return None

    def get_battery_charge_time(self) -> Optional[datetime]:
        charged_date = self.get_remote_battery_charge_time()
        if charged_date:
            log.info(f"Using remote battery charge time: {charged_date}")
            return self.shell_date(charged_date)
        charged_date = self.get_local_battery_charge_time()
        if charged_date:
            log.info(f"Using local battery charge time: {charged_date}")
            return self.shell_date(charged_date)
        log.warning("No battery charge time")
        return None

    def shell_date(self, date_string: str) -> Optional[datetime]:
        try:
            return datetime.strptime(date_string, "%a %b %d %H:%M:%S %Z %Y")
        except Exception as error:
            log.warning(f"Invalid battery date '{date_string}': {error}")
        return None

    def uprecord_date(self, date_string: str) -> datetime:
        return datetime.strptime(date_string, "%a %b %d %H:%M:%S %Y")

    def get_duration(self, days, hours, minutes, seconds) -> timedelta:
        return timedelta(
            days=int(days), hours=int(hours), minutes=int(minutes), seconds=int(seconds)
        )

    def battery_percent(self) -> Optional[int]:
        usage_percent = self.battery_usage_percent()
        if usage_percent is not None:
            return 100 - usage_percent
        return None

    def alt_battery_usage_percent(self) -> Optional[int]:
        if self.battery_up_days is None or self.device_up_seconds is None:
            return None
        device_ma = self.device_up_seconds * self.device_milli_amp_hour
        screen_ma = self.display_refresh_seconds() * self.display_refresh_milli_amp
        total_usage_mah = (device_ma + screen_ma) / (60 * 60)
        print(self.device_up_seconds, self.display_refresh_seconds())
        battery_self_discharge_pc = (
            self.battery_monthly_self_discharge_percent / 60
        ) * self.battery_up_days
        battery_available_mah = (
            self.battery_milli_amp_hour
            * (self.battery_efficiency_percent - battery_self_discharge_pc)
        ) / 100
        usage_percent = int((total_usage_mah / battery_available_mah) * 100)
        return usage_percent

    def battery_usage_percent(self) -> Optional[int]:
        if self.battery_up_days is None or self.device_up_seconds is None:
            return None
        device_up_hours = self.device_up_seconds / (60 * 60)
        battery_self_discharge_pc = (
            self.battery_monthly_self_discharge_percent / 60
        ) * self.battery_up_days
        battery_actual_mah = (
            self.battery_milli_amp_hour
            * (self.battery_efficiency_percent - battery_self_discharge_pc)
        ) / 100
        device_consumed_mwh = (
            (self.device_milli_amp_hour * self.device_volts)
        ) * device_up_hours
        display_consumed_mwh = 0
        display_refresh_seconds = self.display_refresh_seconds()
        if display_refresh_seconds:
            display_up_hours = display_refresh_seconds / (60 * 60)
            display_consumed_mwh = self.display_refresh_milli_watt * display_up_hours
        battery_available_mwh = (
            (battery_actual_mah * self.battery_volts) if battery_actual_mah > 0 else 0
        )
        consumed_mwh = device_consumed_mwh + display_consumed_mwh
        return int((consumed_mwh / battery_available_mwh) * 100)

    def normalized_uprecord(self, record: str) -> str:
        # Remove '->', strip white spaces
        #
        #      1    61 days, 07:05:42 | Linux 5.10.0-19-amd64     Mon Nov 21 08:34:55 2022
        # ->   2    45 days, 23:53:14 | Linux 5.10.0-19-amd64     Mon Mar  6 22:20:47 2023
        #      3    30 days, 19:00:50 | Linux 5.10.0-15-amd64     Thu Jul 28 17:23:05 2022
        normalized = record
        if record.startswith("->"):
            normalized = record[2:]
        return normalized.strip()

    def get_uptime_after_charge_from_uprecords(self, record) -> Optional[float]:
        # 0    1  2     3        4 5     6                   7   8   9  10       11
        # 2    45 days, 23:53:14 | Linux 5.10.0-19-amd64     Mon Mar  6 22:20:47 2023
        tokens = record.split()

        if len(tokens) != 12:
            log.error(f"Unexpected token count {len(tokens)} != 12 in record: {record}")
            return None

        date_string = record.split(maxsplit=7)[-1]
        record_time = self.uprecord_date(date_string)
        if record_time > self.battery_charge_time:
            duration = self.get_duration(
                tokens[1],
                tokens[3].split(":")[0],
                tokens[3].split(":")[1],
                tokens[3].split(":")[2],
            )
            return duration.total_seconds()
        return 0  # For older records return 0 seconds not None

    def get_device_up(self) -> Tuple[Optional[int], Optional[int]]:
        up_records = self.get_uprecords()
        if up_records and self.battery_charge_time:
            up_time_total = 0
            up_count = 0
            separator = "----"
            separators_found = 0
            for record in up_records:
                if record.startswith(separator):
                    separators_found += 1
                    continue  # skip separators
                if separators_found > 1:
                    break  # stop on footer stats record
                if (
                    separators_found == 1
                ):  # read data records, till footer stats or end of data
                    normalised_record = self.normalized_uprecord(record)
                    up_time = self.get_uptime_after_charge_from_uprecords(
                        normalised_record.strip()
                    )
                    if up_time:
                        up_time_total += int(up_time)
                        up_count += 1
                    self.device_boots += 1
                # else headers skipped
            return up_count, up_time_total
        return None, None

    def format_minutes(self, seconds) -> Optional[str]:
        if seconds is not None:
            formatted = str(timedelta(seconds=seconds))
            return formatted.rsplit(":", 1)[0]
        return None

    def get_battery_up_days(self) -> Optional[int]:
        if self.battery_charge_time:
            duration = datetime.now() - self.battery_charge_time
            return duration.days if duration.days else 1  # round up zero days
        return None

    def get_device_up_hour_minutes(self) -> Optional[str]:
        return self.format_minutes(self.device_up_seconds)

    def display_refresh_seconds(self) -> Optional[int]:
        if self.device_up_count:
            return self.device_up_count * self.display_refresh_time_secs
        return None

    def get_device_up_count(self) -> Optional[int]:
        if self.device_up_count:
            return self.device_up_count
        return None

    def get_display_refresh_hour_minutes(self) -> Optional[str]:
        return self.format_minutes(self.display_refresh_seconds())

    def status(self) -> Dict[str, Union[Optional[str], Optional[int]]]:
        return {
            "battery_up_days": self.battery_up_days,
            "device_up_count": self.device_up_count,
            "device_up_hour_minutes": self.get_device_up_hour_minutes(),
            "display_refresh_hour_minutes": self.get_display_refresh_hour_minutes(),
            "battery_percent": self.battery_percent(),
        }

    def get_device_boots(self) -> int:
        return self.device_boots
