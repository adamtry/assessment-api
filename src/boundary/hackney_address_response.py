from dataclasses import dataclass


@dataclass
class HackneyAddressResponse:
    lpi_key: str
    lpi_logical_status: str
    lpi_start_date: int
    lpi_end_date: int
    lpi_last_update_date: int
    usrn: int
    uprn: int
    parent_uprn: int
    blpu_start_date: int
    blpu_end_date: int
    blpu_class: str
    blpu_last_update_date: int
    usage_description: str
    usage_primary: str
    property_shell: bool
    easting: float
    northing: float
    unit_number: int
    sao_text: str
    building_number: str
    pao_text: str
    paon_start_num: int
    street_description: str
    locality: str
    ward: str
    town: str
    postcode: str
    postcode_nospace: str
    planning_use_class: str
    neverexport: bool
    longitude: float
    latitude: float
    gazetteer: str
    organisation: str
    line1: str
    line2: str
    line3: str
    line4: str