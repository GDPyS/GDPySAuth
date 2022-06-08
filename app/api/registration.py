from typing import Literal

from fastapi import APIRouter
from fastapi import Query

registration_router = APIRouter(prefix="/database")


@registration_router.post("/registerGJAccount.php")
async def registration_request(
    userName: str = Query(...),
    password: str = Query(...),
    email: str = Query(...),
    secret: Literal["Wmfv3899gc9"] = Query(...),
):
    return "-1"
