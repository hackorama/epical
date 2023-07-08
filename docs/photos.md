# Displaying Photos 


Configured in [config.py](../epical/config.py) 

```python
PHOTO_FILE_OR_FOLDER: str = "resources/photos"
EVENT_PHOTO_FILE_OR_FOLDER: str = "resources/event_photos"
```

A photo is selected to display in this order:

1. If the external control server is running at `CONTROL_SERVER_URL`
and if there is a `CONTROL_SERVER_URL/photo.xxx` photo available
then it is selected
2. Else if there is an event photo matching the current day `resources/event_photos/<Month>_<Day>.xxx` then it is selected
3. Else if there is local photo specifically named `resources/photos/photo.xxx` then it is selected
4. Otherwise, one of the photos from `resources/photos/*.xxx` will be selected

## Naming photo files

The photos folders should have only valid image files with extensions: `*.jpg`, `*.jpeg`, `*.png`, `*.bmp`

The folder for event day specific images uses naming scheme: `[MM]_[DD].xxx`

Example: Special image for Christmas and New Years day: `12_25.png`, `1_1.bmp`

## Photo image colors

The Waveshare epd12in48b_V2 ePaper display supports only three colors: black, white and red.

So all regular images `*.jpg`, `*.jpeg`, `*.png` will get converted by ePiCal to monochrome black and white with dithering to simulate gray scale.

The `*.bmp` images are expected to be already converted to black, white and red tri-color following [convert.sh](../utils/convert.sh)

Example tri-color bmp [../epical/resources/event_photos/12_25.bmp](../epical/resources/event_photos/12_25.bmp):

![Tri-color](../epical/resources/event_photos/12_25.bmp)
