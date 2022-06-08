from fastapi import FastAPI

import app.api
import app.state


def init_routers(fastapi_app: FastAPI) -> None:
    fastapi_app.include_router(app.api.login.login_router)
    fastapi_app.include_router(app.api.registration.registration_router)


def init_events(fastapi_app: FastAPI) -> None:
    @fastapi_app.on_event("startup")
    async def on_startup() -> None:
        await app.state.services.mongo.connect()
        await app.state.services.redis.connect()

    @fastapi_app.on_event("shutdown")
    async def on_shutdown() -> None:
        await app.state.services.mongo.disconnect()
        await app.state.services.redis.disconnect()


def init_app() -> FastAPI:
    fastapi_app = FastAPI()

    init_routers(fastapi_app)
    init_events(fastapi_app)

    return fastapi_app


fastapi_app = init_app()
