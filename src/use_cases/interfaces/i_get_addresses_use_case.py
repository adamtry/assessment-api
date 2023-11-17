from abc import abstractmethod, ABC

from src.boundary.hackney_address_response import HackneyAddressResponse


class IGetAddressesUseCase(ABC):
    @abstractmethod
    def execute(self, postcode: str) -> list[HackneyAddressResponse]:
        raise NotImplementedError
