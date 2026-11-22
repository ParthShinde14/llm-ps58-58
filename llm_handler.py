import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("Gemini API key not found in .env")

client = genai.Client(api_key=API_KEY)

MODEL_NAME = "gemini-3.5-flash-lite"


def explain_medicine(medicine):

    name = medicine.get("Medicine Name", "Not available")
    composition = medicine.get("Composition", "Not available")
    uses = medicine.get("Uses", "Not available")
    side_effects = medicine.get("Side_effects", "Not available")

    prompt = f"""
You are MediGuide AI, a medicine information assistant.

Explain the following dataset information in simple English.

Medicine: {name}
Composition: {composition}
Uses: {uses}
Side Effects: {side_effects}

STRICT RULES:
1. Use only the supplied dataset information.
2. Do not invent additional uses or side effects.
3. Do not prescribe dosage or treatment.
4. Do not claim the medicine is suitable for everyone.
5. Explain that listed side effects may not occur in everyone.
6. Clearly identify information missing from the dataset.

Use these headings:

### About the Medicine
### Composition
### What is it used for?
### Listed Side Effects
### Important Note

Keep the explanation concise and easy to understand.

### Important Note

This information is for educational purposes only.
The dataset does not provide individualized medical
advice or dosage instructions. Consult a qualified
healthcare professional.

"""

    try:

        response = client.models.generate_content(model=MODEL_NAME, contents=prompt)

        if response.text:
            return response.text

        return "The AI could not generate an explanation."

    except Exception as e:

        return f"Gemini API Error: {str(e)}"
