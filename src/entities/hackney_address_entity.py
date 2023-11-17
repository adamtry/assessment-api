from dataclasses import dataclass, asdict

from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase, MappedAsDataclass, Mapped, mapped_column

from src.domain.hackney_address import HackneyAddress


class Base(MappedAsDataclass, DeclarativeBase):
    pass


@dataclass
class HackneyAddressEntity(Base):
    __tablename__ = "hackney_address"
    __table_args__ = {"schema": "public"}

    lpi_key: Mapped[str] = mapped_column(String(14), primary_key=True)
    lpi_logical_status: Mapped[str] = mapped_column(String(18))
    lpi_start_date: Mapped[int] = mapped_column()
    lpi_end_date: Mapped[int] = mapped_column()
    lpi_last_update_date: Mapped[int] = mapped_column()
    usrn: Mapped[int] = mapped_column()
    uprn: Mapped[int] = mapped_column()
    parent_uprn: Mapped[int] = mapped_column()
    blpu_start_date: Mapped[int] = mapped_column()
    blpu_end_date: Mapped[int] = mapped_column()
    blpu_class: Mapped[str] = mapped_column(String(4))
    blpu_last_update_date: Mapped[int] = mapped_column()
    usage_description: Mapped[str] = mapped_column(String(160))
    usage_primary: Mapped[str] = mapped_column(String(160))
    property_shell: Mapped[bool] = mapped_column()
    easting: Mapped[float] = mapped_column()
    northing: Mapped[float] = mapped_column()
    unit_number: Mapped[int] = mapped_column()
    sao_text: Mapped[str] = mapped_column(String(90))
    building_number: Mapped[str] = mapped_column(String(17))
    pao_text: Mapped[str] = mapped_column(String(90))
    paon_start_num: Mapped[int] = mapped_column()
    street_description: Mapped[str] = mapped_column(String(100))
    locality: Mapped[str] = mapped_column(String(100))
    ward: Mapped[str] = mapped_column(String(100))
    town: Mapped[str] = mapped_column(String(100))
    postcode: Mapped[str] = mapped_column(String(8))
    postcode_nospace: Mapped[str] = mapped_column(String(8))
    planning_use_class: Mapped[str] = mapped_column(String(50))
    neverexport: Mapped[bool] = mapped_column()
    longitude: Mapped[float] = mapped_column()
    latitude: Mapped[float] = mapped_column()
    gazetteer: Mapped[str] = mapped_column(String(8))
    organisation: Mapped[str] = mapped_column(String(100))
    line1: Mapped[str] = mapped_column(String(200))
    line2: Mapped[str] = mapped_column(String(200))
    line3: Mapped[str] = mapped_column(String(200))
    line4: Mapped[str] = mapped_column(String(100))

    to_dict = asdict

    def __repr__(self) -> str:
        return f"HackneyAddress(uprn={self.uprn!r}, line1={self.line1!r}, postcode={self.postcode!r})"

    def to_domain(self) -> HackneyAddress:
        return HackneyAddress(**asdict(self))
