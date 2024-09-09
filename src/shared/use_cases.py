from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
import logging
from typing import Any, Generic, TypeVar

TUseCaseResult = TypeVar("TUseCaseResult")
"""The data type that is returned by an executed use case."""


@dataclass
class AbstractUseCase(ABC, Generic[TUseCaseResult]):
    _executed: bool = field(default=False, init=False)

    def __post_init__(self):
        self.log = logging.getLogger(__class__.__name__)

    def execute(self) -> TUseCaseResult:
        if self._executed:
            raise RuntimeError("Use cases can be executed only once")
        self._executed = True

        try:
            return self._execute()
        except UseCaseException as e:
            self.log.error(
                f"Use case exception occurred: [{e.__class__.__name__}] {e.message} (error code: {e.error_code})"
            )
            raise e
        except Exception as e:
            self.log.warning(f"Unhandled exception in use case: [{e.__class__.__name__}] {e}")
            raise UnhandledException(e=e) from e

    @abstractmethod
    def _execute(self) -> TUseCaseResult:
        """Must be implemented by derived use case classes, to perform the
        operations for the use case flow.

        When the use case flow runs into an error, an exception of type
        `UseCaseException` must be raised."""
        raise NotImplementedError


@dataclass
class CommandUseCase(AbstractUseCase[None], ABC):
    """A base class for implementing CQRS-style command use cases.
    These are use cases that change something in the system, and that will not
    return any data."""

    pass


@dataclass
class QueryUseCase(AbstractUseCase[TUseCaseResult], ABC):
    """A base class for implementing CQRS-style query use cases.
    These are use cases that do not change anything in the system, and that will
    gather and return data to the caller.
    """

    pass


class UseCaseException(Exception):
    """Must be implemented by exceptions that are raised from use case implementations.

    The `message_fmt` field is used to define the format of the error message to use.
    Its value can contain `{label}` references, which are used for formatting based
    on the named input parameters of the constructor.
    .
    The use case can suggest an error code to be used by HTTP API code as the HTTP
    request status code through the `error_code` field."""

    error_code: int
    message_fmt: str | None = None

    def __init__(self, **kwargs: Any) -> None:
        try:
            self.message = (
                self.message_fmt.format(**kwargs)
                if self.message_fmt
                else f"Data: {', '.join(k + '=' + str(v) for (k, v) in kwargs.items())}"
            )
        except KeyError as e:
            raise ValueError(f"Missing parameter {e} for {self.__class__.__name__!r}") from None

        if not (200 <= self.error_code <= 599):
            raise ValueError("Invalid error code (expected 200-599)") from None

    def __str__(self) -> str:
        return self.message


class UnhandledException(UseCaseException):
    error_code = 500
    message_fmt = "Error: [{e.__class__.__name__}] {e}"
