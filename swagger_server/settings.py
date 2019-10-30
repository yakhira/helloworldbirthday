import os

DB_HOST = os.getenv('DB_HOST', 'hellowroldbirth-redis.w6vutn.0001.use2.cache.amazonaws.com')
DB_PORT = os.getenv('DB_PORT', 6379)
DB_PASSWORD = os.getenv('DB_PASSWORD')
