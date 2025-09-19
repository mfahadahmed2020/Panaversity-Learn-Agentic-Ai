class HealthWellnessAgent:
    def __init__(self):
        self.name = "Health & Wellness AI"

    def get_advice(self, query: str) -> str:
        if not query:
            return "⚠️ Please enter a health-related question."
        return f"💡 Health tip for '{query}': stay hydrated, exercise regularly, and get enough rest!"