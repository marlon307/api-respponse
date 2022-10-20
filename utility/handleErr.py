import logging
from fastapi import status, HTTPException
from time import gmtime, strftime

logging.basicConfig(
    filename="log.log",
    encoding="utf-8",
    format="%(asctime)s:%(levelname)s:%(message)s",
    datefmt=strftime("%a, %d %m %Y %H:%M:%S", gmtime()),
)


def handlerErr(text: str):
    print(text)
    logging.error(text)

    return HTTPException(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        detail="Server error.",
    )
