import streamlit as st
from PIL import Image
from datetime import datetime, timedelta
import pytz

RESET_HOUR = st.secrets["constants"]["reset_hour"]
UTC_TIMEZONE = pytz.utc

# Get today's object
def get_today_object():
    today = datetime.now(UTC_TIMEZONE)
    day_of_year = today.timetuple().tm_yday
    return st.secrets["constants"]["objects"][day_of_year % len(st.secrets["constants"]["objects"])]

# Function to calculate time remaining until the next reset
def time_until_reset():
    now = datetime.now(UTC_TIMEZONE)
    reset_time = now.replace(hour=RESET_HOUR, minute=0, second=0, microsecond=0)

    if now >= reset_time:
        reset_time += timedelta(days=1)
    
    time_remaining = reset_time - now
    return time_remaining

def format_time_remaining(time_remaining):
    days, remainder = divmod(time_remaining.total_seconds(), 86400)
    hours, remainder = divmod(remainder, 3600)
    minutes, seconds = divmod(remainder, 60)
    return f"**{int(hours)} hours, {int(minutes)} minutes**"
