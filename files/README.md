# Suicide Risk Analyzer - AI Mental Health Assessment Tool

An AI-powered text analysis system that assesses suicide risk indicators using Google Gemini AI. This tool is designed to help identify individuals who may need mental health support.

## ⚠️ CRITICAL DISCLAIMER

**This tool is for assessment and educational purposes only. It does NOT replace professional mental health evaluation, diagnosis, or treatment.**

- Always consult qualified mental health professionals
- In crisis situations, call emergency services (911) or crisis hotlines immediately
- This tool should be used as a supplementary resource, not a primary diagnostic tool

## 🚨 Crisis Resources

- **US Crisis Hotline**: 988 (Suicide & Crisis Lifeline)
- **Crisis Text Line**: Text HOME to 741741
- **International**: https://findahelpline.com
- **Emergency**: 911 (US) or your local emergency number

## 🎯 Features

- **AI-Powered Analysis**: Uses Google Gemini AI for sophisticated text analysis
- **Risk Assessment**: Categorizes risk into Low, Moderate, High, or Severe levels
- **Indicator Detection**: Identifies specific suicide risk indicators in text
- **Compassionate Responses**: Provides supportive, non-judgmental feedback
- **Resource Provision**: Automatically provides crisis resources based on risk level
- **Web Interface**: User-friendly web application for easy access
- **Report Generation**: Creates detailed assessment reports with timestamps

## 📋 Risk Indicators Analyzed

The system analyzes text for:

1. **Direct Suicidal Ideation**: Explicit thoughts of self-harm or suicide
2. **Hopelessness/Helplessness**: Expressions of despair or lack of control
3. **Social Isolation**: Withdrawal from relationships and activities
4. **Severe Emotional Pain**: Intense psychological distress
5. **Burden Beliefs**: Feeling like a burden to others
6. **Recent Trauma/Loss**: Significant life stressors
7. **Substance Abuse**: Mentions of drug or alcohol misuse
8. **Planning/Preparation**: Indicators of suicide planning

## 🛠️ Installation

### Prerequisites

- Python 3.8 or higher
- Google API Key (Gemini AI)

### Step 1: Clone or Download

Download all project files to your local machine.

### Step 2: Install Dependencies

```bash
pip install -r requirements.txt
```

Or install individually:

```bash
pip install google-generativeai python-dotenv flask
```

### Step 3: Get Google API Key

1. Visit https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Create a new API key
4. Copy the API key

### Step 4: Set Environment Variable

**On Windows (Command Prompt):**
```cmd
set GOOGLE_API_KEY=your_api_key_here
```

**On Windows (PowerShell):**
```powershell
$env:GOOGLE_API_KEY="your_api_key_here"
```

**On Mac/Linux:**
```bash
export GOOGLE_API_KEY=your_api_key_here
```

**Or create a .env file:**
```
GOOGLE_API_KEY=your_api_key_here
```

## 🚀 Usage

### Option 1: Command Line Interface

Run the command-line version:

```bash
python suicide_risk_analyzer.py
```

Then enter text when prompted. Type 'quit' to exit.

**Example:**

```
Enter text to analyze (or 'quit' to exit):
--------------------------------------------------

Text to analyze: I've been feeling really down lately and don't see a way forward

Analyzing...

============================================================
SUICIDE RISK ANALYSIS REPORT
============================================================
[Results will display here]
```

### Option 2: Web Interface

1. Start the Flask server:

```bash
python app.py
```

2. Open your browser and go to:
```
http://localhost:5000
```

3. Enter text in the textarea and click "Analyze Text"

4. View detailed results including:
   - Risk level assessment
   - Confidence score
   - Identified indicators
   - Supportive message
   - Recommendations
   - Crisis resources

## 📊 Understanding Results

### Risk Levels

| Level | Description | Action Required |
|-------|-------------|-----------------|
| **SEVERE** | Immediate danger indicators present | Call 911 or crisis hotline NOW |
| **HIGH** | Significant risk factors identified | Seek professional help today |
| **MODERATE** | Some concerning indicators | Schedule professional consultation |
| **LOW** | Minimal risk indicators | Consider supportive resources |

### Confidence Score

