from datetime import date
from typing import Optional

from sqlalchemy import Date, ForeignKey, Index, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Customer(Base):
    __tablename__ = "customer"

    customer_id: Mapped[int] = mapped_column(primary_key=True)
    last_name: Mapped[str] = mapped_column(String(40))
    first_name: Mapped[str] = mapped_column(String(40))
    company: Mapped[Optional[str]] = mapped_column(String(30))
    address: Mapped[Optional[str]] = mapped_column(String(70))
    city: Mapped[Optional[str]] = mapped_column(String(40))
    state: Mapped[Optional[str]] = mapped_column(String(40))
    country: Mapped[Optional[str]] = mapped_column(String(40))
    postal_code: Mapped[Optional[str]] = mapped_column(String(10))
    phone: Mapped[Optional[str]] = mapped_column(String(24))
    fax: Mapped[Optional[str]] = mapped_column(String(24))
    email: Mapped[str] = mapped_column(String(320))
    support_rep_id = mapped_column(ForeignKey("employee.employee_id"), nullable=True)

    __table_args__ = (
        Index("customer_IX1", "last_name"),
        Index("customer_IX2", "first_name"),
        Index("customer_IX3", "email"),
        Index("customer_IX4", "support_rep_id"),
    )

    def __repr__(self) -> str:
        return (
            "Customer("
            "customer_id={customer_id!r}, "
            "last_name={last_name!r}, "
            "first_name={first_name!r}, "
            "company={company!r}, "
            "address={address!r}, "
            "city={city!r}, "
            "state={state!r}, "
            "country={country!r}, "
            "postal_code={postal_code!r}, "
            "phone={phone!r}, "
            "fax={fax!r}, "
            "email={email!r}, "
            "support_rep_id={support_rep_id!r} "
            ")"
        ).format(
            customer_id=self.customer_id,
            last_name=self.last_name,
            first_name=self.first_name,
            company=self.company,
            address=self.address,
            city=self.city,
            state=self.state,
            country=self.country,
            postal_code=self.postal_code,
            phone=self.phone,
            fax=self.fax,
            email=self.email,
            support_rep_id=self.support_rep_id,
        )
