from abc import ABC, abstractmethod

from src.domain.hackney_address import HackneyAddress


class IAddressGateway(ABC):
    def __init__(self, connection_string: str):
        """
        :param connection_string: Connection string for address database
        """
        self.connection_string = connection_string
        
    @abstractmethod
    def get_addresses_for_postcode(self, postcode: str) -> list[HackneyAddress]:
        raise NotImplementedError
