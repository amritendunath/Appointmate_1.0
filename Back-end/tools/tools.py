from models.tools import DateModel, DateTimeModel, IdentificationNumberModel
from typing import  Literal
from langchain_core.tools import tool
import pandas as pd
from datetime import datetime


def convert_datetime_format(dt_str):
    # Parse the input datetime string
    dt = datetime.strptime(dt_str, "%Y-%m-%d %H:%M")
    
    # Format the output as 'DD-MM-YYYY H.M' (removing leading zero from hour only)
    return dt.strftime("%d-%m-%Y %#H.%M")