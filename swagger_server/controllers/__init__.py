from swagger_server.settings import DB_HOST, DB_PORT, DB_PASSWORD
from swagger_server.utils.database import DBConnection

dbconnection = DBConnection(DB_HOST, DB_PORT, DB_PASSWORD)
