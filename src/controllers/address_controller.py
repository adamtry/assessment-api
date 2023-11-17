import re
from urllib.parse import unquote

from flask import Blueprint

from src.gateways.address_gateway import AddressGateway
from src.use_cases.get_addresses_use_case import GetAddressesUseCase

POSTCODE_REGEX = r"[A-Za-z][1-9] [1-9][A-Za-z]{2}"

_username, _password, _host, _port = ("postgres", "mypassword", "localhost", 5432)
connection_string = f"postgresql://{_username}:{_password}@{_host}:{_port}/postgres"
ADDRESS_GATEWAY = AddressGateway(connection_string)
GET_ADDRESSES_USE_CASE = GetAddressesUseCase(ADDRESS_GATEWAY)

address_controller = Blueprint('address_controller', __name__)


@address_controller.route('/addresses/<postcode>', methods=['GET'])
def get_addresses_for_postcode(postcode: str):
    postcode = unquote(postcode).strip()
    if not postcode:
        return "No postcode provided", 400
    if not re.match(POSTCODE_REGEX, postcode):
        return f"Validation error: Postcode {postcode} is not valid", 400
    addresses = GET_ADDRESSES_USE_CASE.execute(postcode)
    if not addresses:
        return f"No addresses found for postcode {postcode}", 404
    return addresses, 200
