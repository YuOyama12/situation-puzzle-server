from typing import Optional

from pydantic import BaseModel


class ResultResponse(BaseModel):
    code: int
    message: Optional[str]
