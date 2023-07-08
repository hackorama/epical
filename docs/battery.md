# Battery Usage Tracking

When using an external power back or battery pack, the battery charge percent can be tracked
using the uptime and the average power use by Pi Zero device.

> Please see [power management options](./power.md)

1. Track when battery was fully charged by storing the date : `date > ~/.epical/battery`
2. Install and configure `uptimed` with `uprecords` to track Pi Zero device uptime

Once the battery date file and `uprecords` are available the battery percentage
will be calculated based on the battery and device power specs configured in [config.py](../epical/config.py)

The power usage details will be displayed at the bottom of the screen:

- Bottom right: `85 %` Battery remaining percentage
- Bottom left: `7/5 0:38` 7 device boots in 5 days since last battery charge with 0 hour 38 minutes of total device uptime

Available in the logs as well:

```commandline
INFO     2023-07-01 18:33:34,707 - Battery up days   5
INFO     2023-07-01 18:33:34,710 - Device boot count 7
INFO     2023-07-01 18:33:34,713 - Device up time    0:38
INFO     2023-07-01 18:33:34,716 - Display up time   0:10
INFO     2023-07-01 18:33:34,719 - Battery           85 %
```

## Configure `uptimed` and use `uprecords` 

```commandline
hackorama@hackorama:~ $ sudo apt install uptimed
hackorama@hackorama:~ $ uprecords
uptimed: no useable database found.
     #               Uptime | System                                     Boot up
----------------------------+---------------------------------------------------
->   1     0 days, 00:14:08 | Linux 6.1.21+             Tue Jul  1 20:17:15 2023
----------------------------+---------------------------------------------------
NewRec     0 days, 00:14:07 | since                     Tue Jul  1 20:17:16 2023
    up     0 days, 00:14:08 | since                     Wed Dec 31 16:00:00 1969
  down  6250 days, 06:54:46 | since                     Wed Dec 31 16:00:00 1969
   %up                0.000 | since                     Wed Dec 31 16:00:00 1969
```
   

#### Fix 'uptimed: no useable database found.'


```commandline
hackorama@hackorama:~ $ ps aux | grep uptimed
daemon     761  0.0  0.3   1960  1324 ?        Ss   20:20   0:00 /usr/sbin/uptimed -f
hackorama@hackorama:~ $ sudo kill 761

hackorama@hackorama:~ $ sudo service  uptimed start
hackorama@hackorama:~ $ uprecords
     #               Uptime | System                                     Boot up
----------------------------+---------------------------------------------------
->   1     0 days, 00:21:42 | Linux 6.1.21+             Tue Jul  1 20:17:15 2023
----------------------------+---------------------------------------------------
NewRec     0 days, 00:21:41 | since                     Tue Jul  1 20:17:15 2023
    up     0 days, 00:21:42 | since                     Tue Jul  1 20:17:15 2023
  down     0 days, 00:00:00 | since                     Tue Jul  1 20:17:15 2023
   %up              100.000 | since                     Tue Jul  1 20:17:15 2023
```

#### Change uptime tracking frequency to minute
   
```commandline
hackorama@hackorama:~ $ sudo cp  /etc/uptimed.conf /etc/uptimed.conf.original
hackorama@hackorama:~ $ sudo vi /etc/uptimed.conf
hackorama@hackorama:~ $ diff /etc/uptimed.conf.original /etc/uptimed.conf
4c4
< UPDATE_INTERVAL=3600
---
> UPDATE_INTERVAL=60
10c10
< LOG_MINIMUM_UPTIME=1h
---
> LOG_MINIMUM_UPTIME=1m
hackorama@hackorama:~ $

hackorama@hackorama:~ $ sudo service uptimed restart
```