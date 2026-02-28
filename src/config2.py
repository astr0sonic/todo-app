import os
from dataclasses import dataclass

from dotenv import load_dotenv


@dataclass
class Config:
    port: int


load_dotenv()


port_str = os.getenv("PORT")
if port_str is None:
    print("PORT is not set")
    exit(1)

config = Config(port=int(port_str))
