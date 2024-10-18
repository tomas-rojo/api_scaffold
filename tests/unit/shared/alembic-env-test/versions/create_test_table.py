from typing import Sequence, Union

from alembic import op

revision: str = '5f42e864e30a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.execute("CREATE TABLE test (id INTEGER NOT NULL)")


def downgrade() -> None:
    raise NotImplementedError("Downgrade is not supported")
