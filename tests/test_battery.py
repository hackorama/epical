import os
import sys
from unittest.mock import patch, MagicMock

if os.path.exists("../epical"):
    sys.path.append("../epical")

import config
from data.battery import Battery


class TestBattery:

    config.CONTROL_SERVER_URL = "http://127.0.0.1:0"  # Invalid url to force local tests

    @staticmethod
    def assert_empty_status(status):
        assert status["battery_up_days"] is None
        assert status["device_up_count"] is None
        assert status["device_up_hour_minutes"] is None
        assert status["display_refresh_hour_minutes"] is None
        assert status["battery_percent"] is None

    @staticmethod
    def assert_status(status):
        assert status["battery_up_days"] > 0
        assert status["device_up_count"] > 0
        assert int(status["device_up_hour_minutes"].split(":")[1]) >= 0
        assert int(status["display_refresh_hour_minutes"].split(":")[1]) >= 0
        assert status["battery_percent"] > 0

    def test_battery_status_without_data(self):
        restore_records_file = config.POWER_OPTIONAL_UP_RECORDS_FILE
        restore_battery_file = config.POWER_REQD_BATTERY_FILE
        config.POWER_OPTIONAL_UP_RECORDS_FILE = ""
        config.POWER_REQD_BATTERY_FILE = ""
        status = Battery().status()
        TestBattery.assert_empty_status(status)
        assert Battery().get_device_boots() == 0
        config.POWER_OPTIONAL_UP_RECORDS_FILE = restore_records_file
        config.POWER_REQD_BATTERY_FILE = restore_battery_file

    def test_battery_status_with_data(self):
        restore_records_file = config.POWER_OPTIONAL_UP_RECORDS_FILE
        restore_battery_file = config.POWER_REQD_BATTERY_FILE
        config.POWER_OPTIONAL_UP_RECORDS_FILE = "./resources/uprecords.txt"
        config.POWER_REQD_BATTERY_FILE = "./resources/battery"
        battery = Battery()
        status = battery.status()
        print(status)
        TestBattery.assert_status(status)
        assert battery.get_device_boots() > 0
        config.POWER_OPTIONAL_UP_RECORDS_FILE = restore_records_file
        config.POWER_REQD_BATTERY_FILE = restore_battery_file


    def test_battery_status_and_data_methods(self):
        restore_records_file = config.POWER_OPTIONAL_UP_RECORDS_FILE
        restore_battery_file = config.POWER_REQD_BATTERY_FILE
        config.POWER_OPTIONAL_UP_RECORDS_FILE = "./resources/uprecords.txt"
        config.POWER_REQD_BATTERY_FILE = "./resources/battery"
        battery = Battery()
        status = battery.status()
        assert status["battery_up_days"] == battery.get_battery_up_days()
        assert status["device_up_count"] == battery.get_device_up_count()
        assert status["device_up_hour_minutes"] == battery.get_device_up_hour_minutes()
        assert status["display_refresh_hour_minutes"] == battery.get_display_refresh_hour_minutes()
        assert status["battery_percent"] == battery.battery_percent()
        config.POWER_OPTIONAL_UP_RECORDS_FILE = restore_records_file
        config.POWER_REQD_BATTERY_FILE = restore_battery_file

    def test_battery_status_with_empty_data(self):
        restore_records_file = config.POWER_OPTIONAL_UP_RECORDS_FILE
        restore_battery_file = config.POWER_REQD_BATTERY_FILE
        config.POWER_OPTIONAL_UP_RECORDS_FILE = "./resources/uprecords.txt"
        config.POWER_REQD_BATTERY_FILE = "./resources/empty_battery"
        battery = Battery()
        status = battery.status()
        TestBattery.assert_empty_status(status)
        assert battery.get_device_boots() == 0
        config.POWER_OPTIONAL_UP_RECORDS_FILE = restore_records_file
        config.POWER_REQD_BATTERY_FILE = restore_battery_file

    def test_battery_status_with_invalid_data(self):
        restore_records_file = config.POWER_OPTIONAL_UP_RECORDS_FILE
        restore_battery_file = config.POWER_REQD_BATTERY_FILE
        config.POWER_OPTIONAL_UP_RECORDS_FILE = "./resources/uprecords.txt"
        config.POWER_REQD_BATTERY_FILE = "./resources/invalid_battery"
        battery = Battery()
        status = battery.status()
        TestBattery.assert_empty_status(status)
        assert battery.get_device_boots() == 0
        config.POWER_OPTIONAL_UP_RECORDS_FILE = restore_records_file
        config.POWER_REQD_BATTERY_FILE = restore_battery_file

    @patch('data.battery.requests')
    def test_battery_status_remote_data(self, mock_requests):
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.text = "Sat Jun 3 13:37:29 PDT 2023"
        mock_requests.get.return_value = mock_response

        restore_records_file = config.POWER_OPTIONAL_UP_RECORDS_FILE
        config.POWER_OPTIONAL_UP_RECORDS_FILE = "./resources/uprecords.txt"
        battery = Battery()
        status = battery.status()
        print(status)
        TestBattery.assert_status(status)
        assert battery.get_device_boots() >= 0
        config.POWER_OPTIONAL_UP_RECORDS_FILE = restore_records_file
