# ☀️ Solar Rooftop Analysis AI Tool

This project is part of the AI Internship Assessment for WattMonk. It is an AI-powered tool that analyzes rooftop satellite images to assess solar panel installation potential, provide installation recommendations, and estimate ROI.

---

## 🔍 Features

- Upload rooftop satellite images (.jpg/.png)
- AI-driven image analysis using Claude 3 Sonnet via OpenRouter API
- Estimation of:
  - Rooftop area (sqm)
  - Panel count and system capacity (kW)
  - Installation cost and annual savings
  - ROI and payback period
- Real-time performance metrics (processing time)
- Enhanced Streamlit UI with clean layout and styling

---

## 🛠️ Tech Stack

- **Frontend/UI**: Streamlit
- **Backend Logic**: Python
- **AI Model**: Claude 3 Sonnet via OpenRouter API
- **Deployment Ready**: Locally and on Hugging Face Spaces

---

## 🚀 Getting Started

### 1. Clone or Download

Download the ZIP or clone this repo.

```bash
git clone https://github.com/kartikey-agrawal/solar_ai_tool.git
cd solar_ai_tool
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Add Your API Key

In `image_analysis.py`, replace:
```python
"Authorization": "Bearer YOUR_API_KEY"
```
with your actual OpenRouter key.

### 4. Run the App

```bash
streamlit run main.py
```

---

## 🧪 Example Use Case

1. Upload a rooftop satellite image.
2. The app processes the image using Claude 3 and estimates solar potential.
3. Output includes system capacity, cost, and ROI.

---

## 📈 Performance Metrics

- Measures total image-to-analysis processing time
- Displayed after every submission for transparency

---

## 📂 Project Structure

```
solar_ai_tool/
├── main.py
├── styles.css
├── image_analysis.py
├── solar_calculations.py
├── requirements.txt
├── README.md
└── setup_instructions.txt
```

---

## 🌱 Future Improvements

- Auto-crop rooftop from wider satellite image
- Use map API to fetch rooftops from addresses
- Integrate financial incentive calculators
- Export analysis as PDF report

---

## 👨‍💼 Author

Kartikey Agrawal  
AI Intern Applicant – WattMonk  
[LinkedIn](https://www.linkedin.com/in/kartikey-agrawal02)
