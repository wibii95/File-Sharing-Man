import sys

from bot import Bot
from config import ADMINS, LOGGER, OWNER_ID, blacklistman

try:
    Bot().run()
    if OWNER_ID and ADMINS in blacklistman:
        print(
            "MAKANYA GA USAH BERTINGKAH GOBLOK, BOTnya GUA MATIIN NAJIS BANGET DIPAKE JAMET KEK LU.\nCredits: @mrismanaziz"
        )
        sys.exit(1)
except Exception as e:
    print(str(e), exc_info=True)
    sys.exit(1)
