PYTHON_PATH = venv/bin
# Replace with below if on Windows
# PYTHON_PATH = venv/Scripts

serve:
	${PYTHON_PATH}/python -m flask run

local_db:
	docker-compose up sample-database

test:
	${PYTHON_PATH}/python -m pytest