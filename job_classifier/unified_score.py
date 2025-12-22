def calculate_unified_score(
    skill_score: float,
    experience_score: float,
    llm_score: float
) -> float:
    """
    Combines skill match, experience similarity, and LLM reasoning
    into a unified candidate score.
    """

    final_score = (
        (skill_score * 0.4) +
        (experience_score * 0.4) +
        (llm_score * 0.2)
    )

    return round(final_score, 2)
