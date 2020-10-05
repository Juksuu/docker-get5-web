import os

##### You must change these before running
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')  # Sqlalchemy database connection info
STEAM_API_KEY = os.environ.get('STEAM_API_KEY')  # See https://steamcommunity.com/dev/apikey
SECRET_KEY = os.environ.get('SECRET_KEY')  # Secret key used for flask cookies
DATABASE_KEY = os.environ.get('DATABASE_KEY')  # Used for encryption on database. MUST BE 16 BYTES.
WEBPANEL_NAME = os.environ.get('WEBPANEL_NAME') # Used for the title header on the webpage.
JSON_AS_ASCII = False #UTF-8 Encoding Issue.
CUSTOM_PLAYER_NAMES = True

##### Everything below this line is optional to change

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__), '..', 'logs'))
LOG_PATH = os.path.join(location, 'get5.log')

DEBUG = False
TESTING = False

SQLALCHEMY_TRACK_MODIFICATIONS = False
USER_MAX_SERVERS = 10  # Max servers a user can create
USER_MAX_TEAMS = 100  # Max teams a user can create
USER_MAX_MATCHES = 1000  # Max matches a user can create
USER_MAX_SEASONS = 100 # Max seasons a user can create
DEFAULT_PAGE = '/matches'
ADMINS_ACCESS_ALL_MATCHES = True  # Whether admins can always access any match admin panel
CREATE_MATCH_TITLE_TEXT = False # Whether settings for "match title text" and "team text" appear on "create a match page"

# All maps that are selectable in the "create a match" page
MAPLIST = os.environ.get('MAPLIST', '').split(',')

# Maps whose checkbox is selected (in the mappool) by default in the "create a match" page
DEFAULT_MAPLIST = os.environ.get('DEFAULT_MAPLIST', '').split(',')

# You may set the game server to allow whitelisted steam ids to specatate.
# By default, NO users can spectate matches.
# Change [] out with your own SteamID. Example ["STEAMID64"]
SPECTATOR_IDS = os.environ.get('SPECTATOR_IDS', '').split(',')

# You may set the server to allow allow whitelisted steamids to login.
# By default any user can login and create teams/servers/matches.
# Change [] out with your own SteamID. Example ["STEAMID64"]
WHITELISTED_IDS = os.environ.get('WHITELISTED_IDS', '').split(',')

# Admins will have extra access to create "public" teams, and if ADMINS_ACCESS_ALL_MATCHES
# is set, they can access admin info for all matches (can pause, cancel, etc.) ANY match.
# Change [] out with your own SteamID. Example ["STEAMID64"]
ADMIN_IDS = os.environ.get('ADMIN_IDS', '').split(',')

# Super admins will have the most access, as if ADMINS_ACCESS_ALL_MATCHES was set.
# They'll be able to access EVERYTHING for ANY match, as well as FORFEIT matches.
# Change [] out with your own SteamID. Example ["STEAMID64"]
SUPER_ADMIN_IDS = os.environ.get('SUPER_ADMIN_IDS', '').split(',')

# This overrides the default way to build the config URL that get appended to the get5_loadmatch_url rcon command.
# Uncomment and use this if you need to set another ip for your get5 instance than the public ip you're using get5 with
# in your browser.
GET5_URL_OVERRIDE = os.environ.get('GET5_URL_OVERRIDE')
