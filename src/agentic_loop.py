import time
from advanced_ai_pipelines import MockNLPSystem, MockSLMSystem, MockGenAISystem

class AgenticLegalAssistant:
    def __init__(self):
        self.nlp = MockNLPSystem()
        self.slm = MockSLMSystem()
        self.genai = MockGenAISystem()
        self.state = "IDLE"
        
    def perceive(self, user_input):
        print(f"\n[Agent: PERCEIVE] Received user request: '{user_input}'")
        self.context = self.slm.summarize(user_input)
        self.entities = self.nlp.extract_entities(user_input)
        self.state = "PLANNING"
        
    def plan(self):
        print(f"[Agent: PLAN] Designing document structure for entities: {self.entities['entities']}")
        time.sleep(1)
        self.plan_steps = ["Draft Introduction", "Draft Core Claims", "Draft Liability Clause", "Review"]
        self.state = "EXECUTING"
        
    def execute(self):
        print(f"[Agent: EXECUTE] Executing plan steps...")
        document = ""
        for step in self.plan_steps:
            print(f" -> Executing: {step}")
            clause_text = self.genai.draft_novel_clause(step, self.context)
            document += f"\n### {step} ###\n{clause_text}\n"
            time.sleep(0.5)
            
        print("[Agent: EXECUTE] Validating document against legal precedents...")
        validation = self.genai.simulate_scenario(document)
        
        if validation == "High risk of litigation":
            print("[Agent: EXECUTE] High risk detected! Triggering self-correction...")
            document += "\n[Amended to reduce risk based on simulated outcomes.]"
            
        self.final_document = document
        self.state = "COMPLETED"
        
    def run_autonomous_loop(self, user_input):
        self.perceive(user_input)
        self.plan()
        self.execute()
        print("\n--- Final Output ---")
        print("Status:", self.state)
        print("Generated Document:\n", self.final_document)

if __name__ == '__main__':
    print("--- Final Evolution: Agentic AI System ---")
    agent = AgenticLegalAssistant()
    agent.run_autonomous_loop("I need a software patent application for a new machine learning algorithm that predicts stock prices.")
