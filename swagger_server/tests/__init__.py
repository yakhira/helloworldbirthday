import logging
import connexion
import pytest

from swagger_server.encoder import JSONEncoder
from swagger_server.tests.mocks.database import dbconnection_mock


def create_app():
    """Create flask app."""
    logging.getLogger('connexion.operation').setLevel('ERROR')
    app = connexion.App(__name__, specification_dir='../swagger/')
    app.app.json_encoder = JSONEncoder
    app.add_api('swagger.yaml')

    return app.app


@pytest.fixture
def client(mocker):
    """Create client pytest fixture."""
    mocker.patch(
        'swagger_server.utils.database.DBConnection',
        new=dbconnection_mock
    )
    return create_app().test_client()
