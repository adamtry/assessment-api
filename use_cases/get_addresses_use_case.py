from gateways.interfaces.i_address_gateway import IAddressGateway


class GetAddressesUseCase:
    def __init__(self, address_gateway: IAddressGateway):
        self.gateway = address_gateway

    def execute(self, postcode: str):
        return self.gateway.get_addresses_for_postcode(postcode)


if __name__ == "__main__":
    from gateways.address_gateway import AddressGateway
    _username, _password, _host, _port = ("postgres", "mypassword", "localhost", 5432)
    connection_string = f"postgresql://{_username}:{_password}@{_host}:{_port}/postgres"
    address_gateway = AddressGateway(connection_string)
    use_case = GetAddressesUseCase(address_gateway)
    addresses = use_case.execute("N16 6PS")
    print(addresses)
