## Pillow Fonts

The malayalam fonts with complex text layout ligatures are not rendered correctly in Pillow.

Requires [libraqm](https://github.com/HOST-Oman/libraqm) to fix the complex text layout

> [Install libraqm](https://stackoverflow.com/questions/74608140/pillow-not-recognizing-libraqm-installation-on-mac-os)

```shell
$ pip uninstall pillow
$ brew install freetype harfbuzz fribidi
$ brew install libraqm
$ pip install --upgrade pillow  --global-option="build_ext" --global-option="--enable-raqm"
```
This enables the font layout_engine `ImageFont.LAYOUT_RAQM` in `Pillow/PIL`

```shell
$ python
>>> from PIL.features import features
>>> print(features.get('raqm', "No RAQM Support"))
('PIL._imagingft', 'HAVE_RAQM', 'raqm_version')
>>>
```

## On device dependencies

On Pi Zero Pillow requires native images libs

```shell
$ sudo apt-get install libopenjp2-7
```


