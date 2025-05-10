import logging

from .source import SourceSettings
from .base import AppBaseSettings
from .db import DatabaseSettings
from .logging import LoggingSettings


class AppSettings(AppBaseSettings):
    source: SourceSettings
    db: DatabaseSettings
    logging: LoggingSettings


APP_CFG = AppSettings()

# print(APP_CFG.model_dump_json(indent=2))

logger = logging.getLogger()
logger.setLevel(APP_CFG.logging.level)
