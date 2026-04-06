from datetime import date
from typing import Optional

from sqlalchemy import Date, ForeignKey, Index, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from tests.shared_code.infra.database.sqlalchemy.orm.entity.base import Base


class Invoice(Base):
    __tablename__ = "invoice"

    invoice_id: Mapped[int] = mapped_column(primary_key=True)
    customer_id = mapped_column(ForeignKey("customer.customer_id"), nullable=True)
    invoice_date: Mapped[date] = mapped_column(Date, nullable=True)
    billing_address: Mapped[Optional[str]] = mapped_column(String(70))
    billing_city: Mapped[Optional[str]] = mapped_column(String(40))
    billing_state: Mapped[Optional[str]] = mapped_column(String(40))
    billing_country: Mapped[Optional[str]] = mapped_column(String(40))
    billing_postal_code: Mapped[Optional[str]] = mapped_column(String(10))
    total: Mapped[int] = mapped_column(Integer)

    __table_args__ = (
        Index("invoice_IX1", "customer_id"),
        Index("invoice_IX2", "invoice_date"),
    )

    def __repr__(self) -> str:
        return (
            "Invoice("
            "invoice_id={invoice_id!r}, "
            "customer_id={customer_id!r}, "
            "invoice_date={invoice_date!r}, "
            "billing_address={billing_address!r}, "
            "billing_city={billing_city!r}, "
            "billing_state={billing_state!r}, "
            "billing_country={billing_country!r}, "
            "billing_postal_code={billing_postal_code!r}, "
            "total={total!r}"
            ")"
        ).format(
            invoice_id=self.invoice_id,
            customer_id=self.customer_id,
            invoice_date=self.invoice_date,
            billing_address=self.billing_address,
            billing_city=self.billing_city,
            billing_state=self.billing_state,
            billing_country=self.billing_country,
            billing_postal_code=self.billing_postal_code,
            total=self.total,
        )
