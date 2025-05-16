# --------------M----------------------------------

import os
from os import getenv
# ---------------R---------------------------------
API_ID = int(os.environ.get("API_ID", "28227907"))
# ------------------------------------------------
API_HASH = os.environ.get("API_HASH", "bc3acb5bd0282fe4fd076cec1f24df62")
# ----------------D--------------------------------
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7987339891:AAGL1CNFqUiGGRl4pwbYloJfE0eDnS39sjo")
# -----------------A-------------------------------
BOT_USERNAME = os.environ.get("@Gffrrrrrrrebot")
# ------------------X------------------------------
OWNER_ID = int(os.environ.get("OWNER_ID", "919335654"))
# ------------------X------------------------------

SUDO_USERS = list(map(int, getenv("SUDO_USERS", "919335654").split()))
# ------------------------------------------------
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", "-1002558774598"))
# ------------------------------------------------
MONGO_URL = os.environ.get("MONGO_URL", "mongodb+srvter")
# -----------------------------------------------
PREMIUM_LOGS = int(os.environ.get("PREMIUM_LOGS", "-1002275697950"))

