from typing import Literal

import gdpyslib.usecases.user
from fastapi import APIRouter
from fastapi import Query
from gdpyslib.responses.registration import RegistrationResponse

import app.state

registration_router = APIRouter(prefix="/database")


@registration_router.post("/registerGJAccount.php")
async def registration_request(
    userName: str = Query(...),
    password: str = Query(...),
    email: str = Query(...),
    secret: Literal["Wmfv3899gc9"] = Query(...),
):
    registration_response, user = await gdpyslib.usecases.user.register_user(
        userName,
        email,
        password,
        app.state.services.mongo.client.gdpys,
    )

    return str(registration_response)
