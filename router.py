import re

from langsmith import traceable


AGRICULTURE_KEYWORDS = {

    "crop",
    "soil",
    "fertilizer",
    "irrigation",
    "pesticide",
    "farming",
    "agriculture",
    "seed",
    "harvest",
    "farmer",
    "disease",
    "plant",
    "cultivation",
    "weather",
    "yield",
    "rice",
    "wheat",
    "cotton",
    "tomato",
    "maize",

    # CALENDAR KEYWORDS
    "calendar",
    "season",
    "kharif",
    "rabi",
    "sowing",
    "harvesting",
    "schedule",
    "month",
    "january",
    "february",
    "march",
    "april",
    "may",
    "june",
    "july",
    "august",
    "september",
    "october",
    "november",
    "december"
}


PROBLEM_KEYWORDS = {

    "yellow leaves",
    "leaf spots",
    "low yield",
    "crop damage",
    "plant dying",
    "fungus",
    "pest attack",
    "wilting",
    "soil problem",
    "water problem",
    "disease"
}


# ---------------------------------------------------------
# QUERY CLASSIFICATION
# ---------------------------------------------------------

@traceable(name="Query Classification", run_type="chain")
def classify_query(query: str) -> str:

    q = query.lower().strip()

    if any(word in q for word in PROBLEM_KEYWORDS):
        return "PROBLEM"

    if any(word in q for word in AGRICULTURE_KEYWORDS):
        return "AGRICULTURE"

    return "GENERAL"