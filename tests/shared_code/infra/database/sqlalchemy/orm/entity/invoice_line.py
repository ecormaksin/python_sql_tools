from sqlalchemy import DECIMAL, ForeignKey, Index, Integer
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class InvoiceLine(Base):
    __tablename__ = "invoice_line"

    invoice_line_id: Mapped[int] = mapped_column(primary_key=True)
    invoice_id = mapped_column(ForeignKey("invoice.invoice_id"))
    track_id = mapped_column(ForeignKey("track.track_id"))
    unit_price: Mapped[float] = mapped_column(DECIMAL(9, 2))
    quantity: Mapped[int] = mapped_column(Integer)

    __table_args__ = (
        Index("invoice_line_IX1", "invoice_id"),
        Index("invoice_line_IX2", "track_id"),
    )

    def __repr__(self) -> str:
        return (
            "InvoiceLine("
            "invoice_line_id={invoice_line_id!r}, "
            "invoice_id={invoice_id!r}, "
            "track_id={track_id!r}, "
            "unit_price={unit_price!r}, "
            "quantity={quantity!r}"
            ")"
        ).format(
            invoice_line_id=self.invoice_line_id,
            invoice_id=self.invoice_id,
            track_id=self.track_id,
            unit_price=self.unit_price,
            quantity=self.quantity,
        )
