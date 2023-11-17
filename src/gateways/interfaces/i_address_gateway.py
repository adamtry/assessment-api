from abc import ABC, abstractmethod

from src.domain.hackney_address import HackneyAddress
from sqlalchemy.orm import sessionmaker, Session as HA_Session


class IAddressGateway(ABC):
    def __init__(self, connection_string: str):
        """
        :param connection_string: Connection string for address database
        """
        self.session = self._session_for_address_db(connection_string)

    @abstractmethod
    def get_addresses_for_postcode(self, postcode: str) -> list[HackneyAddress]:
        raise NotImplementedError

    @abstractmethod
    def _session_for_address_db(self, connection_string: str) -> sessionmaker[HA_Session]:
        raise NotImplementedError
