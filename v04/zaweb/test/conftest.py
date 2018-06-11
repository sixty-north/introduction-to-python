import pytest
from zaweb import create_app


@pytest.fixture
def app():
    return create_app()
