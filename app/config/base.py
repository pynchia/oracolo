import pathlib

from pydantic_settings import BaseSettings, SettingsConfigDict


APP_ROOT_PATH = pathlib.Path(__file__).parent.parent.parent
ENV_FILE_NAME = pathlib.Path(".env")
ENV_FILE_PATH = APP_ROOT_PATH / ENV_FILE_NAME


class AppBaseSettings(BaseSettings):
    model_config = SettingsConfigDict(
        extra="forbid",
        env_nested_delimiter="__",
    )
