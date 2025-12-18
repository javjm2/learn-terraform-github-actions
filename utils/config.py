import requests
import os
from pydantic_settings import BaseSettings

class Config(BaseSettings):
    HOSTNAME: str = '127.0.0.1:62660'

    @property
    def base_url(self) -> str:
        if self.HOSTNAME.startswith("http"):
            return self.HOSTNAME
        return f"http://{self.HOSTNAME}"

    def config_requests(self):
        session = requests.session()

        session.headers.update(
            {
                "accept": "application/json",
                "Authorization": f"Bearer token={os.environ.get('API_KEY')}",
            }
        )
        return session

