import os

DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', 6379)
DB_PASSWORD = os.getenv('DB_PASSWORD')
