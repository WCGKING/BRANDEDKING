from BRANDED X KING.core.bot import BRANDED
from BRANDED X KING.core.dir import dirr
from BRANDED X KING.core.git import git
from BRANDED X KING.core.userbot import Userbot
from BRANDED X KING.misc import dbb, heroku, sudo

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = BRANDED()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
