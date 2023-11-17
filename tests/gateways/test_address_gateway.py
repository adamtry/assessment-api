from dataclasses import asdict

import pytest

from src.domain.hackney_address import HackneyAddress
from src.entities import hackney_address_entity as sql_schema
from faker import Faker

from src.gateways.address_gateway import AddressGateway
import psycopg2


@pytest.fixture
def connection_string():
    _username, _password, _host, _port = ("postgres", "mypassword", "localhost", 5432)
    return f"postgresql://{_username}:{_password}@{_host}:{_port}/postgres"


@pytest.fixture
def address():
    faker = Faker()
    """Address entity fixture with fake data"""
    # TODO: Use autofixture equivalent to generate fake data
    return sql_schema.HackneyAddressEntity(
        lpi_key=faker.pystr(),
        lpi_logical_status=faker.pystr(),
        lpi_start_date=faker.pyint(),
        lpi_end_date=faker.pyint(),
        lpi_last_update_date=faker.pyint(),
        usrn=faker.pyint(),
        uprn=faker.pyint(),
        parent_uprn=faker.pyint(),
        blpu_start_date=faker.pyint(),
        blpu_end_date=faker.pyint(),
        blpu_class=faker.pystr()[0:4],
        blpu_last_update_date=faker.pyint(),
        usage_description=faker.pystr(),
        usage_primary=faker.pystr(),
        property_shell=faker.pybool(),
        easting=faker.pyfloat(),
        northing=faker.pyfloat(),
        unit_number=faker.pyint(),
        sao_text=faker.pystr(),
        building_number=faker.pystr(),
        pao_text=faker.pystr(),
        paon_start_num=faker.pyint(),
        street_description=faker.pystr(),
        locality=faker.pystr(),
        ward=faker.pystr(),
        town=faker.pystr(),
        postcode=faker.postcode(),
        postcode_nospace=faker.postcode(),
        planning_use_class=faker.pystr(),
        neverexport=faker.pybool(),
        longitude=faker.pyfloat(),
        latitude=faker.pyfloat(),
        gazetteer=faker.pystr(),
        organisation=faker.pystr(),
        line1=faker.pystr(),
        line2=faker.pystr(),
        line3=faker.pystr(),
        line4=faker.pystr(),
    )


# TODO: Fix psycopg2 cross-platform issue
@pytest.fixture
def create_test_data(connection_string, address):
    # Create test data
    ps_connection = psycopg2.connect(connection_string)
    ps_cursor = ps_connection.cursor()

    ade_dict = asdict(address)
    query = "INSERT INTO hackney_address VALUES ("
    for key, value in ade_dict.items():
        query += f"'{str(value)[:8]}',"
    query = query[:-1] + ");"
    print(query)

    ps_cursor.execute(query)
    ps_connection.commit()


def test_get_addresses(address, connection_string, create_test_data):
    """Test that the use case returns the address domain objects from the gateway if found."""
    # Arrange
    _username, _password, _host, _port = ("postgres", "mypassword", "localhost", 5432)
    address_gateway = AddressGateway(connection_string)

    # Act
    addresses = address_gateway.get_addresses_for_postcode(address.postcode)

    # Assert
    assert len(addresses) == 1
    assert isinstance(addresses[0], HackneyAddress)
    assert addresses[0].postcode == address.postcode
    assert addresses[0].uprn == address.uprn


def test_get_addresses_no_results(address, connection_string):
    """Test that the gateway successfully returns an empty list when no addresses are found."""
    # Arrange
    _username, _password, _host, _port = ("postgres", "mypassword", "localhost", 5432)
    address_gateway = AddressGateway(connection_string)

    # Act
    addresses = address_gateway.get_addresses_for_postcode(address.postcode)

    # Assert
    assert len(addresses) == 0
