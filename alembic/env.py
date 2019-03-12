from __future__ import with_statement
import os, sys
from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool


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


sys.path.append(os.getcwd())
# This is the Alembic Config object, which provides
# access to the values within the .ini file in use.
config = context.config

# Interpret the config file for Python logging.
# This line sets up loggers basically.
fileConfig(config.config_file_name)

# Add your model's MetaData object here
# for 'autogenerate' support
# from myapp import mymodel
# target_metadata = mymodel.Base.metadata
from olive.models import Base
target_metadata = Base.metadata

# other values from the config, defined by the needs of env.py,
# can be acquired:
# my_important_option = config.get_main_option("my_important_option")
# ... etc.


def run_migrations_offline():
    """Run migrations in 'offline' mode.

    This configures the context with just a URL
    and not an Engine, though an Engine is acceptable
    here as well.  By skipping the Engine creation
    we don't even need a DBAPI to be available.

    Calls to context.execute() here emit the given string to the
    script output.

    """
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url, target_metadata=target_metadata, literal_binds=True
    )

    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online():
    """Run migrations in 'online' mode.

    In this scenario we need to create an Engine
    and associate a connection with the context.

    """
    alembic_config = config.get_section(config.config_ini_section)
    alembic_config['sqlalchemy.url'] = DATABASE_URL

    connectable = engine_from_config(
        alembic_config,
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    # connectable = engine_from_config(
    #     config.get_section(config.config_ini_section),
    #     prefix="sqlalchemy.",
    #     poolclass=pool.NullPool,
    # )

    with connectable.connect() as connection:
        context.configure(
            connection=connection, target_metadata=target_metadata
        )

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
