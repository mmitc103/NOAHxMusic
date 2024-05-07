from NOAHxMusic.core.bot import Hotty
from NOAHxMusic.core.dir import dirr
from NOAHxMusic.core.git import git
from NOAHxMusic.core.userbot import Userbot
from NOAHxMusic.misc import dbb, heroku

from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Hotty()
userbot = Userbot()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
