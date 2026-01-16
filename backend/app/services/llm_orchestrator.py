
import os
import openai
import google.generativeai as genai
from typing import Literal

class LLMOrchestrator:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        self.gemini_api_key = os.getenv("GEMINI_API_KEY")
        
        if self.gemini_api_key:
            genai.configure(api_key=self.gemini_api_key)

    def execute_query(self, query: str, context: str = "", provider: Literal["openai", "gemini"] = "openai") -> str:
        prompt = f"Context: {context}\n\nQuestion: {query}\n\nAnswer:"
        
        if provider == "openai" and self.openai_api_key:
            client = openai.OpenAI(api_key=self.openai_api_key)
            response = client.chat.completions.create(
                model="gpt-4o",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
            
        elif provider == "gemini" and self.gemini_api_key:
            model = genai.GenerativeModel('gemini-pro')
            response = model.generate_content(prompt)
            return response.text
            
        return "LLM Provider not configured or API Key missing."

llm_orchestrator = LLMOrchestrator()
