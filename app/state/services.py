from gdpyslib.connections.mongo import MongoConnection
from gdpyslib.connections.redis import RedisConnection

import app.config

mongo = MongoConnection(str(app.config.MONGODB_DSN))
redis = RedisConnection(str(app.config.REDIS_DSN))
