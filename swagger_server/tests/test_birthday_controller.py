# coding: utf-8
from __future__ import absolute_import

from datetime import date
from swagger_server.tests import client


def test_add_birthday(client):
    """Test case for add_birthday"""

    response = client.put(
        '/hello/JhonSmith',
        json={
            'dateOfBirth': '1985-06-25'
        }
    )

    assert response.status_code == 204


def test_get_birthday(mocker, client):
    """Test case for get_birthday"""
    response = client.get('/hello/JhonSmith')

    assert response.status_code == 200
    assert b'Hello, JhonSmith! You birthday is in' in response.data


def test_add_birthday_now(client):
    """Test case for add_birthday with today's birth"""
    response = client.put(
        '/hello/JhonDow',
        json={
            'dateOfBirth': date.today()
        }
    )

    assert response.status_code == 204


def test_get_birthday_now(mocker, client):
    """Test case for get_birthday with today's birth"""
    response = client.get('/hello/JhonDow')

    assert b'Hello, JhonDow! Happy birthday!' in response.data


def test_add_birthday_invalid_date(client):
    """Test case for add_birthday with invalid date"""
    response = client.put(
        '/hello/JhonSmith',
        json={
            'dateOfBirth': '1985-06-25-'
        }
    )

    assert response.status_code == 400


def test_get_birthday_invalid_username(mocker, client):
    """Test case for get_birthday with invalid username"""
    response = client.get('/hello/JhonSmith123')

    assert response.status_code == 400
