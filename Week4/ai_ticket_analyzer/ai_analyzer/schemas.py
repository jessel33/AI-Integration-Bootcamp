# schemas.py
# This file will be used to define and eventualy validate
# the AI's output structure.
#

from typing import Literal

from pydantic import BaseModel


class TicketAnalysis(BaseModel):
    category: Literal["mechanical", "electrical", "software", "other"]
    priority: Literal["low", "medium", "high", "critical"]
    summary: str
