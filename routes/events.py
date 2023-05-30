from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from models.driver import RequestDriver

import sqlmodel

event_router = APIRouter(
    tags=["Events"]
)

data_base = list()


@event_router.get("/number_on_frame")
async def number_on_frame(data: RequestDriver) -> dict:

    if data.data:
        data_base.append(data)

        return {
            "result": "SUCCESS",
            "desc": "",
            "data": {}
        }

    raise HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail="JSON is empty!"
    )


@event_router.get("/take_all")
async def retrieve_all_events() -> list:

    if data_base:
        return data_base

    raise HTTPException(
        status_code=status.HTTP_204_NO_CONTENT,
        detail="Events does not exist"
    )
