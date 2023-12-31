PYTHON_PATH = venv/bin
# Replace with below if on Windows
# PYTHON_PATH = venv/Scripts

serve:
	${PYTHON_PATH}/python -m flask run

serve_docker:
	docker compose up assessment-api --build

local_db:
	docker compose up sample-database

test:
	# Requires local db to be running for gateway tests
	DB_USERNAME='postgres' DB_PASSWORD='mypassword' DB_HOST='localhost' DB_PORT='5432' ${PYTHON_PATH}/python -m pytest

test_docker:
	docker compose build assessment-api-test && docker compose run assessment-api-test

install:
	python3 -m venv venv
	${PYTHON_PATH}/pip install -r requirements.txt