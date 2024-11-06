import uuid
from contextlib import AbstractContextManager

import sqlalchemy
import sqlalchemy.exc
from exceptions.user_email_already_exists import EmailAlreadyExists
from exceptions.user_not_found import UserNotFound
from models.user import User
from ports.abstract_repository import AbstractRepository
from sqlalchemy import Boolean, String
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
        if self._engine.dialect.name != "sqlite":
            raise RuntimeError("create_schema() is only allowed for sqlite connections")
        Base.metadata.create_all(bind=self._engine)

    def drop_schema(self) -> None:
        if self._engine.dialect.name != "sqlite":
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
        try:
            with self.autocommit_session as session:
                db_user = DbUser(id=user.id, email=user.email, is_active=user.is_active)
                session.add(db_user)
        except sqlalchemy.exc.IntegrityError as e:
            if "email" in str(e.orig):
                raise EmailAlreadyExists(user.email) from None
            raise Exception  # raise broad exception on purpose

    def _get(self, user_id: uuid.UUID) -> User:
        with self.no_autocommit_session as session:
            user = session.get(DbUser, user_id)
            if not user:
                raise UserNotFound(user_id.hex) from None
            return User(email=user.email, is_active=user.is_active, id=user.id)

    def _remove(self, user_id: uuid.UUID) -> None:
        with self.autocommit_session as session:
            user = session.get(DbUser, user_id)  # Fetch the DbUser instance
            if user is None:
                raise UserNotFound(f"User with ID {user_id} not found")
            session.delete(user)

    def update(self, user: User) -> None:
        try:
            with self.autocommit_session as session:
                _user = session.get(DbUser, user.id)
                if not _user:
                    raise UserNotFound(f"User with ID {user.id} not found")
                _user.email = user.email
                _user.is_active = user.is_active
        except sqlalchemy.exc.IntegrityError as e:
            if "email" in str(e.orig):
                raise EmailAlreadyExists(user.email) from None
