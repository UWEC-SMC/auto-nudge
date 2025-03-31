from typing import Optional

from pydantic import BaseModel, Field

class AutoNudgeCache(BaseModel):
    last_update_hash: Optional[str] = Field(
        "",
        description="",
    )