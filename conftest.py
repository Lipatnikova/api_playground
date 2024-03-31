import pytest
from dotenv import load_dotenv
import os
from config.base_host import BaseHost
from utils.http_handler import HTTPHandler


load_dotenv()


@pytest.fixture(autouse=True, scope="session")
def init_environment():
    HTTPHandler.post_headers(
        url=f'{BaseHost.HOST}/setup',
        headers={"Authorization": f"Bearer {os.getenv('API_TOKEN')}"}
    )
