from typing import Generic, Type, TypeVar, Optional
import random
import string

from sqlmodel import SQLModel, select, Session, func
from fastapi import HTTPException

from app.models import Shortlink


ModelType = TypeVar("ModelType", bound=SQLModel)


class CRUDBase(Generic[ModelType]):
    model: Type[ModelType]

    def __init__(self, session: Session, model: Type[ModelType] = None):
        self.session = session
        self.model = model or self.model
        assert self.model is not None, "model is required"

    def create(self, obj: ModelType) -> ModelType:
        self.session.add(obj)
        self.session.commit()
        self.session.refresh(obj)
        return obj


class CRUDShortlink(CRUDBase[Shortlink]):
    def __init__(self, session: Session):
        super().__init__(session, Shortlink)

    def generate_short(self, length: int = 6) -> str:
        chars = string.ascii_letters + string.digits
        return ''.join(random.choice(chars) for _ in range(length))

    def get_by_short(self, short: str) -> Optional[Shortlink]:
        return self.session.scalar(select(Shortlink).where(Shortlink.short == short))

    def get_by_long(self, long: str) -> Optional[Shortlink]:
        return self.session.scalar(select(Shortlink).where(Shortlink.long == long))

    def short_exists(self, short: str) -> bool:
        return self.session.scalar(select(func.count()).where(Shortlink.short == short)) > 0

    def create(self, long: str) -> Shortlink:
        item = self.get_by_long(long)
        if item:
            return item
        short = None
        for _ in range(3):
            short = self.generate_short()
            if not self.short_exists(short):
                break
        if not short:
            raise HTTPException(status_code=400, detail="Failed to generate short link")

        db_obj = Shortlink(long=long, short=short)
        super().create(db_obj)
        return db_obj
