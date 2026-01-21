# Configuration file for Suicide Risk Analyzer
# Edit these settings to customize the behavior

import os

# API Configuration
GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY', '')
MODEL_NAME = 'gemini-pro'

# Risk Level Thresholds
RISK_LEVELS = {
    'severe': {
        'threshold': 80,  # Confidence threshold for severe risk
        'keywords': ['suicide', 'end my life', 'kill myself', 'plan to die']
    },
    'high': {
        'threshold': 60,
        'keywords': ['hopeless', 'no way out', 'burden', 'worthless']
    },
    'moderate': {
        'threshold': 40,
        'keywords': ['depressed', 'alone', 'isolated', 'meaningless']
    },
    'low': {
        'threshold': 0,
        'keywords': ['stressed', 'down', 'difficult']
    }
}

# Crisis Resources (customize for your region)
CRISIS_RESOURCES = {
    "emergency": {
        "United States": "988 (Suicide & Crisis Lifeline)",
        "United Kingdom": "116 123 (Samaritans)",
        "Canada": "1-833-456-4566 (Talk Suicide Canada)",
        "Australia": "13 11 14 (Lifeline)",
        "International": "https://findahelpline.com",
        "Text Support": "Text HOME to 741741 (Crisis Text Line)"
    },
    "websites": [
        "https://suicidepreventionlifeline.org",
        "https://www.opencounseling.com/suicide-hotlines",
        "https://www.befrienders.org",
        "https://www.iasp.info/resources/Crisis_Centres"
    ],
    "professional": [
        "Contact a licensed therapist or counselor",
        "Visit your primary care physician",
        "Go to nearest emergency room if in immediate danger",
        "Contact your local mental health crisis center"
    ]
}

# Analysis Settings
ANALYSIS_SETTINGS = {
    'max_tokens': 1000,
    'temperature': 0.3,  # Lower temperature for more consistent results
    'enable_logging': True,
    'save_reports': True,
    'report_directory': './reports/'
}

# Web Application Settings
WEB_APP_CONFIG = {
    'host': '0.0.0.0',
    'port': 5000,
    'debug': False,  # Set to False in production
    'max_text_length': 5000,  # Maximum characters for analysis
}

# Privacy Settings
PRIVACY_CONFIG = {
    'store_analyses': False,  # Do not store user data by default
    'anonymize_reports': True,
    'data_retention_days': 0,  # 0 means no retention
}

# Risk Indicators to Analyze
RISK_INDICATORS = [
    "Direct expressions of suicidal ideation",
    "Specific plans or methods mentioned",
    "Hopelessness or helplessness",
    "Social isolation or withdrawal",
    "Severe emotional pain or anguish",
    "Talk of being a burden to others",
    "Recent significant losses or trauma",
    "Substance abuse mentions",
    "Giving away possessions",
    "Saying goodbye or seeking closure",
    "Previous suicide attempts mentioned",
    "Mental health condition mentions",
    "Access to lethal means",
    "Impulsivity or recklessness",
    "Changes in mood or behavior"
]

# Supportive Response Templates
SUPPORTIVE_MESSAGES = {
    'severe': "I'm deeply concerned about what you've shared. You don't have to face this alone. Please reach out to a crisis counselor immediately - they're available 24/7 and want to help.",
    'high': "Thank you for sharing how you're feeling. These thoughts can be overwhelming, but professional support can make a real difference. Please consider reaching out to a mental health professional.",
    'moderate': "I hear that things are difficult right now. It takes courage to acknowledge these feelings. Speaking with a counselor or therapist could provide valuable support.",
    'low': "It sounds like you're going through a challenging time. Remember that it's okay to seek support, and reaching out for help is a sign of strength."
}

# Language and Localization
LANGUAGE_CONFIG = {
    'default_language': 'en',
    'available_languages': ['en'],  # Extend for multilingual support
    'timezone': 'UTC'
}
