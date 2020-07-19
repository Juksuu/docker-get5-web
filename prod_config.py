import os

##### You must change these before running
SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')  # Sqlalchemy database connection info
STEAM_API_KEY = os.environ.get('STEAM_API_KEY')  # See https://steamcommunity.com/dev/apikey
SECRET_KEY = os.environ.get('SECRET_KEY')  # Secret key used for flask cookies

##### Everything below this line is optional to change

location = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__), '..', 'logs'))
LOG_PATH = os.path.join(location, 'get5.log')

DEBUG = False
TESTING = False

SQLALCHEMY_TRACK_MODIFICATIONS = False
USER_MAX_SERVERS = 10  # Max servers a user can create
USER_MAX_TEAMS = 100  # Max teams a user can create
USER_MAX_MATCHES = 1000  # Max matches a user can create
DEFAULT_PAGE = '/matches'
ADMINS_ACCESS_ALL_MATCHES = True  # Whether admins can always access any match admin panel
CREATE_MATCH_TITLE_TEXT = False # Whether settings for "match title text" and "team text" appear on "create a match page"

# All maps that are selectable in the "create a match" page
MAPLIST = os.environ.get('MAPLIST', '').split(',')

# Maps whose checkbox is selected (in the mappool) by default in the "create a match" page
DEFAULT_MAPLIST = os.environ.get('DEFAULT_MAPLIST', '').split(',')

# You may set the server to allow allow whitelisted steamids to login.
# By default any user can login and create teams/servers/matches.
WHITELISTED_IDS = []

# Admins will have extra access to create "public" teams, and if ADMINS_ACCESS_ALL_MATCHES
# is set, they can access admin info for all matches (can pause, cancel, etc.) ANY match.
ADMIN_IDS = os.environ.get('ADMIN_IDS', '').split(',')

# The spectator value is for observers and other personnel 
# that need to be able to join the server, while the game is live or in the warmup. And would otherwise get kicked by the game.
SPECTATOR_IDS = []

# This specifies how much spectators are needed to ready up to get the match started/live
# this is an optional configuration
# MIN_SPECTATORS_TO_READY = 0

# This overrides the default way to build the config URL that get appended to the get5_loadmatch_url rcon command.
# Uncomment and use this if you need to set another ip for your get5 instance than the public ip you're using get5 with
# in your browser.
# GET5_URL_OVERRIDE = '127.0.0.1'
