import uuid
from contextlib import AbstractContextManager

import sqlalchemy
from exceptions.item_not_found import ItemNotFound
from ports.abstract_repository import AbstractRepository
from sqlalchemy import String, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker


class Base(DeclarativeBase):
    pass


class DbUser(Base):
    __tablename__ = "main_users"
    id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID(as_uuid=True), primary_key=True)
    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(255), unique=True)


class SQLRepository(AbstractRepository):
    def __init__(self, engine: Engine):
        self._engine = engine
        self._sessionmaker = sessionmaker(engine)

    @property
    def autocommit_session(self) -> AbstractContextManager[Session]:
        """Creates a managed context for an auto-committing database session."""
        return self._sessionmaker.begin()

    def add(self, id: str) -> None:
        with self.autocommit_session as session:
            session.add(id)

    def get(self, id: str) -> str:
        with Session(self._engine) as session:
            result = session.execute(text("SELECT 1"))
            element = result.first()
        if element is None:
            raise ItemNotFound(id) from None
        return str(element[0])
