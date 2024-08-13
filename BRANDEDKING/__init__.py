from BRANDEDKING.core.bot import BRANDED
from BRANDEDKING.core.dir import dirr
from BRANDEDKING.core.git import git
from BRANDEDKING.core.userbot import Userbot
from BRANDEDKING.misc import dbb, heroku, sudo

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