- Represents the AI's confidence in its assessment (0-100%)
- Higher scores indicate stronger indicator presence
- Lower scores suggest ambiguous or limited information

## 🔒 Privacy & Ethics

### Data Handling

- **No Storage**: User text is not permanently stored
- **Privacy**: All processing happens in real-time
- **Confidentiality**: No data is shared with third parties
- **Reports**: Saved locally only if user chooses to save

### Ethical Considerations

1. **Non-Judgmental**: System provides compassionate, supportive responses
2. **Cultural Sensitivity**: Designed to be respectful of diverse backgrounds
3. **False Positives**: System errs on side of caution to ensure safety
4. **Professional Referral**: Always recommends professional help when appropriate

## 🏗️ Project Structure

```
suicide-risk-analyzer/
│
├── suicide_risk_analyzer.py    # Core analysis engine
├── app.py                       # Flask web application
├── requirements.txt             # Python dependencies
├── templates/
│   └── index.html              # Web interface
└── README.md                    # This file
```

## 🧪 Example Use Cases

### 1. Mental Health Screening
Organizations can use this tool for preliminary assessment of written responses in mental health questionnaires.

### 2. Crisis Hotline Support
Supplement crisis hotline operations by analyzing chat transcripts for risk prioritization.

### 3. Research & Training
Mental health professionals can use this for training or research purposes.

### 4. Educational Tool
Teach about suicide risk factors and the importance of mental health awareness.

## ⚙️ Customization

### Modify Risk Indicators

Edit the `analyze_text()` method in `suicide_risk_analyzer.py` to adjust which indicators are analyzed:

```python
prompt = f"""
Assess the text for:
1. Your custom indicator 1
2. Your custom indicator 2
...
"""
```

### Adjust Crisis Resources

Update the `resources` dictionary in the `__init__` method:

```python
self.resources = {
    "emergency": {
        "Your Country": "Your Crisis Number"
    }
}
```

### Change Risk Thresholds

Modify the `get_recommendations()` method to adjust response levels.

## 🐛 Troubleshooting

### API Key Issues

**Error: "Please set GOOGLE_API_KEY environment variable"**

- Solution: Make sure you've set the environment variable correctly
- Verify: Print the variable with `echo %GOOGLE_API_KEY%` (Windows) or `echo $GOOGLE_API_KEY` (Mac/Linux)

### Import Errors

**Error: "No module named 'google.generativeai'"**

- Solution: Install dependencies with `pip install -r requirements.txt`

### Web Interface Not Loading

**Error: "Connection refused" or "Unable to connect"**

- Solution: Make sure Flask is running with `python app.py`
- Check: Verify the URL is http://localhost:5000

## 📝 Technical Details

### Technology Stack

- **AI Model**: Google Gemini Pro
- **Backend**: Python 3.8+
- **Web Framework**: Flask
- **Frontend**: HTML, CSS, JavaScript
- **API**: Google Generative AI API

### How It Works

1. **Text Input**: User provides text to analyze
2. **AI Processing**: Text sent to Google Gemini with structured prompt
3. **Risk Assessment**: AI evaluates text against multiple risk indicators
4. **JSON Response**: Structured response with risk level, confidence, indicators
5. **Report Generation**: System generates comprehensive report with recommendations
6. **Resource Provision**: Appropriate crisis resources displayed based on risk level

## 🤝 Contributing

This is an educational project. If you'd like to improve it:

1. Add more sophisticated risk algorithms
2. Improve the UI/UX design
3. Add multilingual support
4. Integrate with professional mental health APIs
5. Add data visualization features

## 📜 License

This project is for educational and research purposes. Please use responsibly and ethically.

## 🙏 Acknowledgments

- Google Gemini AI for providing the AI capabilities
- Mental health organizations for crisis resource information
- Suicide prevention organizations for their invaluable work

## 📞 Support

For technical issues with this code:
- Review the troubleshooting section
- Check the Google Gemini API documentation

For mental health support:
- **US**: 988 (Suicide & Crisis Lifeline)
- **International**: https://findahelpline.com

---

**Remember**: This tool is a supplement, not a replacement for professional mental health care. Always prioritize human connection and professional support in mental health crises.
