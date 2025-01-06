from crewai import Task


# Define the Research Task
research_task = Task(
    description=(
        "You are part of {our_company} and are working on a meeting with {company}. Research about {our_company} to know"
        "more about what we do then conduct thorough research on {company}, their position in the sector, "
        "and recent industry trends. Focus on news from the last year, as the current "
        "year is 2024. Use accurate facts, numbers, and statistics about {company} to provide a detailed report.\n\n"
        "Take into account any information from prior interactions if there is any: {prior_interactions}\n\n"
        "Participants {participants}\n"
        "Meeting Context {context}"
    ),
    expected_output=(
        "A comprehensive report on {company}'s background, their status in the "
        "sector locally and globally, and relevant industry insights. Use accurate facts, numbers, and statistics."
        "about the {company}. Include a list of 10 bullet points highlighting the most crucial information for our"
        "meeting and a detailed report summarizing key findings about each participant {participants}."
    )
)

# Define the Product Alignment Task
product_alignment_task = Task(
    description=(
        "Analyze the current industry trends, challenges, and opportunities "
        "relevant to the meeting's context. Consider market reports, recent "
        "developments, and expert opinions to provide a comprehensive overview of the industry landscape."
        "Include any relevant, accurate and factual information, numbers, and statistics relevant to the meeting.\n\n"
        "Consider any insights from prior interactions, if any - {prior_interactions}\n\n"
        "Participants {participants}\n"
        "Meeting Context {context}"
    ),
    expected_output=(
        "An insightful and comprehensive industry analysis including statistical analysis that identifies major trends, potential "
        "challenges, and strategic opportunities."
    )
)

# Define the Sales Strategy Task
sales_strategy_task = Task(
    description=(
        "Develop a tailored sales approach for {company} as you are working for {our_company}. Consider their position in "
        "the sector both locally and globally, company size, and potential objections. Prepare extremely detailed strategies "
        "for handling these objections to be able to convince them and identify potential upselling or cross-selling"
        "opportunities. Use numbers, statistics, and factual information. Develop strategic talking points, questions, and discussion angles "
        "for the meeting based on the research and industry analysis conducted.\n\n"
        "Factor in any insights from, if any {prior_interactions}\n"
        "Meeting Context: {context}\n"
        "Meeting Objective: {objective}"
    ),
    expected_output=(
        "A comprehensive and detailed sales strategy document including facts, statitistics, talking points, approach, objection handling "
        "techniques, and additional sales opportunities tailored for the meeting with "
        "{company}."
    )
)

# Define the Meeting Preparation Task
meeting_preparation_task = Task(
    description=(
        "Compile all the research findings, industry analysis, and strategic "
        "talking points into a concise, comprehensive & detailed briefing document for "
        "the meeting with {company}. Use the relevant facts, numbers, and statistics to ensure the briefing is easy to"
        "digest and equips the meeting"
        "participants with all necessary information and strategies.\n\n"
        "Meeting Context {context}\n"
        "Meeting Objective {objective}\n"
        "Incorporate any relevant points from prior interactions, if any {prior_interactions}"
    ),
    expected_output=(
        "A comprehensive and detailed briefing document for the meeting with {company} that includes sections for meeting clients only info,"
        "who are {participants}, industry overview, talking points, and strategic recommendations. The document should be structured in a logical "
        "and engaging manner to facilitate a productive and insightful meeting."
    )
)
