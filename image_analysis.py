import os
import requests
from PIL import Image
import base64
import io

def analyze_image(image: Image.Image):
    try:
        # Convert image to base64
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        img_base64 = base64.b64encode(buffered.getvalue()).decode()

        # Get API key from environment variable
        api_key = os.getenv("OPENROUTER_API_KEY")
        if not api_key:
            return {"error": "Missing API key. Please set OPENROUTER_API_KEY in your environment."}

        # Claude 3 Sonnet via OpenRouter
        url = "https://openrouter.ai/api/v1/chat/completions"

        headers = {
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        }

        prompt = f"""
You are a solar analysis expert. Analyze the following rooftop satellite image to estimate:
1. Total usable rooftop area in square meters (approx.)
2. Obstructions or issues
3. Suitability for solar panels
4. One-line recommendation

Format the output as JSON like:
{{
  "raw_output": "...",
  "estimated_area_sqm": number
}}
The image (base64) is: {img_base64}
"""

        payload = {
            "model": "anthropic/claude-3-sonnet",
            "messages": [
                {"role": "user", "content": prompt}
            ]
        }

        response = requests.post(url, headers=headers, json=payload, timeout=60)

        if response.status_code != 200:
            return {"error": f"API call failed: {response.status_code} - {response.text}"}

        result_text = response.json()["choices"][0]["message"]["content"]

        # Try to convert stringified JSON
        try:
            import json
            parsed = json.loads(result_text)
            return parsed
        except:
            return {"raw_output": result_text}

    except Exception as e:
        return {"error": str(e)}
