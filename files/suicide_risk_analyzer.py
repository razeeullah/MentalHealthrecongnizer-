"""
Suicide Risk Analyzer using Google Gemini AI
A mental health assessment tool that analyzes text for suicide risk indicators
"""

import os
import google.generativeai as genai
from datetime import datetime
import json

class SuicideRiskAnalyzer:
    def __init__(self, api_key):
        """
        Initialize the analyzer with Google Gemini API
        
        Args:
            api_key: Your Google API key for Gemini
        """
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-pro')
        
        # Mental health resources
        self.resources = {
            "emergency": {
                "US": "988 (Suicide & Crisis Lifeline)",
                "International": "https://findahelpline.com",
                "Text": "Text HOME to 741741 (Crisis Text Line)"
            },
            "websites": [
                "https://suicidepreventionlifeline.org",
                "https://www.opencounseling.com/suicide-hotlines"
            ]
        }
    
    def analyze_text(self, user_text):
        """
        Analyze user text for suicide risk indicators
        
        Args:
            user_text: The text to analyze
            
        Returns:
            dict: Analysis results with risk level and recommendations
        """
        
        # Construct the analysis prompt
        prompt = f"""
        You are a mental health assessment AI assistant. Analyze the following text for suicide risk indicators.
        
        Assess the text for:
        1. Direct expressions of suicidal ideation
        2. Hopelessness or helplessness
        3. Social isolation or withdrawal
        4. Severe emotional pain
        5. Talk of being a burden
        6. Recent losses or trauma
        7. Substance abuse mentions
        8. Planning or preparation indicators
        
        Text to analyze:
        "{user_text}"
        
        Provide your response in JSON format with the following structure:
        {{
            "risk_level": "low/moderate/high/severe",
            "confidence": "0-100",
            "indicators_found": ["list of specific indicators"],
            "reasoning": "brief explanation of assessment",
            "immediate_action_needed": true/false,
            "supportive_response": "compassionate message to the person"
        }}
        
        Be compassionate, non-judgmental, and err on the side of caution.
        """
        
        try:
            response = self.model.generate_content(prompt)
            
            # Extract JSON from response
            response_text = response.text
            
            # Clean up response to extract JSON
            if "```json" in response_text:
                json_start = response_text.find("```json") + 7
                json_end = response_text.find("```", json_start)
                response_text = response_text[json_start:json_end].strip()
            elif "```" in response_text:
                json_start = response_text.find("```") + 3
                json_end = response_text.find("```", json_start)
                response_text = response_text[json_start:json_end].strip()
            
            analysis = json.loads(response_text)
            
            # Add timestamp
            analysis['timestamp'] = datetime.now().isoformat()
            analysis['original_text'] = user_text
            
            return analysis
            
        except Exception as e:
            print(f"Error during analysis: {e}")
            return {
                "error": str(e),
                "risk_level": "unknown",
                "message": "Unable to complete analysis. Please seek professional help if needed."
            }
    
    def get_recommendations(self, risk_level):
        """
        Get recommendations based on risk level
        
        Args:
            risk_level: The assessed risk level
            
        Returns:
            dict: Recommendations and resources
        """
        recommendations = {
            "severe": {
                "action": "IMMEDIATE PROFESSIONAL HELP REQUIRED",
                "steps": [
                    "Call 988 (Suicide & Crisis Lifeline) immediately",
                    "Go to nearest emergency room",
                    "Call 911 if in immediate danger",
                    "Do not leave the person alone"
                ],
                "urgency": "CRITICAL"
            },
            "high": {
                "action": "Urgent professional support needed",
                "steps": [
                    "Contact a mental health professional today",
                    "Call 988 or crisis hotline for immediate support",
                    "Reach out to trusted friend or family member",
                    "Create a safety plan with professional help"
                ],
                "urgency": "HIGH"
            },
            "moderate": {
                "action": "Professional consultation recommended",
                "steps": [
                    "Schedule appointment with therapist or counselor",
                    "Talk to someone you trust about how you're feeling",
                    "Call crisis hotline if feelings intensify",
                    "Practice self-care and avoid isolation"
                ],
                "urgency": "MODERATE"
            },
            "low": {
                "action": "Supportive resources available",
                "steps": [
                    "Consider talking to a counselor or therapist",
                    "Maintain social connections",
                    "Practice mental health wellness activities",
                    "Know that help is available if needed"
                ],
                "urgency": "LOW"
            }
        }
        
        return recommendations.get(risk_level, recommendations["moderate"])
    
    def generate_report(self, analysis):
        """
        Generate a comprehensive report from analysis
        
        Args:
            analysis: The analysis results
            
        Returns:
            str: Formatted report
        """
        risk_level = analysis.get('risk_level', 'unknown')
        recommendations = self.get_recommendations(risk_level)
        
        report = f"""
{'='*60}
SUICIDE RISK ANALYSIS REPORT
{'='*60}

Timestamp: {analysis.get('timestamp', 'N/A')}

RISK ASSESSMENT:
- Risk Level: {risk_level.upper()}
- Confidence: {analysis.get('confidence', 'N/A')}%
- Urgency: {recommendations['urgency']}

INDICATORS FOUND:
"""
        
        for indicator in analysis.get('indicators_found', []):
            report += f"  • {indicator}\n"
        
        report += f"""
REASONING:
{analysis.get('reasoning', 'N/A')}

SUPPORTIVE MESSAGE:
{analysis.get('supportive_response', 'Please know that help is available.')}

{'='*60}
RECOMMENDATIONS: {recommendations['action']}
{'='*60}
"""
        
        for step in recommendations['steps']:
            report += f"  {step}\n"
        
        report += f"""
{'='*60}
CRISIS RESOURCES:
{'='*60}
"""
        
        for location, number in self.resources['emergency'].items():
            report += f"  {location}: {number}\n"
        
        report += "\nAdditional Resources:\n"
        for website in self.resources['websites']:
            report += f"  • {website}\n"
        
        report += f"""
{'='*60}
IMPORTANT DISCLAIMER:
This is an AI-assisted assessment tool and does not replace
professional mental health evaluation. Always consult with
qualified mental health professionals for proper diagnosis
and treatment.
{'='*60}
"""
        
        return report


def main():
    """
    Main function to run the analyzer
    """
    print("Suicide Risk Analyzer - Mental Health Assessment Tool")
    print("="*60)
    print("\nIMPORTANT: This tool is for assessment purposes only.")
    print("It does not replace professional mental health care.\n")
    
    # Get API key (you'll need to set this)
    api_key = os.getenv('GOOGLE_API_KEY')
    
    if not api_key:
        print("ERROR: Please set GOOGLE_API_KEY environment variable")
        print("Get your API key from: https://makersuite.google.com/app/apikey")
        return
    
    # Initialize analyzer
    analyzer = SuicideRiskAnalyzer(api_key)
    
    # Example usage
    print("Enter text to analyze (or 'quit' to exit):")
    print("-"*60)
    
    while True:
        user_input = input("\nText to analyze: ").strip()
        
        if user_input.lower() == 'quit':
            break
        
        if not user_input:
            print("Please enter some text to analyze.")
            continue
        
        print("\nAnalyzing...")
        
        # Perform analysis
        analysis = analyzer.analyze_text(user_input)
        
        # Generate and display report
        report = analyzer.generate_report(analysis)
        print(report)
        
        # Save to file
        filename = f"risk_analysis_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w') as f:
            json.dump(analysis, f, indent=2)
        print(f"\nAnalysis saved to: {filename}")


if __name__ == "__main__":
    main()
