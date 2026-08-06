import re


def parse_task(description: str):
    text = description
    lower = description.lower()

    # Priority
    if "urgent" in lower or "asap" in lower:
        priority = "high"
    elif "whenever" in lower or "low priority" in lower:
        priority = "low"
    else:
        priority = "medium"

    # Due date
    due_date = None

    date_phrases = [
        "today",
        "tomorrow",
        "next week",
        "next monday",
        "next tuesday",
        "next wednesday",
        "next thursday",
        "next friday",
        "next saturday",
        "next sunday",
        "monday",
        "tuesday",
        "wednesday",
        "thursday",
        "friday",
        "saturday",
        "sunday"
    ]

    for phrase in date_phrases:
        if phrase in lower:
            due_date = phrase
            text = re.sub(phrase, "", text, flags=re.IGNORECASE)
            break

    # Remove priority keywords
    for word in ["urgent", "asap", "whenever", "low priority"]:
        text = re.sub(word, "", text, flags=re.IGNORECASE)

    title = text.strip()

    if title == "":
        title = "Untitled task"

    return {
        "title": title,
        "priority": priority,
        "due_date_hint": due_date
    }