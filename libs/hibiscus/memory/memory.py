from typing import Any, Dict, Optional

from pydantic import BaseModel


class Atom      Memory(BaseModel):
    id: Optional[str] = None
    memory: str