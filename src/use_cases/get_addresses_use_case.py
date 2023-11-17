import os
from src.boundary.hackney_address_response import HackneyAddressResponse
from src.gateways.interfaces.i_address_gateway import IAddressGateway


class GetAddressesUseCase:
    def __init__(self, address_gateway: IAddressGateway):
        self.gateway = address_gateway

    def execute(self, postcode: str) -> list[HackneyAddressResponse]:
        addresses = self.gateway.get_addresses_for_postcode(postcode)
        return [address.to_response() for address in addresses]


if __name__ == "__main__":
    from src.gateways.address_gateway import AddressGateway

    _username = os.getenv("DB_USERNAME")
    _password = os.getenv("DB_PASSWORD")
    _host = os.getenv("DB_HOST")
    _port = os.getenv("DB_PORT")
    connection_string = f"postgresql://{_username}:{_password}@{_host}:{_port}/postgres"
    address_gateway = AddressGateway(connection_string)
    use_case = GetAddressesUseCase(address_gateway)
    addresses = use_case.execute("N16 6PS")
    print(addresses)
