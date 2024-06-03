"""update table names v10

Revision ID: d6b56534fda4
Revises: 881e0c8b3c8e
Create Date: 2024-01-22 23:02:38.690976

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = "d6b56534fda4"
down_revision: Union[str, None] = "881e0c8b3c8e"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "assessments",
        sa.Column("verified_reference_context", sa.String(), nullable=True),
    )
    op.add_column(
        "assessments", sa.Column("chunks_retrieved", sa.JSON(), nullable=True)
    )
    op.add_column(
        "assessments", sa.Column("min_retrieval_score", sa.Float(), nullable=True)
    )
    op.add_column(
        "assessments", sa.Column("max_retrieval_score", sa.Float(), nullable=True)
    )
    op.add_column(
        "assessments", sa.Column("avg_retrieval_score", sa.Float(), nullable=True)
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column("assessments", "avg_retrieval_score")
    op.drop_column("assessments", "max_retrieval_score")
    op.drop_column("assessments", "min_retrieval_score")
    op.drop_column("assessments", "chunks_retrieved")
    op.drop_column("assessments", "verified_reference_context")
    # ### end Alembic commands ###