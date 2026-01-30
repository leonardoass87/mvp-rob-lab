import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

class Intelligence:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_KEY")
        genai.configure(api_key=self.api_key)
        self.model = self._get_working_model()

    def _get_working_model(self):
        modelos = [m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods]
        return genai.GenerativeModel(model_name=modelos[0])

    def ask(self, prompt):
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            return f"Erro na IA: {e}"