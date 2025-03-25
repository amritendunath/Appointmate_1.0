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

@tool
def check_availability_by_doctor(desired_date:DateModel, doctor_name:Literal['kevin anderson','robert martinez','susan davis','daniel miller','sarah wilson','michael green','lisa brown','jane smith','emily johnson','john doe']):
    """
    Checking the database if we have availability for the specific doctor.
    The parameters should be mentioned by the user in the query
    """
    #Dummy data
    df = pd.read_csv(f"availability.csv")
    df['date_slot_time'] = df['date_slot'].apply(lambda input: input.split(' ')[-1])
    rows = list(df[(df['date_slot'].apply(lambda input: input.split(' ')[0]) == desired_date.date)&(df['doctor_name'] == doctor_name)&(df['is_available'] == True)]['date_slot_time'])

    if len(rows) == 0:
        output = "No availability in the entire day"
    else:
        output = f'This availability for {desired_date.date}\n'
        output += "Available slots: " + ', '.join(rows)

    return output