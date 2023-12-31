# Fake Addresses API

API for fetching address details from an address database.

Based on the [LBH Base API](https://github.com/LBHackney-IT/lbh-base-api)

## Stack

- Flask as a web framework.
- SQLAlchemy as an ORM.
- PyTest as a test framework.

## Contributing

### Setup

1. Install [Docker][docker-download].
2. Install a recent version of [Python][python-install].
3. Clone this repository.
4. Install dependencies in a venv with `make install`
5. Activate the venv with `source venv/bin/activate` on MacOS/Linux or `venv\Scripts\activate` on Windows
6. Open the project in your IDE

### Running locally

1. Open the `Makefile` and set the `PYTHON_PATH` depending on your OS (see comment in file)
2. Run `make local_db` to start the local database
3. Run `make serve` to start the API
4. Connect to the API at `localhost:5000`

You can alternatively run the API with Docker with `make serve_docker` - check the console for the hostname to connect to

## Testing

### Run the tests
1. Spin up the local database with `make local_db`
2. Run the tests with `make test`
3. You could instead run the tests with Docker with `make test_docker`

## Contacts

### Maintainers

- **Adam Tracy**, Associate Software Engineer at London Borough of Hackney (adam.tracy@hackney.gov.uk)

[docker-download]: https://www.docker.com/products/docker-desktop
[python-install]: https://www.python.org/downloads/
