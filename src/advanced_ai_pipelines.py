import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("COMET_API_KEY")
base_url = os.getenv("COMET_API_BASE")

client = OpenAI(
    api_key=api_key,
    base_url=base_url
)

MODEL = "gpt-4o"

class MockNLPSystem:
    def extract_entities(self, text):
        print(f"[NLP] Extracting entities from: '{text[:30]}...'")
        try:
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": "Extract the key entities (inventors, companies, technologies) from the text. Return as a comma-separated list."},
                    {"role": "user", "content": text}
                ]
            )
            entities = response.choices[0].message.content.split(',')
            return {"entities": [e.strip() for e in entities]}
        except Exception as e:
            print(f"API Error: {e}")
            return {"entities": ["Error parsing entities"]}
        
    def analyze_sentiment(self, text):
        print(f"[NLP] Analyzing legal sentiment...")
        return {"sentiment": "Neutral/Objective", "confidence": 0.95}

class MockSLMSystem:
    def summarize(self, text):
        print(f"[SLM] Summarizing complex legal text...")
        return "Summary: This document outlines a patent filing based on user requirements."
        
    def generate_concise_response(self, query):
        print(f"[SLM] Processing query: {query}")
        return "Answer: Processing..."

class MockGenAISystem:
    def draft_novel_clause(self, topic, context):
        print(f"[GenAI] Drafting actual legal text for topic: {topic}")
        try:
            prompt = f"Write a formal legal section for a patent application regarding: {topic}.\n\nContext of the patent:\n{context}\n\nMake it professional and legally sound."
            response = client.chat.completions.create(
                model=MODEL,
                messages=[
                    {"role": "system", "content": "You are an expert patent attorney AI assistant."},
                    {"role": "user", "content": prompt}
                ]
            )
            return response.choices[0].message.content.strip()
        except Exception as e:
            return f"[API Error generating {topic}: {str(e)}]"
        
    def simulate_scenario(self, clause):
        print(f"[GenAI] Simulating legal outcomes for clause...")
        return "Legally sound (Verified by LLM)"

if __name__ == '__main__':
    print("--- Phase 3, 4, 5: NLP, SLM, and GenAI Integration (Real API) ---")
    genai = MockGenAISystem()
    print(genai.draft_novel_clause("Introduction", "A machine learning algorithm for stock prediction."))
