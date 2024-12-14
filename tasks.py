from crewai import Task


# Define the Research Task
research_task = Task(
    description=(
        "Conduct thorough research on {company}, their position in the sector, "
        "and recent industry trends. Focus on news from the last year, as the current "
        "year is 2024.\n\n"
        "Take into account any information from prior interactions: {prior_interactions}\n\n"
        "Participants {participants}\n"
        "Meeting Context {context}"
    ),
    expected_output=(
        "A comprehensive report on {company}'s background, their status in the "
        "sector, and relevant industry insights. Include a list of 10 bullet points "
        "highlighting the most crucial information for our meeting and a detailed report "
        "summarizing key findings about each participant."
    )
)

# Define the Product Alignment Task
product_alignment_task = Task(
    description=(
        "Analyze the current industry trends, challenges, and opportunities "
        "relevant to the meeting's context. Consider market reports, recent "
        "developments, and expert opinions to provide a comprehensive overview of the industry landscape.\n\n"
        "Consider any insights from prior interactions - {prior_interactions}\n\n"
        "Participants {participants}\n"
        "Meeting Context {context}"
    ),
    expected_output=(
        "An insightful analysis that identifies major trends, potential "
        "challenges, and strategic opportunities."
    )
)

# Define the Sales Strategy Task
sales_strategy_task = Task(
    description=(
        "Develop a tailored sales approach for {company}. Consider their position in "
        "the sector, company size, and potential objections. Prepare strategies "
        "for handling these objections and identify potential upselling or cross-selling "
        "opportunities. Develop strategic talking points, questions, and discussion angles "
        "for the meeting based on the research and industry analysis conducted.\n\n"
        "Factor in any insights from {prior_interactions}\n"
        "Meeting Context: {context}\n"
        "Meeting Objective: {objective}"
    ),
    expected_output=(
        "A comprehensive sales strategy document including approach, objection handling "
        "techniques, and additional sales opportunities tailored for the meeting with "
        "{company}."
    )
)

# Define the Meeting Preparation Task
meeting_preparation_task = Task(
    description=(
        "Compile all the research findings, industry analysis, and strategic "
        "talking points into a concise, comprehensive briefing document for "
        "the meeting with {company}. Ensure the briefing is easy to digest and equips the meeting "
        "participants with all necessary information and strategies.\n\n"
        "Meeting Context {context}\n"
        "Meeting Objective {objective}\n"
        "Incorporate any relevant points from prior interactions {prior_interactions}"
    ),
    expected_output=(
        "A comprehensive briefing document for the meeting with {company} that includes sections for meeting participant-only bios, "
        "industry overview, talking points, and strategic recommendations. The document should be structured in a logical "
        "and engaging manner to facilitate a productive and insightful meeting."
    )
)
