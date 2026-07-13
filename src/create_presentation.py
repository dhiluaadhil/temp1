from reportlab.lib.pagesizes import landscape, letter
from reportlab.pdfgen import canvas
from reportlab.lib import colors
import os

def create_slide(c, title, bullets):
    c.setFillColor(colors.HexColor("#0b0f19"))
    c.rect(0, 0, landscape(letter)[0], landscape(letter)[1], fill=1)
    
    # Title
    c.setFont("Helvetica-Bold", 36)
    c.setFillColor(colors.HexColor("#a855f7"))
    c.drawString(50, landscape(letter)[1] - 80, title)
    
    # Bullets
    c.setFont("Helvetica", 24)
    c.setFillColor(colors.white)
    y_position = landscape(letter)[1] - 160
    for bullet in bullets:
        c.drawString(70, y_position, f"• {bullet}")
        y_position -= 50
    c.showPage()

def generate_pdf(filepath):
    c = canvas.Canvas(filepath, pagesize=landscape(letter))
    
    # Slide 1: Title
    c.setFillColor(colors.HexColor("#0b0f19"))
    c.rect(0, 0, landscape(letter)[0], landscape(letter)[1], fill=1)
    c.setFont("Helvetica-Bold", 48)
    c.setFillColor(colors.HexColor("#6366f1"))
    c.drawCentredString(landscape(letter)[0]/2, landscape(letter)[1]/2 + 20, "Automated Legal Document Generation")
    c.setFont("Helvetica", 24)
    c.setFillColor(colors.white)
    c.drawCentredString(landscape(letter)[0]/2, landscape(letter)[1]/2 - 30, "Project Overview for HR & Leadership")
    c.showPage()
    
    # Slide 2: The Challenge
    create_slide(c, "The Challenge", [
        "Manual drafting of Intellectual Property (IP) filings is slow.",
        "High risk of human error in complex legal terminology.",
        "Scaling legal operations requires expensive, specialized labor.",
        "Inconsistent wording across different attorneys and departments."
    ])
    
    # Slide 3: Our Solution
    create_slide(c, "Our Solution: Agentic AI", [
        "A fully autonomous AI pipeline tailored for legal documents.",
        "Evolves from basic Machine Learning to Advanced Generative AI.",
        "Capable of perceiving user needs and planning document structure.",
        "Automatically drafts novel clauses and simulates legal risk."
    ])
    
    # Slide 4: How It Works
    create_slide(c, "How It Works (The Technology)", [
        "Phase 1: Deep Learning analyzes historical IP success rates.",
        "Phase 2: NLP extracts key entities (Inventors, Companies).",
        "Phase 3: GenAI (GPT-4o) drafts formal patent clauses.",
        "User Interface: A sleek, user-friendly web dashboard."
    ])
    
    # Slide 5: Business Impact
    create_slide(c, "Business Impact", [
        "Efficiency: Reduces drafting time from days to seconds.",
        "Accuracy: AI validates clauses against legal precedents.",
        "Cost Savings: Automates the repetitive aspects of legal work.",
        "Scalability: Handles infinite concurrent patent applications."
    ])
    
    c.save()

if __name__ == "__main__":
    output_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "HR_Project_Presentation.pdf")
    generate_pdf(output_path)
    print(f"Presentation saved to: {output_path}")
