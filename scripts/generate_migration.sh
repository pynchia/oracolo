#!/bin/bash
set -a
source .env
set +a
export DB__POSTGRES__URL=$DB__POSTGRES__URL_LOCAL
echo Generate migration based on local db $DB__POSTGRES__URL

docker compose up -d postgres
sleep 3

alembic revision --autogenerate -m "$1"

docker compose down postgres
