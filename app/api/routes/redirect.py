from fastapi.responses import RedirectResponse

from fastapi import APIRouter, HTTPException

from app.api.deps import SessionDep
from app.crud import CRUDShortlink


router = APIRouter()


@router.get("/{short}", response_class=RedirectResponse, status_code=302)
async def redirect(session: SessionDep, short: str):
    crud_shortlink = CRUDShortlink(session)
    instance = crud_shortlink.get_by_short(short)
    if not instance:
        raise HTTPException(status_code=404, detail="Short link not found")
    return RedirectResponse(instance.long)
