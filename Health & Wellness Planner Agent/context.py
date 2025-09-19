# Health_Wellness_Agent/Context.py

class UserSessionContext:
    """Simple container for user session data."""

    def __init__(self, name="Guest", uid=1, diet_preferences=None, experience_level="beginner"):
        self.name = name
        self.uid = uid
        self.diet_preferences = diet_preferences
        self.experience_level = experience_level
        self.goal = None
        self.meal_plan = None
        self.workout_plan = None
        self.progress_logs = []

    def to_dict(self):
        return {
            "name": self.name,
            "uid": self.uid,
            "diet_preferences": self.diet_preferences,
            "experience_level": self.experience_level,
            "goal": self.goal,
            "meal_plan": self.meal_plan,
            "workout_plan": self.workout_plan,
            "progress_logs": self.progress_logs,
        }