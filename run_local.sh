#!/bin/bash
set -a
source .env
set +a
export DB__POSTGRES__URL=$DB__POSTGRES__URL_LOCAL
echo Run app locally against local db $DB__POSTGRES__URL

docker compose up -d postgres
sleep 3

fastapi dev app/main.py --host 0.0.0.0 --port 8000 --reload

docker compose down postgres
