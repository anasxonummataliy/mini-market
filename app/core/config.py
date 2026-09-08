from pydantic import BaseSettings


class Conf(BaseSettings):
    PG_USER: str
    PG_PASSWORD: str
    PG_DB: str
    PG_HOST: str
    PG_PORT: int

    REDIS_HOST: str
    REDIS_PORT: int

    model_config = {
        "env_file": ".env",
        "env_file_encoding": "utf-8",
    }


conf = Conf()
