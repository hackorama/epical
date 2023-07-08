# Configuration

Default configuration file [config.py](../epical/config.py) uses demo 
configuration default values and refers to demo events and photos 
located inside source folder resources folder.


```commandline
$ cat config.py| grep -i -E 'file|folder'
LOG_FILE: str = "~/.epical/epical.log"
EVENTS_FILE: str = "resources/events.json"
PHOTO_FILE_OR_FOLDER: str = "resources/photos"
EVENT_PHOTO_FILE_OR_FOLDER: str = "resources/event_photos"
POWER_OPTIONAL_UP_RECORDS_FILE: str = "~/.epical/uprecords.txt"
POWER_REQD_BATTERY_FILE: str = "~/.epical/battery"
```

Also any generated files like logs and battery charge goes to user home folder `~/.epical`

You can customize the configuration and also use the same `~/.epical` folder to 
store the custom events and photos files.

```commandline
$ cat ~/.epical/config.py | grep -i -E 'file|folder'
LOG_FILE: str = "~/.epical/epical.log"
EVENTS_FILE: str = "~/.epical/events.json"
PHOTO_FILE_OR_FOLDER: str = "~/.epical/photos"
EVENT_PHOTO_FILE_OR_FOLDER: str = "~/.epical/event_photos"
POWER_OPTIONAL_UP_RECORDS_FILE: str = "~/.epical/uprecords.txt"
POWER_REQD_BATTERY_FILE: str = "~/.epical/battery"
```

The `config.py` can also be placed in `~/.epical/config.py` and 
then copied over in the run script to override the default config.

```commandline
$ grep config.py *.sh
check_run_and_halt.sh:  CONTROL_URL=$(grep CONTROL_SERVER_URL "$INSTALL_ROOT"/epical/config.py |  cut -d '=' -f 2 | xargs)
run.sh:  [ -f "$CONFIG_ROOT"/config.py ] && cp "$CONFIG_ROOT"/config.py "$INSTALL_ROOT"/epical
run_and_halt.sh:  [ -f "$CONFIG_ROOT"/config.py ] && cp "$CONFIG_ROOT"/config.py "$INSTALL_ROOT"/epical
```

> Please see [photo configuration](./photos.md) for setting daily rotation and event day specific photos
