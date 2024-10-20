from sqlmodel import SQLModel, Field
from typing import Optional
from datetime import datetime
from app.core.config import settings


class ShortlinkBase(SQLModel):
    long: str = Field(max_length=2048)
    short: str = Field(max_length=10)


class Shortlink(ShortlinkBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    created_at: datetime = Field(default_factory=datetime.now)

    def get_complete_short_url(self) -> str:
        return f"{settings.SHORT_URL_PREFIX}/{self.short}"

    def to_public(self) -> "ShortlinkPublic":
        return ShortlinkPublic(long=self.long, short=self.get_complete_short_url())


class ShortlinkCreate(SQLModel):
    long: str = Field(max_length=2048)


class ShortlinkPublic(ShortlinkBase):
    short: str = Field(max_length=30)
