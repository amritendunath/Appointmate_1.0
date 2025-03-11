from models.tools import DateModel, DateTimeModel, IdentificationNumberModel
from langchain_core.pydantic_v1 import constr, BaseModel, Field, validator
from typing import Optional

# Primary Assistant
class ToPrimaryBookingAssistant(BaseModel):
    """Transfers work to a specialized assistant to handle flight updates and cancellations."""

    request: str = Field(
        description="Any necessary followup questions the update flight assistant should clarify before proceeding."
    )
