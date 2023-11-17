from unittest.mock import Mock

from faker import Faker

from src.boundary.hackney_address_response import HackneyAddressResponse
from src.controllers.address_controller import get_addresses_for_postcode
from src.use_cases.interfaces.i_get_addresses_use_case import IGetAddressesUseCase

faker = Faker()
MOCK_ADDRESS_RESPONSE = HackneyAddressResponse(
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
    postcode="N16 6PS",
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


def test_get_addresses_for_postcode_returns_data():
    # Arrange
    postcode = MOCK_ADDRESS_RESPONSE.postcode
    mock_address_use_case = Mock(spec=IGetAddressesUseCase)
    mock_address_use_case.execute.return_value = [MOCK_ADDRESS_RESPONSE]

    # Act
    response, response_code = get_addresses_for_postcode(postcode, mock_address_use_case)

    # Assert
    assert response_code == 200
    assert isinstance(response[0], HackneyAddressResponse)
    assert len(response) == 1
    assert response[0].postcode == postcode


def test_get_addresses_for_empty_postcode_returns_400():
    # Arrange
    postcode = ""
    mock_address_use_case = Mock(spec=IGetAddressesUseCase)
    mock_address_use_case.execute.return_value = [MOCK_ADDRESS_RESPONSE]

    # Act
    response, response_code = get_addresses_for_postcode(postcode, mock_address_use_case)

    # Assert
    assert response_code == 400
    assert isinstance(response, str)
    assert response == "No postcode provided"


def test_get_addresses_for_invalid_postcode_returns_400():
    # Arrange
    postcode = "invalid"
    mock_address_use_case = Mock(spec=IGetAddressesUseCase)
    mock_address_use_case.execute.return_value = [MOCK_ADDRESS_RESPONSE]

    # Act
    response, response_code = get_addresses_for_postcode(postcode, mock_address_use_case)

    # Assert
    assert response_code == 400
    assert isinstance(response, str)
    assert response == "Validation error: Postcode invalid is not valid"

