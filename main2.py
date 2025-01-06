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
import time
import base64

# Load environment variables
load_dotenv()

st.set_page_config(page_title="AI-Powered Meeting Hub", page_icon="📊", layout="wide")

# Function to generate download link
def generate_download_link(content, filename, file_type):
    b64 = base64.b64encode(content.encode()).decode()
    return f'<a href="data:file/{file_type};base64,{b64}" download="{filename}">Download {filename}</a>'

# Set up Streamlit Layout
st.title("AI-Powered Client Meeting Preparation Hub")

# Add spacing and style to Meeting Details
st.markdown("## 📋 **Meeting Details**", unsafe_allow_html=True)

# Collect User Inputs with Columns
col1, col2 = st.columns(2)

with col1:
    your_company = st.text_input("🏢 Your Company", placeholder="Enter your company name")
    company_name = st.text_input("🏢 Company Name", placeholder="Enter the client's company name")

with col2:
    participants = st.text_area("👥 Clients (Names or Emails)", 
                                placeholder="Enter Clients' names or emails, separated by commas")
    meeting_context = st.text_area("📝 Meeting Context", 
                                   placeholder="Describe the purpose or context of the meeting")

# Full-width Input
meeting_objective = st.text_area("🎯 Meeting Objective", placeholder="What do you aim to achieve in the meeting?")
prior_interactions = st.text_area("🔄 Prior Interactions", placeholder="Provide any details from previous meetings. Type none if no interaction")

# Run the Crew Workflow
if st.button("🚀 Run Meeting Preparation"):
    if not (your_company and company_name and participants and meeting_context and meeting_objective):
        st.error("❗ Please provide all required fields: Company Name, Participants, Context, and Objective.")
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
            process=Process.sequential,
            cache = False,
            verbose=False
        )

        # Execute the crew workflow
        start_time = time.time()
        try:
            result = crew.kickoff(inputs={
                "our_company": your_company,
                "company": company_name,
                "participants": participants,
                "context": meeting_context,
                "prior_interactions": prior_interactions,
                "objective": meeting_objective,
            })
            end_time = time.time()

            st.success("✅ Meeting Preparation Complete!")
            st.info(f"⏱️ Execution Time: {end_time - start_time:.2f} seconds")

            # Display Results
            result_str = str(result)  # Ensure result is a string
            st.subheader("📝 Meeting Preparation Results")
            st.markdown(result_str, unsafe_allow_html=True)

            # Add Download Button
            st.markdown("### 💾 Download Results")
            download_link = generate_download_link(result_str, "meeting_preparation.md", "markdown")
            st.markdown(download_link, unsafe_allow_html=True)

        except Exception as e:
            st.error(f"❗ An error occurred during the workflow execution: {str(e)}")