from abc import abstractmethod, ABC


class IGetAddressesUseCase(ABC):
    @abstractmethod
    def execute(self, postcode: str):
        raise NotImplementedError
