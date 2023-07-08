import datetime
import logging
import os
import subprocess
from pathlib import Path

import kollavarsham
import pytz
import uvicorn
from dateutil.tz import tzlocal
from fastapi import BackgroundTasks, FastAPI, File, UploadFile, status
from fastapi.responses import RedirectResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image, ImageOps

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

PROJECT_NAME = "epical"
STATIC_FILES_FOLDER = "static"
RUN_SH = "../../web.sh"
PHOTO_WIDTH = 700
PHOTO_HEIGHT = 525

app = FastAPI()

"""
Simple REST API server with string responses and no json
for use from low powered devices like Pi or Arduino

NOTE: No HTTPS and auth enabled since both the device and server
      are on trusted local 192.168.0.0/16 network.
      Please enable them as required if deploying on external network
      
      No input path validation since running on trusted local 192.168.0.0/16 network
      Add strict input validation and file write restrictions as needed
      when deploying on an external network.
"""


def start_refresh():
    logging.info("Starting screen refresh ...")
    result = subprocess.run([RUN_SH], stdout=subprocess.PIPE, check=False)
    logging.info("Finished screen refresh")
    print(result)


@app.put("/refresh", status_code=200)
async def refresh(background_tasks: BackgroundTasks) -> str:
    background_tasks.add_task(start_refresh)
    return "OK"


@app.get("/kollavarsham", status_code=200)
async def kolla_varsham() -> str:
    now = pytz.utc.localize(datetime.datetime.utcnow())
    kv_date = kollavarsham.Kollavarsham(
        latitude=10, longitude=76.2, system="SuryaSiddhanta"
    )
    today = kv_date.from_gregorian_date(date=now)
    return (
        f"{today.year} {today.ml_masa_name} {today.date} {today.naksatra.ml_malayalam}"
    )


@app.get("/health", status_code=200)
async def health() -> str:
    return "OK"


@app.post("/upload/logs")
async def upload_logs(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(f"{STATIC_FILES_FOLDER}/{PROJECT_NAME}.log", "wb") as _file:
            _file.write(contents)
    except Exception as error:  # pylint: disable=broad-exception-caught
        logger.error("File upload failed: %s", error)
        return "ERROR"
    return "OK"


@app.post("/upload/screen")
async def upload_screen(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(f"{STATIC_FILES_FOLDER}/{PROJECT_NAME}.png", "wb") as _file:
            _file.write(contents)
    except Exception as error:  # pylint: disable=broad-exception-caught
        logger.error("File upload failed: %s", error)
        return "ERROR"
    return "OK"


@app.post("/upload/photo")
async def upload_photo(file: UploadFile = File(...)):
    try:
        image = Image.open(file.file)
        fixed_image = ImageOps.exif_transpose(image)  # prevent image rotation
        fixed_image.thumbnail((PHOTO_WIDTH, PHOTO_HEIGHT))
        fixed_image.save(f"{STATIC_FILES_FOLDER}/photo.png", "PNG")
    except Exception as error:  # pylint: disable=broad-exception-caught
        logger.error("Photo upload and processing failed: %s", error)
        return RedirectResponse(
            url="/error.html", status_code=status.HTTP_303_SEE_OTHER
        )
    return RedirectResponse(url="/settings.html", status_code=status.HTTP_303_SEE_OTHER)


@app.post("/delete/photo")
async def delete_photo():
    try:
        if os.path.isfile(f"{STATIC_FILES_FOLDER}/photo.png"):
            os.remove(f"{STATIC_FILES_FOLDER}/photo.png")
    except Exception as error:  # pylint: disable=broad-exception-caught
        logger.error("Photo delete failed: %s", error)
        return RedirectResponse(
            url="/error.html", status_code=status.HTTP_303_SEE_OTHER
        )
    return RedirectResponse(url="/settings.html", status_code=status.HTTP_303_SEE_OTHER)


@app.post("/refresh/disable")
async def refresh_disable():
    disable_file = f"{STATIC_FILES_FOLDER}/disable"
    try:
        if os.path.isfile(disable_file):
            os.remove(disable_file)
        else:
            Path(disable_file).touch()
    except Exception as error:  # pylint: disable=broad-exception-caught
        logger.error("Disable update failed: %s", error)
        return RedirectResponse(
            url="/error.html", status_code=status.HTTP_303_SEE_OTHER
        )
    return RedirectResponse(url="/settings.html", status_code=status.HTTP_303_SEE_OTHER)


@app.post("/refresh/battery")
async def refresh_battery():
    battery_file = f"{STATIC_FILES_FOLDER}/battery"
    try:
        if os.path.isfile(battery_file):
            os.remove(battery_file)
        else:
            with open(battery_file, "w", encoding="utf-8") as _file:
                # Match default unix date command output with timezone
                _file.write(
                    f'{datetime.datetime.now(tzlocal()).strftime("%a %b %-d %H:%M:%S %Z %Y")}\n'
                )
    except Exception as error:  # pylint: disable=broad-exception-caught
        logger.error("Battery update failed: %s", error)
        return RedirectResponse(
            url="/error.html", status_code=status.HTTP_303_SEE_OTHER
        )
    return RedirectResponse(url="/settings.html", status_code=status.HTTP_303_SEE_OTHER)


@app.post("/remove/upgrade")
async def remove_upgrade():
    package_file = f"{STATIC_FILES_FOLDER}/{PROJECT_NAME}.tar"
    try:
        if os.path.isfile(package_file):
            os.remove(package_file)
    except Exception as error:  # pylint: disable=broad-exception-caught
        logger.error("Remove upgrade failed: %s", error)
        return RedirectResponse(
            url="/error.html", status_code=status.HTTP_303_SEE_OTHER
        )
    return RedirectResponse(url="/settings.html", status_code=status.HTTP_303_SEE_OTHER)


app.mount("/", StaticFiles(directory=STATIC_FILES_FOLDER, html=True), name="static")


def start():
    uvicorn.run("server:app", host="0.0.0.0", port=8888)


if __name__ == "__main__":
    start()
