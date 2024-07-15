# ------------Project Imports 
from app.config import Settings
from utils.consts import *
# ------------Lib Imports 
from datetime import datetime, date
import re


# ----------------------------------------------------------------------------------- #
# ------------------------------------ DATE TIME ------------------------------------ #
# ----------------------------------------------------------------------------------- #

def datetime_without_milliseconds(string):
    return bool(re.match(DB_DATETIME_FORMAT_REG, string))

def datetime_with_milliseconds(string):
    return bool(re.match(DB_F_DATETIME_FORMAT_REG, string))

def datetime_response_format(string):
    return bool(re.match(RESPONSE_DATE_FORMAT_REG, string))

# -----date time as input
def dateToFormatedDate(date ):
    stringDate= datetime.strftime(date, RESPONSE_DATE_FORMAT)  
    return datetime.strptime(stringDate, RESPONSE_DATE_FORMAT)  

def dateToFormatedStr(date ):
    return datetime.strftime(date, RESPONSE_DATE_FORMAT)  

# -----string as input, string having issues with date time, so managed separately 
def strToDateTime(stringDate: str):
    try:
        if datetime_without_milliseconds(stringDate):
            stringDate=  datetime.strptime(stringDate, DB_DATETIME_FORMAT)  
        elif datetime_with_milliseconds(stringDate):
            stringDate= datetime.strptime(stringDate, DB_F_DATETIME_FORMAT)  
        elif datetime_response_format(stringDate):
            stringDate= datetime.strptime(stringDate, RESPONSE_DATE_FORMAT)  
        else:
            print("Unknow format")
        return stringDate
    except Exception as ex:
        raise ("Unknown Format for this sting "+ stringDate)
    
def strToFormatedStr(stringDate):
    if isinstance(stringDate, str):
        stringDate = strToDateTime(stringDate = stringDate)
    return datetime.strftime(stringDate, RESPONSE_DATE_FORMAT)  

def strToFormatedDate(stringDate : str):
    date= strToDateTime(stringDate = stringDate)     
    return dateToFormatedDate(date = date)     


def parseDBDateTime(value):
    try: 
        if value:
            if isinstance(value, str):
                return dateToFormatedStr(strToDateTime(stringDate = value))
            elif isinstance(value, date):
                return dateToFormatedStr(value)
    except Exception as msg:
        raise (str(msg))
    return value

# ----------------------------------------------------------------------------------- #
# ------------------------------------ OTHERS --------------------------------------- #
# ----------------------------------------------------------------------------------- #
 