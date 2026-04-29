import asyncio
from logging.config import fileConfig

from sqlalchemy import pool
from sqlalchemy.engine import Connection
from sqlalchemy.ext.asyncio import async_engine_from_config

from alembic import context

# ✅ ВАЖЛИВО: Імпортуй свою Base і DATABASE_URL
from database import Base, DATABASE_URL

# ✅ ВАЖЛИВО: Імпортуй ВСІ свої моделі
from models.books import BookModel
# Якщо додаси нові моделі, імпортуй їх тут!

# Конфіг Alembic
config = context.config

# ✅ Встановлюємо DATABASE_URL з .env
config.set_main_option("sqlalchemy.url", DATABASE_URL)

# Налаштування логування
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# ✅ ВАЖЛИВО: Вказуємо metadata з наших моделей
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Міграції в offline режимі (без підключення до БД)"""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )

    with context.begin_transaction():
        context.run_migrations()


def do_run_migrations(connection: Connection) -> None:
    context.configure(connection=connection, target_metadata=target_metadata)

    with context.begin_transaction():
        context.run_migrations()


async def run_async_migrations() -> None:
    """Міграції в async режимі (для asyncpg)"""
    connectable = async_engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    async with connectable.connect() as connection:
        await connection.run_sync(do_run_migrations)

    await connectable.dispose()


def run_migrations_online() -> None:
    """Міграції в online режимі"""
    asyncio.run(run_async_migrations())


# Вибираємо режим
if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()
