from datetime import date
from typing import Optional

from sqlalchemy import Date, ForeignKey, Index, String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Employee(Base):
    __tablename__ = "employee"

    employee_id: Mapped[int] = mapped_column(primary_key=True)
    last_name: Mapped[str] = mapped_column(String(40))
    first_name: Mapped[str] = mapped_column(String(40))
    title: Mapped[Optional[str]] = mapped_column(String(30))
    reports_to = mapped_column(ForeignKey("employee.employee_id"), nullable=True)
    birth_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    hire_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    address: Mapped[Optional[str]] = mapped_column(String(70))
    city: Mapped[Optional[str]] = mapped_column(String(40))
    state: Mapped[Optional[str]] = mapped_column(String(40))
    country: Mapped[Optional[str]] = mapped_column(String(40))
    postal_code: Mapped[Optional[str]] = mapped_column(String(10))
    phone: Mapped[Optional[str]] = mapped_column(String(24))
    fax: Mapped[Optional[str]] = mapped_column(String(24))
    email: Mapped[str] = mapped_column(String(320))

    __table_args__ = (
        Index("employee_IX1", "last_name"),
        Index("employee_IX2", "first_name"),
        Index("employee_IX3", "email"),
        Index("employee_IX4", "reports_to"),
    )

    def __repr__(self) -> str:
        return (
            "Employee("
            "employee_id={employee_id!r}, "
            "last_name={last_name!r}, "
            "first_name={first_name!r}, "
            "title={title!r}, "
            "reports_to={reports_to!r}, "
            "birth_date={birth_date!r}, "
            "hire_date={hire_date!r}, "
            "address={address!r}, "
            "city={city!r}, "
            "state={state!r}, "
            "country={country!r}, "
            "postal_code={postal_code!r}, "
            "phone={phone!r}, "
            "fax={fax!r}, "
            "email={email!r}"
            ")"
        ).format(
            employee_id=self.employee_id,
            last_name=self.last_name,
            first_name=self.first_name,
            title=self.title,
            reports_to=self.reports_to,
            birth_date=self.birth_date,
            hire_date=self.hire_date,
            address=self.address,
            city=self.city,
            state=self.state,
            country=self.country,
            postal_code=self.postal_code,
            phone=self.phone,
            fax=self.fax,
            email=self.email,
        )
