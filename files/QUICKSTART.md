# 🚀 QUICK START GUIDE
## Suicide Risk Analyzer - Get Started in 5 Minutes

### ⚠️ FIRST THINGS FIRST
**In a mental health crisis RIGHT NOW?**
- 🚨 Call 988 (US Suicide & Crisis Lifeline)
- 🌍 International: https://findahelpline.com
- 💬 Text HOME to 741741 (Crisis Text Line)

---

## Step 1️⃣: Install Python

**Check if you have Python:**
```bash
python --version
```
or
```bash
python3 --version
```

**Need Python?** Download from https://www.python.org/downloads/
- Minimum version: Python 3.8
- Recommended: Python 3.10 or higher

---

## Step 2️⃣: Get Your Google API Key

1. Go to: https://makersuite.google.com/app/apikey
2. Sign in with your Google account
3. Click **"Get API Key"** or **"Create API Key"**
4. Copy your API key (looks like: `AIzaSyB...`)

**Keep this key SECRET!** Don't share it or commit it to public repositories.

---

## Step 3️⃣: Install Dependencies

Open terminal/command prompt in the project folder and run:

```bash
pip install google-generativeai flask python-dotenv
```

Or use the requirements file:
```bash
pip install -r requirements.txt
```

---

## Step 4️⃣: Set Your API Key

### Option A: Environment Variable (Recommended)

**Windows (Command Prompt):**
```cmd
set GOOGLE_API_KEY=your_api_key_here
```

**Windows (PowerShell):**
```powershell
$env:GOOGLE_API_KEY="your_api_key_here"
```

**Mac/Linux:**
```bash
export GOOGLE_API_KEY=your_api_key_here
```

### Option B: Create .env File

Create a file named `.env` in the project folder:
```
GOOGLE_API_KEY=your_api_key_here
```

---

## Step 5️⃣: Run the Application

### Option A: Web Interface (Recommended for Beginners)

1. Start the server:
```bash
python app.py
```

2. Open your browser and go to:
```
http://localhost:5000
```

3. Enter text and click "Analyze"!

### Option B: Command Line

```bash
python suicide_risk_analyzer.py
```

Then type or paste text when prompted.

---

## 📝 Example Usage

### Web Interface:
1. Open http://localhost:5000
2. Type or paste text in the box
3. Click "Analyze Text"
4. View results and recommendations

### Command Line:
```
Text to analyze: I've been feeling really down and hopeless lately

Analyzing...
[Results display with risk level, indicators, and resources]
```

---

## 🧪 Test with Examples

Run the example test cases:
```bash
python example_tests.py
```

This will analyze pre-written examples showing different risk levels.

---

## ⚙️ Customization

Edit `config.py` to customize:
- Crisis resources for your region
- Risk level thresholds
- Analysis parameters
- Language settings

---

## 🐛 Troubleshooting

### "No module named 'google.generativeai'"
**Fix:** Install dependencies
```bash
pip install google-generativeai
```

### "Please set GOOGLE_API_KEY environment variable"
**Fix:** Make sure you've set the API key (Step 4)

### Web page won't load
**Fix:** Check that Flask is running
```bash
python app.py
```
Then go to http://localhost:5000

### "Connection refused" or network errors
**Fix:** 
1. Check your internet connection
2. Verify your API key is correct
3. Try accessing https://generativelanguage.googleapis.com

---

## 📚 What's Next?

### Learn More:
- Read the full README.md for detailed documentation
- Check config.py for customization options
- Review the code to understand how it works

### Improve the Project:
- Add more languages
- Customize for your organization
- Integrate with existing systems
- Add data visualization

### Use Responsibly:
- Remember this is a tool, not a replacement for professional care
- Always provide crisis resources
- Protect user privacy
- Document your use case

---

## 🎯 Real-World Applications

### For Organizations:
- Mental health screening in schools
- Employee assistance programs
- Crisis hotline support tools
- Research and training

### For Individuals:
- Self-awareness and monitoring
- Journaling analysis
- Understanding mental health indicators
- Educational purposes

---

## ⚖️ Ethical Guidelines

1. **Privacy First**: Never store personal information without consent
2. **Professional Referral**: Always recommend professional help
3. **Non-Diagnostic**: This is assessment, not diagnosis
4. **Transparent**: Be clear about the tool's limitations
5. **Compassionate**: Maintain empathy and respect

---

## 📞 Support

### Technical Issues:
- Review this guide
- Check README.md
- Read Google Gemini API docs

### Mental Health Support:
- **DO NOT** use this tool as your only resource in a crisis
- **ALWAYS** call crisis hotlines for immediate help
- **SEEK** professional mental health care

---

## ✅ Quick Checklist

Before you start:
- [ ] Python 3.8+ installed
- [ ] Google API key obtained
- [ ] Dependencies installed
- [ ] API key set as environment variable
- [ ] Understand this is for assessment only
- [ ] Know crisis resources for your region

Ready to run:
- [ ] Run `python app.py` or `python suicide_risk_analyzer.py`
- [ ] Test with example text
- [ ] Review results and resources
- [ ] Customize for your needs (optional)

---

## 🙏 Remember

This tool exists to help identify those who need support, not to replace human connection and professional care. 

**Every person deserves compassion, understanding, and access to mental health resources.**

If you're struggling: **You matter. Help is available. You're not alone.**

🆘 **Crisis? Call 988 or visit https://findahelpline.com** 🆘

---

**Good luck with your project! Use it wisely and compassionately. 💙**
