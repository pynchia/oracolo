# import pathlib

import pytest
# import sqlalchemy as sa

from app.api.deps.db import session_manager
# from tests.util.alembic import apply_migrations, downgrade_migrations


@pytest.fixture
async def db_session():
    async with session_manager.session() as session:
        yield session


# The following fixtures are not needed for SQLite

# remove the session scope if the application creates/updates any data
# @pytest.fixture(scope="session", autouse=True)
# def setup_db():
#     apply_migrations()


# remove the session scope if the application creates/updates any data
# @pytest.fixture(scope="session", autouse=True)
# async def reset_db(setup_db):
#     yield
#     downgrade_migrations()


# Note: remove the session scope (and/or autouse) if the application creates/updates any data
# @pytest.fixture(scope="session", autouse=True)
# async def dataset(setup_db):
#     data_dir = pathlib.Path("tests/fixtures/postgres_db_data")
#     async with session_manager.session() as session:
#         for data_file_name in (
#             "activity.sql",
#             "activity_contributor.sql",
#             "country_code_name.sql",
#             "organization.sql",
#             "organization_alias.sql",
#             "organization_link.sql",
#             "organization_list.sql",
#             "researcher.sql",
#             "researcher_activity.sql",
#             "researcher_orcid.sql",
#             "researcher_organization.sql",
#         ):
#             data_file = data_dir / data_file_name
#             if not data_file.exists():
#                 raise FileNotFoundError(f"Data file {data_file} does not exist")
#             query = sa.text(data_file.read_text())
#             # TODO with a more sophisticated session
#             # this too may be executed concurrently:
#             #   the entities concurrently
#             #   then the relationships concurrently
#             await session.execute(query)
#         await session.commit()
