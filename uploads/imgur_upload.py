import requests
from base64 import b64encode
import os


def upload_image_imgur(files_list):
    url = "https://api.imgur.com/3/image"
    headers = {"Authorization": f"Bearer %s" % os.getenv("AUTH_TOKEN_IMGUR")}
    info_files = list()

    for key in files_list:
        for file in files_list.getlist(key):
            payload = {
                "name": "Teste",
                "title": "title teste",
                "description": "description",
                "image": b64encode(file.read()),
            }

            response = requests.post(
                url=url,
                headers=headers,
                data=payload,
            ).json()["data"]

            info_files.append(
                {
                    "id": response["id"],
                    "ref_color": key,
                    "link": response["link"],
                    "deletehash": response["deletehash"],
                }
            )

    return info_files
