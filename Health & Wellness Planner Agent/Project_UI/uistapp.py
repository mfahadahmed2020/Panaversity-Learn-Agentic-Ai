import streamlit as st
import asyncio
from pprint import pformat

from health_wellness_agent.agent import HealthWellnessAgent
from health_wellness_agent.context import UserSessionContext

# Setup Streamlit page
st.set_page_config(
    page_title="Health & Wellness Planner",
    layout="wide",
    page_icon="💪"
)

st.title("💪 Health & Wellness Planner Agent")

# Initialize session state
if "user_ctx" not in st.session_state:
    st.session_state.user_ctx = {
        "name": "Guest",
        "uid": 1,
        "diet_preferences": None,
        "experience_level": "beginner",
        "goal": None,
        "meal_plan": None,
        "workout_plan": None,
        "progress_logs": [],
    }
if "agent" not in st.session_state:
    st.session_state.agent = HealthWellnessAgent()

# Sidebar config
st.sidebar.header("⚙️ Preferences")
st.session_state.user_ctx["name"] = st.sidebar.text_input("Your name", "Kamran")
st.session_state.user_ctx["diet_preferences"] = st.sidebar.selectbox(
    "Diet preference", ["vegetarian", "vegan", "omnivore"]
)
st.session_state.user_ctx["experience_level"] = st.sidebar.radio(
    "Experience level", ["beginner", "intermediate", "advanced"]
)

# Goal input
st.subheader("🎯 Set Your Goal")
goal_text = st.text_input("Enter your fitness/health goal:", "I want to lose 5kg in 2 months")

if st.button("Generate Plan"):
    async def run_agent():
        return await st.session_state.agent.handle_user(goal_text, st.session_state.user_ctx)

    result = asyncio.run(run_agent())

    if "handoff" in result:
        st.warning(f"Handoff triggered: {result['handoff']}")
        st.write(result["handoff_resp"]["message"])
    else:
        st.success("✅ Plan generated successfully!")

        # Display results
        with st.expander("📋 Goal Analysis", expanded=True):
            st.json(result["goal_analysis"])

        with st.expander("🥗 Meal Plan (7 days)", expanded=False):
            for day in result["meal_plan"]:
                st.markdown(f"**{day['day']}**")
                for meal in day["meals"]:
                    st.write(f"- {meal['meal']}: {meal['menu']}")

        with st.expander("🏋️ Workout Plan", expanded=False):
            for w in result["workout_plan"]["workouts"]:
                st.write(f"{w['day']}: {w['type']} ({w['duration_mins']} mins)")

        with st.expander("⏰ Next Check-in", expanded=False):
            st.json(result["next_checkin"])

# Progress update section
st.subheader("📈 Track Progress")
update_weight = st.text_input("Weight update (kg)", "")
update_notes = st.text_area("Notes", "")

if st.button("Save Progress Update"):
    update_data = {}
    if update_weight:
        update_data["weight"] = update_weight
    if update_notes:
        update_data["notes"] = update_notes

    async def run_update():
        return await st.session_state.agent.accept_update(st.session_state.user_ctx, update_data)

    upd = asyncio.run(run_update())
    st.success("Progress updated!")
    st.json(upd)

# Show context (for debugging / transparency)
with st.expander("🔍 Session Context (Debug)", expanded=False):
    st.text(pformat(st.session_state.user_ctx))
