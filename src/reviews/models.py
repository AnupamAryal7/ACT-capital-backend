from sqlmodel import SQLModel, Column, Field
from datetime import datetime
import sqlalchemy.dialects.postgresql as pg
import uuid

class Review(SQLModel, Table=True):
    __tablename__ = "reviews"

    uid:uuid.UUID = Field(
        sa_column=Column(
            pg.UUID,
            primary_key=True,
            unique=True,
            nullable=False
        )
    )
    auther: str
    created_at: datetime = Field(
        sa_column= Column(
            pg.TIMESTAMP,
            default=datetime.now
        )
    )