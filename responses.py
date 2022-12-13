from datetime import datetime

def sample_responses (text):
    msg = str (text).lower()

    if msg in ("hello", "hi", "sup", "what's up?", "good day"):
        return "Hey, how is it going?"

    if msg in ("who are you?", "who you be?", "what is your purpose?", "who are you", "what is your deal?"):
        return "I am a bot. My creator named me Vikano..."

    if msg in ("time", "what is the time"):
        nowx = datetime.now()
        the_time = nowx.strftime ("%Y/%m/%d, %H:%m:%S")
        return str (the_time)
        
    else:
        return "I am currently not configured to answer your request. Reach out to my maker - @Iamanosike - for more info."