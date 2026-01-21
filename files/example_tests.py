"""
Example Test Cases for Suicide Risk Analyzer
These are sample texts that demonstrate different risk levels
"""

# Test cases with different risk levels
TEST_CASES = {
    "severe_risk": {
        "text": "I have a plan to end it all tonight. I've written goodbye letters and I don't see any other way out. Nobody would miss me.",
        "expected_level": "severe or high",
        "description": "Direct suicidal ideation with planning"
    },
    
    "high_risk": {
        "text": "Everything feels hopeless. I'm a burden to everyone. I've been thinking a lot about not being here anymore. I feel so alone.",
        "expected_level": "high or moderate",
        "description": "Multiple risk indicators without specific plan"
    },
    
    "moderate_risk": {
        "text": "I've been really depressed lately. Nothing seems to matter anymore. I feel completely isolated and worthless.",
        "expected_level": "moderate",
        "description": "Depression and hopelessness indicators"
    },
    
    "low_risk": {
        "text": "I'm feeling down and stressed about work, but I know I'll get through this with support from my friends.",
        "expected_level": "low",
        "description": "Some stress but with positive coping"
    },
    
    "complex_case": {
        "text": "After losing my job and my relationship ending, I've been drinking heavily. I feel like everyone would be better off without me. Sometimes I think about just disappearing.",
        "expected_level": "high or moderate",
        "description": "Multiple stressors with substance use and burden thoughts"
    },
    
    "ambiguous_case": {
        "text": "Life has been tough lately. I'm struggling to find meaning in anything I do.",
        "expected_level": "moderate or low",
        "description": "Vague concerning language without specific indicators"
    }
}


def run_example_tests():
    """
    Run example tests to demonstrate the analyzer
    Note: Requires GOOGLE_API_KEY to be set
    """
    import os
    from suicide_risk_analyzer import SuicideRiskAnalyzer
    
    api_key = os.getenv('GOOGLE_API_KEY')
    
    if not api_key:
        print("ERROR: GOOGLE_API_KEY environment variable not set")
        print("Please set your API key before running tests")
        return
    
    print("="*70)
    print("SUICIDE RISK ANALYZER - EXAMPLE TEST CASES")
    print("="*70)
    print("\nIMPORTANT: These are example texts for testing purposes only.")
    print("In real situations, always take mental health concerns seriously.\n")
    
    analyzer = SuicideRiskAnalyzer(api_key)
    
    for case_name, case_data in TEST_CASES.items():
        print("\n" + "="*70)
        print(f"TEST CASE: {case_name.upper()}")
        print("="*70)
        print(f"\nDescription: {case_data['description']}")
        print(f"Expected Level: {case_data['expected_level']}")
        print(f"\nText to analyze:")
        print(f'"{case_data["text"]}"')
        print("\nAnalyzing...")
        
        # Perform analysis
        analysis = analyzer.analyze_text(case_data['text'])
        
        # Display key results
        print(f"\nRESULTS:")
        print(f"  Risk Level: {analysis.get('risk_level', 'unknown').upper()}")
        print(f"  Confidence: {analysis.get('confidence', 'N/A')}%")
        
        if analysis.get('indicators_found'):
            print(f"\n  Indicators Found:")
            for indicator in analysis['indicators_found']:
                print(f"    • {indicator}")
        
        print(f"\n  Reasoning: {analysis.get('reasoning', 'N/A')}")
        
        recommendations = analyzer.get_recommendations(analysis.get('risk_level', 'moderate'))
        print(f"\n  Recommended Action: {recommendations['action']}")
        print(f"  Urgency: {recommendations['urgency']}")
        
        input("\nPress Enter to continue to next test case...")
    
    print("\n" + "="*70)
    print("TESTING COMPLETE")
    print("="*70)
    print("\nREMINDER: This tool is for assessment purposes only.")
    print("Always consult mental health professionals for proper care.")


if __name__ == "__main__":
    run_example_tests()
