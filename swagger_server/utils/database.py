import logging
from redis import Redis, exceptions

logger = logging.getLogger(__name__)


class DBConnection:
    """Connection to Redis."""

    def __init__(self, db_host, db_port, db_password):
        self.__connection = Redis(
            host=db_host,
            port=db_port,
            password=db_password,
            decode_responses=True
        )
        if self.__connection:
            logger.info(f'Connected to host {db_host}.')
        else:
            logger.error(f'Error connection to host {db_host}.')

    def save(self, username, date_of_birth):
        """Save/update the given's name and date of birth in the Redis.

        :param username:  Given's username
        :type username: str
        :param date_of_birth: User's date of birth
        :type username: str

        :rtype: bool
        """
        if self.__connection:
            return self.__connection.set(username, date_of_birth)
        return False

    def read(self, username):
        """Return hello birthday message for the given user from Redis.

        :param username: Given's username
        :type username: str

        :rtype: str|none
        """
        if self.__connection:
            return self.__connection.get(username)
        return None
