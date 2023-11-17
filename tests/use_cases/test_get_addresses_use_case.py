from src.boundary.hackney_address_response import HackneyAddressResponse
from src.domain.hackney_address import HackneyAddress
from src.gateways.interfaces.i_address_gateway import IAddressGateway
from src.use_cases.get_addresses_use_case import GetAddressesUseCase
from faker import Faker
from unittest.mock import Mock


faker = Faker()
MOCK_ADDRESS = HackneyAddress(
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
            blpu_class=faker.pystr(),
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
            line4=faker.pystr()
        )


def test_get_addresses():
    """Test that the use case returns the address domain objects from the gateway."""
    # Arrange
    mock_address_gateway = Mock(spec=IAddressGateway)
    mock_address_gateway.get_addresses_for_postcode.return_value = [MOCK_ADDRESS]

    # Act
    use_case = GetAddressesUseCase(mock_address_gateway)
    addresses = use_case.execute(MOCK_ADDRESS.postcode)

    # Assert
    assert len(addresses) == 1
    assert isinstance(addresses[0], HackneyAddressResponse)
    assert addresses[0].postcode == MOCK_ADDRESS.postcode
    assert addresses[0].uprn == MOCK_ADDRESS.uprn
    mock_address_gateway.get_addresses_for_postcode.assert_called_once_with(MOCK_ADDRESS.postcode)


def test_get_addresses_no_results():
    """Test that the use case successfully returns an empty list when no addresses are found."""
    # Arrange
    mock_address_gateway = Mock(spec=IAddressGateway)
    mock_address_gateway.get_addresses_for_postcode.return_value = []

    # Act
    use_case = GetAddressesUseCase(mock_address_gateway)
    addresses = use_case.execute(MOCK_ADDRESS.postcode)

    # Assert
    assert len(addresses) == 0
    mock_address_gateway.get_addresses_for_postcode.assert_called_once_with(MOCK_ADDRESS.postcode)

