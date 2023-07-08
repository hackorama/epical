# Control Protocol

The device checks the following control URL endpoints from the run script
[check_run_and_halt.sh](../../../check_run_and_halt.sh) and the screen refresh code.

Configured in [config.py](../../../epical/config.py)

```python
# External server for control checks (check_run_and_halt.sh) and data (image, battery) updates
CONTROL_SERVER_URL: str = "http://home.local.net:8888"
```

## Disable screen refresh

Check screen refresh disable from device

`GET http://home.local.net:8888/disable`

Toggle disable/enable screen refresh from UI

`POST http://home.local.net:8888/refresh/disable`

Or from the shell

```shell
$ touch web/server/static/disable
```
```shell
$ rm  web/server/static/disable
```

## Update battery charge time

Fetch battery charge time from device

`GET http://home.local.net:8888/battery`

Toggle update/clear battery charge date from UI

`POST http://home.local.net:8888/refresh/battery`

Or from the shell

```shell
$ date > web/server/static/battery
```
```shell
$ rm web/server/static/disable
```

## Upgrade release

Download and install from device

`GET http://home.local.net:8888/epical.tar`

Set/clear the upgrade package from shell

```shell
$ cp epical.tar web/server/static
```

```shell
$ rm web/server/static/epical.tar
```

Clear upgrade package from UI

`POST http://home.local.net:8888/remove/upgrade`

## Set an override image

Fetch override photo (`.png`, `.bmp`, `.jpg`, `.jpeg`) from device

`GET http://home.local.net:8888/photo.png`

Set new photo from the UI

`POST http://home.local.net:8888/upload/photo`

Clear photo from the UI

`POST http://home.local.net:8888/delete/photo`

Or from the shell

```shell
$ cp photo.png web/server/static
```

```shell
$ rm web/server/static/photo.png
```

## Control check logs

From run script

```shell
CONTROL CHECK: Server http://home.local.net:8888
CONTROL CHECK: No package to deploy
CONTROL CHECK: No refresh disable
```

```shell
CONTROL CHECK: Server http://home.local.net:8888
CONTROL CHECK: No package to deploy
CONTROL CHECK: Refresh disabled, device will not be halted
Exiting, device will not be halted
```

```shell
CONTROL CHECK: Server http://home.local.net:8888
CONTROL CHECK: Found package
Deploying to /home/hackorama/epical/.. ...
CONTROL CHECK: No refresh disable
```

From device update code

```shell
INFO     2023-06-24 07:15:38,531 - Using remote battery charge time: Sat Jun 3 13:37:29 PDT 2023
```

```shell
INFO     2023-06-24 07:15:46,184 - Displaying remote photo.bmp
```
