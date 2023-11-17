PYTHON_PATH = venv/bin
# Replace with below if on Windows
# PYTHON_PATH = venv/Scripts

serve:
	${PYTHON_PATH}/python -m flask run

serve_docker:
	docker compose up assessment-api --build

local_db:
	docker-compose up sample-database

test:
	# Requires local db to be running for gateway tests
	${PYTHON_PATH}/python -m pytest

install:
	python3 -m venv venv
	${PYTHON_PATH}/pip install -r requirements.txt