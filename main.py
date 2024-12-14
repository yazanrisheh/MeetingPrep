import streamlit as st
from dotenv import load_dotenv
from crewai import Crew, Process
from tasks import (
    research_task,
    product_alignment_task,
    sales_strategy_task,
    meeting_preparation_task,
)
from agents import (
    lead_researcher_agent,
    product_specialist_agent,
    sales_strategist_agent,
    briefing_coordinator_agent,
)

# Load environment variables
load_dotenv()

# Streamlit App Title
st.title("Meeting Preparation Crew")

# Collect User Inputs
st.header("Meeting Details")
company = st.text_input("Company Name", placeholder="Enter the company name")
participants = st.text_area(
    "Participants (Names or Emails)",
    placeholder="Enter participants' full names or emails, separated by commas"
)
context = st.text_area(
    "Meeting Context",
    placeholder="Describe the purpose or context of the meeting"
)
prior_interactions = st.text_area(
    "Prior Interactions",
    placeholder="Provide any details from previous meetings"
)
objective = st.text_area(
    "Meeting Objective",
    placeholder="What do you aim to achieve?"
)

# Run the Crew Workflow
if st.button("Run Meeting Preparation"):
    # Ensure all required inputs are provided
    if not (company and participants and context and objective):
        st.error("Please provide all required fields: Company, Participants, Context, and Objective.")
    else:
        # Assign agents to tasks
        research_task.agent = lead_researcher_agent
        product_alignment_task.agent = product_specialist_agent
        sales_strategy_task.agent = sales_strategist_agent
        meeting_preparation_task.agent = briefing_coordinator_agent

        # Create the Crew
        crew = Crew(
            agents=[
                lead_researcher_agent,
                product_specialist_agent,
                sales_strategist_agent,
                briefing_coordinator_agent,
            ],
            tasks=[
                research_task,
                product_alignment_task,
                sales_strategy_task,
                meeting_preparation_task,
            ],
            process=Process.sequential  # Execute tasks sequentially
        )

        # Execute the workflow
        inputs = {
            "company": company,
            "participants": participants,
            "context": context,
            "prior_interactions": prior_interactions,
            "objective": objective,
        }

        st.info("Running the meeting preparation crew. This might take a while...")

        try:
            # Execute the crew workflow
            result = crew.kickoff(inputs=inputs)

            st.success("Meeting Preparation Complete!")
            st.subheader("Meeting Preparation Results")

            # Display results as markdown
            st.markdown(result, unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred during the workflow execution: {str(e)}")
