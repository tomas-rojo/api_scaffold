import uuid
from contextlib import AbstractContextManager

import sqlalchemy
from exceptions.item_not_found import ItemNotFound
from models.user import User
from ports.abstract_repository import AbstractRepository
from sqlalchemy import Boolean, String, text
from sqlalchemy.engine import Engine
from sqlalchemy.orm import DeclarativeBase, Mapped, Session, mapped_column, sessionmaker


class Base(DeclarativeBase):
    pass


class DbUser(Base):
    __tablename__ = "main_users"
    id: Mapped[uuid.UUID] = mapped_column(sqlalchemy.UUID(as_uuid=True), primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    is_active: Mapped[bool] = mapped_column(Boolean)


class SQLRepository(AbstractRepository):
    def __init__(self, engine: Engine):
        self._engine = engine
        self._sessionmaker = sessionmaker(engine)

    def create_schema(self) -> None:
        if self._engine.url.drivername != "sqlite":
            raise RuntimeError("create_schema() is only allowed for sqlite connections")
        Base.metadata.create_all(bind=self._engine)

    def drop_schema(self) -> None:
        if self._engine.url.drivername != "sqlite":
            raise RuntimeError("drop_schema() is only allowed for sqlite connections")
        Base.metadata.drop_all(bind=self._engine)

    @property
    def autocommit_session(self) -> AbstractContextManager[Session]:
        """Creates a managed context for an auto-committing database session."""
        return self._sessionmaker.begin()
    
    @property
    def no_autocommit_session(self) -> AbstractContextManager[Session]:
        return Session(self._engine)

    def add(self, user: User) -> None:
        with self.autocommit_session as session:
            db_user = DbUser(
                id=user.id,
                email=user.email,
                is_active=user.is_active
            )
            session.add(db_user)

    def get(self, user_id: str) -> User:
        with self.no_autocommit_session as session:
            user = session.get(DbUser, user_id)
            if not user:
                raise ValueError(f"User with ID: {user_id!r} not found")
            return user
