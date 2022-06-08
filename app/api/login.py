from typing import Literal, Optional
from fastapi import APIRouter, Query

login_router = APIRouter(prefix="/database/accounts")


@login_router.post("/loginGJAccount.php")
async def login_request(
    udid: str = Query(...),
    userName: str = Query(...),
    password: str = Query(...),
    secret: Literal["Wmfv3899gc9"] = Query(...),
    sID: Optional[str] = Query(None),
):
    return "-1"
