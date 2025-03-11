from models.tools import DateModel, DateTimeModel, IdentificationNumberModel
from langchain_core.pydantic_v1 import constr, BaseModel, Field, validator
from typing import Optional

# Primary Assistant
class ToPrimaryBookingAssistant(BaseModel):
    """Transfers work to a specialized assistant to handle flight updates and cancellations."""

    request: str = Field(
        description="Any necessary followup questions the update flight assistant should clarify before proceeding."
    )

class ToGetInfo(BaseModel):
    """Get information of doctor availability via name or specialization"""

    desired_date: DateModel = Field(
        description="The desired date for booking"
    )
    specialization: Optional[str] = Field(
        default=None, description="The desired specialization of the doctor"
    )
    doctor_name: Optional[str] = Field(
        default=None, description="The desired doctor name for booking"
    )
    request: str = Field(
        description="Any additional information or requests from the user regarding the appointment."
    )