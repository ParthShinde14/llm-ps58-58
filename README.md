
# 💊 MediGuide AI

### PS 58 – Medicine Information Lookup

## 1. Project Overview

MediGuide AI is a Generative AI-powered medicine information lookup application that helps users understand the uses, composition, and commonly reported side effects of medicines in simple language.

The application retrieves medicine information from a public CSV dataset using Pandas and uses Google Gemini to generate easy-to-understand explanations.

## 2. Problem Statement

People often lack basic information about medicines and their intended uses and side effects.

This project addresses the problem by combining structured medicine data retrieval with LLM-based explanations.

## 3. Features

- Search medicines by name.
- Exact and partial medicine matching.
- Display medicine composition.
- Retrieve medicine uses and side effects.
- Generate simple explanations using Google Gemini.
- Handle medicines not found in the dataset.
- Display a medical disclaimer.

## 4. Technologies Used

| Technology | Purpose |
|---|---|
| Python | Application development |
| Pandas | Medicine data retrieval |
| Streamlit | Web interface |
| Google Gemini API | AI-generated explanations |
| Google GenAI SDK | Gemini integration |
| python-dotenv | API key management |

## 5. Dataset

- Dataset: Medicine Details
- Records: 11,825
- Columns: 9
- Format: CSV

The dataset contains medicine names, composition, uses, side effects, manufacturer details and medicine review information.

## 6. Application Architecture

1. User enters a medicine name.
2. Streamlit receives the input.
3. Pandas searches the medicine CSV.
4. The application retrieves the matching medicine record.
5. Retrieved information is sent to Google Gemini.
6. Gemini generates a simple explanation.
7. Streamlit displays the result.

If a medicine is absent from the dataset, the application displays a not-found message.

## 7. Installation and Execution

### Clone the repository

```bash
git clone https://github.com/ParthShinde14/llm-ps58-58.git
cd llm-ps58-58
```

### Create virtual environment

```bash
python -m venv venv
venv\Scripts\activate
```

### Install dependencies

```bash
pip install -r requirements.txt
```

### Configure API key

Create a `.env` file:

```env
GEMINI_API_KEY=your_api_key_here
```

### Run application

```bash
streamlit run app.py
```

## 8. Screenshots

Application screenshots are available in the `screenshots` folder.

## 9. Medical Disclaimer

This application is intended for educational purposes only. The information may be incomplete or outdated and does not replace professional medical advice. Users should consult qualified healthcare professionals before making medical decisions.

## 10. Conclusion

MediGuide AI demonstrates how structured datasets and Large Language Models can be integrated to make medicine information easier to understand.
