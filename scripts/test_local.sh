#!/bin/bash
set -a
source .env
set +a
export DB__POSTGRES__URL=$DB__POSTGRES__URL_TEST_LOCAL
echo Run tests locally against test db $DB__POSTGRES__URL

docker compose up -d test-postgres
sleep 3

pytest tests/ -vv --cov=. --cov-report xml:coverage.xml --cov-report=term-missing

docker compose down -v test-postgres
