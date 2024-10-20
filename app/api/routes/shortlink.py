from fastapi import APIRouter, HTTPException

from app.api.deps import SessionDep
from app.models import ShortlinkPublic, ShortlinkCreate
from app.crud import CRUDShortlink
from app.core.config import settings

router = APIRouter()


@router.post("", response_model=ShortlinkPublic)
def generate_short(session: SessionDep, input: ShortlinkCreate) -> ShortlinkPublic:
    """
    根据长链接生成短链接
    """
    crud_shortlink = CRUDShortlink(session)
    return crud_shortlink.create(input.long).to_public()


@router.get("/long", response_model=ShortlinkPublic)
def get_long(session: SessionDep, short: str) -> ShortlinkPublic:
    """
    根据短链接查询长连接
    """
    crud_shortlink = CRUDShortlink(session)
    short = short.replace(settings.SHORT_URL_PREFIX, "").strip("/")
    instance = crud_shortlink.get_by_short(short)
    if not instance:
        raise HTTPException(status_code=404, detail="Short link not found")
    return instance.to_public()
