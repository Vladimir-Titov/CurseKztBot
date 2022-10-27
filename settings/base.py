from pathlib import Path
from environs import Env

env = Env()
BASE_PATH = Path.cwd().absolute()
env.read_env(BASE_PATH / '.env')
