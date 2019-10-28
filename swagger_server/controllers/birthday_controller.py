import connexion
import six
import redis

from datetime import datetime, date, timedelta

from swagger_server.models.birthday_body import BirthdayBody  # noqa: E501
from swagger_server.controllers import dbconnection


def add_birthday(body, username):  # noqa: E501
    """Save/update the given's name and date of birth in the database.

    :param body: User's date of birth
    :type body: dict | bytes
    :param username: Given's username
    :type username: str

    :rtype: None
    """
    if connexion.request.is_json:
        body = BirthdayBody.from_dict(connexion.request.get_json())  # noqa: E501
        if dbconnection.save(username, str(body.date_of_birth)):
            return '', 204

    return 'Invalid input', 400


def get_birthday(username):  # noqa: E501
    """Return hello birthday message for the given user.

    :param username: Given's username
    :type username: str

    :rtype: None
    """
    date_of_birth = dbconnection.read(username)

    if date_of_birth:
        now = datetime.now().date()
        date_of_birth = datetime.strptime(date_of_birth, '%Y-%m-%d')

        if now.month > date_of_birth.month:
            next_birthday = date(
                year=now.year+1,
                month=date_of_birth.month,
                day=date_of_birth.day
            )
        else:
            next_birthday = date(
                year=now.year,
                month=date_of_birth.month,
                day=date_of_birth.day
            )

        if next_birthday == now:
            return f'Hello, {username}! Happy birthday!'
        return f'Hello, {username}! You birthday is in {(next_birthday - now).days} day(s)'

    return f'User {username} not found', 404
