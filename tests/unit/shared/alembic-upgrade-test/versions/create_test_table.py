from typing import Sequence, Union

revision: str = '12345678abcd'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    raise NotImplementedError("To prove that upgrade() is called")


def downgrade() -> None:
    raise NotImplementedError("Downgrade is not supported")
