#!/bin/bash
set -a
source .env
set +a
export DB__POSTGRES__URL=$DB__POSTGRES__URL_LOCAL
echo Apply migrations to local db $DB__POSTGRES__URL

docker compose up -d postgres
sleep 3

alembic upgrade head

docker compose down postgres
