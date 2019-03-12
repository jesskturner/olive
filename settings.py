import os

APP_NAME = 'olive'
WEB_PORT = 8030


MYSQL_DB_NAME =  os.environ.get('MYSQL_DB_NAME', 'olive')
MYSQL_DB_HOSTNAME =  os.environ.get( 'MYSQL_DB_HOSTNAME', 'mysql')
MYSQL_DB_PORT = os.environ.get('MYSQL_DB_PORT', '3330')
MYSQL_DB_PASSWORD = os.environ.get('MYSQL_DB_PASSWORD')
MYSQL_DB_USERNAME = os.environ.get('MYSQL_DB_USERNAME', 'root')

MYSQL_DB_USER_PASS_KEY = (
    "{0}:{1}".format(MYSQL_DB_USERNAME, MYSQL_DB_PASSWORD)
    if MYSQL_DB_PASSWORD else MYSQL_DB_USERNAME
)
DATABASE_URL = (
    "mysql://{}@{}:{}/{}".format(
        MYSQL_DB_USER_PASS_KEY, MYSQL_DB_HOSTNAME, MYSQL_DB_PORT,
        MYSQL_DB_NAME
    )
)