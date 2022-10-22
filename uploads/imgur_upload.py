import requests
import os
from utility.handleErr import handlerErr


def upload_image_imgur(files_list: list[bytes], title: str, details: str):
    url = "https://api.imgur.com/3/image"
    headers = {"Authorization": f"Bearer %s" % os.getenv("AUTH_TOKEN_IMGUR")}
    info_files = list()

    for index, file in enumerate(files_list):
        payload = {
            "name": "Image Product",
            "title": title,
            "description": details,
            "image": file,
        }
        response = requests.post(
            url=url,
            headers=headers,
            data=payload,
        ).json()["data"]

        if "error" in response:
            handlerErr("imgur -> %s" % response["error"]["message"])

        info_files.append(
            {
                "upload_id": response["id"],
                "ref_color": index,  # "file.filename",
                "url_image": response["link"],
                "key_img": response["deletehash"],
            }
        )

    return info_files
