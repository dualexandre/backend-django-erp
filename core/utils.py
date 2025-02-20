import os
from pathlib import Path
from dotenv import load_dotenv

BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, ".env"))

class ConfigHelper:
    @staticmethod
    def get_env_str(var_name, default=""):
        return os.getenv(var_name, default)

    @staticmethod
    def get_env_bool(var_name, default=False):
        return os.getenv(var_name, str(default)).lower() in ('true', '1', 'yes', 'on')

    @staticmethod
    def get_env_int(var_name, default=0):
        try:
            return int(os.getenv(var_name, default))
        except ValueError:
            return default
