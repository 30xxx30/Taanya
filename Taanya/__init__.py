from Taanya.core.bot import SHUKLA
from Taanya.core.dir import dirr
from Taanya.core.git import git
from Taanya.core.userbot import Userbot
from Taanya.misc import dbb, heroku

from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = SHUKLA()
userbot = Userbot()
api = SafoneAPI()


from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()

APP = "ll_DRAGON_MUSIC_BOT"  # connect music api key "Dont change it"
