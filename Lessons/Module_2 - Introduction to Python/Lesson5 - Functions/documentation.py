# Write a DocString

def readable_timedelta(days):
    # insert your docstring here
    """Calculate number of weeks and days when given number of days.
    
    Args:
    days (int): number of days to be converted to weeks
    
    Returns:
    a string 
    """
    weeks = days // 7
    remainder = days % 7
    return "{} week(s) and {} day(s).".format(weeks, remainder)