import pytest
from dotenv import load_dotenv
import os
import requests
from config.base_host import BaseHost


load_dotenv()


@pytest.fixture(autouse=True, scope="session")
def init_environment():
    response = requests.post(
        url=f'{BaseHost.HOST}/setup',
        headers={"Authorization": f"Bearer {os.getenv('API_TOKEN')}"}
    )
    assert response.status_code == 205
