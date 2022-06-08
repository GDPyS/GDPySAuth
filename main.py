#!/usr/bin/env python3.9
import uvicorn
import uvloop

import app.config

uvloop.install()


def main() -> int:
    uvicorn.run(
        "app.init_api:fastapi_app",
        server_header=False,
        date_header=False,
        host="127.0.0.1",
        port=app.config.SERVER_PORT,
    )

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
