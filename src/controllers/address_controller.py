import os
import re
from urllib.parse import unquote

from flask import Blueprint

from src.gateways.address_gateway import AddressGateway
from src.use_cases.get_addresses_use_case import GetAddressesUseCase

POSTCODE_REGEX = r"[A-Za-z][1-9]{1,2} [1-9][A-Za-z]{2}"

_username = os.getenv("DB_USERNAME")
_password = os.getenv("DB_PASSWORD")
_host = os.getenv("DB_HOST")
_port = os.getenv("DB_PORT")
if not _username:
    print("Warning: No DB_USERNAME environment variable set")
    _username = "postgres"
if not _password:
    print("Warning: No DB_PASSWORD environment variable set")
    _password = "mypassword"
if not _host:
    print("Warning: No DB_HOST environment variable set")
    _host = "localhost"
if not _port:
    print("Warning: No DB_PORT environment variable set")
    _port = 5432

connection_string = f"postgresql://{_username}:{_password}@{_host}:{_port}/postgres"
ADDRESS_GATEWAY = AddressGateway(connection_string)
GET_ADDRESSES_USE_CASE = GetAddressesUseCase(ADDRESS_GATEWAY)

address_controller = Blueprint("address_controller", __name__)


@address_controller.route("/addresses/<postcode>", methods=["GET"])
def get_addresses_for_postcode(postcode: str, use_case=GET_ADDRESSES_USE_CASE):
    postcode = unquote(postcode).strip()
    if not postcode:
        return "No postcode provided", 400
    if not re.match(POSTCODE_REGEX, postcode):
        return f"Validation error: Postcode {postcode} is not valid", 400
    addresses = use_case.execute(postcode)
    if not addresses:
        return f"No addresses found for postcode {postcode}", 404
    return addresses, 200
