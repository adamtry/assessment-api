from abc import ABC, abstractmethod


class IAddressGateway(ABC):
    def __init__(self, connection_string: str):
        """
        :param connection_string: Connection string for address database
        """
        self.connection_string = connection_string
    @abstractmethod
    def get_addresses_for_postcode(self, postcode: str):
        raise NotImplementedError
