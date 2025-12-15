import re
from skills.skills_list import SKILL_KEYWORDS

def extract_skills(text: str):
    if not text:
        return {}

    text = text.lower()
    extracted = {}

    for category, skills in SKILL_KEYWORDS.items():
        found = set()
        for skill in skills:
            pattern = r"\b" + re.escape(skill) + r"\b"
            if re.search(pattern, text):
                found.add(skill)
        if found:
            extracted[category] = sorted(found)

    return extracted
