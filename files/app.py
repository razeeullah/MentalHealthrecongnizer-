"""
Web Interface for Suicide Risk Analyzer
Flask application with user-friendly interface
"""

from flask import Flask, render_template, request, jsonify
import os
from suicide_risk_analyzer import SuicideRiskAnalyzer
from datetime import datetime
import json

app = Flask(__name__)

# Initialize analyzer
api_key = os.getenv('GOOGLE_API_KEY')
analyzer = SuicideRiskAnalyzer(api_key) if api_key else None

@app.route('/')
def index():
    """Render the main page"""
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    """Analyze text endpoint"""
    if not analyzer:
        return jsonify({
            'error': 'API key not configured',
            'message': 'Please set GOOGLE_API_KEY environment variable'
        }), 500
    
    data = request.get_json()
    user_text = data.get('text', '').strip()
    
    if not user_text:
        return jsonify({
            'error': 'No text provided',
            'message': 'Please enter some text to analyze'
        }), 400
    
    # Perform analysis
    analysis = analyzer.analyze_text(user_text)
    
    # Get recommendations
    recommendations = analyzer.get_recommendations(analysis.get('risk_level', 'moderate'))
    
    # Combine results
    result = {
        **analysis,
        'recommendations': recommendations,
        'resources': analyzer.resources
    }
    
    return jsonify(result)

@app.route('/resources')
def resources():
    """Get crisis resources"""
    return jsonify(analyzer.resources if analyzer else {})

if __name__ == '__main__':
    if not api_key:
        print("WARNING: GOOGLE_API_KEY environment variable not set!")
        print("Get your API key from: https://makersuite.google.com/app/apikey")
    
    app.run(debug=True, port=5000)
