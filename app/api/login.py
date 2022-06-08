from typing import Literal
from typing import Optional

import gdpyslib.usecases.user
from fastapi import APIRouter
from fastapi import Query
from gdpyslib.cryptography.bcrypt import compare_bcrypt
from gdpyslib.responses.general import ResponseStatus

import app.state.services

login_router = APIRouter(prefix="/database/accounts")


@login_router.post("/loginGJAccount.php")
async def login_request(
    uuid: str = Query(..., alias="udid"),
    userName: str = Query(...),
    password: str = Query(...),
    secret: Literal["Wmfv3899gc9"] = Query(...),
    sID: Optional[str] = Query(None),
):
    user = await gdpyslib.usecases.user.fetch_user(
        name=userName,
        mongo=app.state.services.mongo.client.gdpys,
    )

    if not user:
        return str(ResponseStatus.FAIL)

    if not await compare_bcrypt(password, user.password_bcrypt):
        return str(ResponseStatus.FAIL)

    return f"{user.id},{user.id}"
