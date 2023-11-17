from src.domain.hackney_address import HackneyAddress
from src.gateways.interfaces.i_address_gateway import IAddressGateway
from src.entities.hackney_address_entity import HackneyAddressEntity

from sqlalchemy import create_engine
from psycopg2 import connect as psycopg2_connect
from sqlalchemy.orm import sessionmaker, Session as HA_Session
from src.entities.hackney_address_entity import Base as AddressBase


class AddressGateway(IAddressGateway):
    """Gateway for accessing address database"""

    def __init__(self, connection_string: str):
        """
        :param connection_string: Connection string for address database
        """
        self.session = self._session_for_address_db(connection_string)

    def get_addresses_for_postcode(self, postcode: str) -> list[HackneyAddress]:
        """Finds addresses with exactly this postcode"""
        with self.session.begin() as session:
            db_addresses = (
                session.query(HackneyAddressEntity)
                .filter(HackneyAddressEntity.postcode == postcode)
                .all()
            )
        domain_addresses = [address.to_domain() for address in db_addresses]
        return domain_addresses

    def _session_for_address_db(self, connection_string) -> sessionmaker[HA_Session]:
        """
        Commence session with address database
        :param expire_on_commit: Select to persist detached objects after transaction commit
        :return: SQLAlchemy sessionmaker - to be used as a context manager
        """
        engine = create_engine(
            "postgresql://",
            creator=lambda: psycopg2_connect(connection_string),
            echo=True,
        )
        AddressBase.metadata.create_all(bind=engine)

        Session = sessionmaker(bind=engine, expire_on_commit=False)
        return Session


if __name__ == "__main__":
    _username, _password, _host, _port = ("postgres", "mypassword", "localhost", 5432)
    connection_string = f"postgresql://{_username}:{_password}@{_host}:{_port}/postgres"
    address_gateway = AddressGateway(connection_string)
    addresses = address_gateway.get_addresses_for_postcode("N16 6PS")
    print(addresses)
