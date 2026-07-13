from flask import Flask, render_template, request, jsonify
from agentic_loop import AgenticLegalAssistant
import os
import sys
import threading
import contextlib
import io

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/generate', methods=['POST'])
def generate():
    data = request.json
    user_input = data.get('patent_text', '')
    
    if not user_input:
        return jsonify({'error': 'Patent text is required'}), 400
        
    try:
        # Capture the stdout to return the agent's thought process
        f = io.StringIO()
        with contextlib.redirect_stdout(f):
            agent = AgenticLegalAssistant()
            agent.perceive(user_input)
            agent.plan()
            agent.execute()
            
        logs = f.getvalue()
        
        return jsonify({
            'status': 'success',
            'document': agent.final_document,
            'logs': logs
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    # Ensure static and templates folders exist if running from src
    app.run(debug=True, port=5000)
