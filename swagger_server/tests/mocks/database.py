from unittest.mock import Mock


class DBConnection:
    """Connection to Redis."""

    def __init__(self, db_host, db_port, db_password):
        self.__birthdays = {}

    def save(self, username, date_of_birth):
        """Save/update the given's name and date of birth in the Redis.

        :param username:  Given's username
        :type username: str
        :param date_of_birth: User's date of birth
        :type username: str

        :rtype: bool
        """
        self.__birthdays[username] = date_of_birth

        return True

    def read(self, username):
        """Return hello birthday message for the given user from Redis.

        :param username: Given's username
        :type username: str

        :rtype: str|none
        """
        return self.__birthdays.get(username)


dbconnection_mock = Mock(side_effect=DBConnection)
