import base64
import requests
from PIL import Image
from io import BytesIO

def analyze_image(image: Image.Image):
    # Convert image to base64
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")

    # Claude-compatible payload
    payload = {
        "model": "anthropic/claude-3-sonnet",
        "messages": [{
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": (
                        "Analyze the rooftop in this image and provide:\n"
                        "- Estimated rooftop area in square meters\n"
                        "- Obstruction presence (trees, chimneys, etc.)\n"
                        "- Suitability for solar panel installation\n"
                        "- A short one-line recommendation"
                    )
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": f"data:image/png;base64,{img_str}"
                    }
                }
            ]
        }],
        "max_tokens": 500
    }

    headers = {
        "Authorization": "Bearer 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"
    }

    response = requests.post("https://openrouter.ai/api/v1/chat/completions", json=payload, headers=headers)

    if response.status_code == 200:
        try:
            content = response.json()["choices"][0]["message"]["content"]
            # Extract area (optional enhancement)
            estimated_area = 120  # fallback assumption
            return {
                "raw_output": content,
                "estimated_area_sqm": estimated_area
            }
        except Exception as e:
            return {"error": f"Parsing error: {str(e)}"}
    else:
        return {"error": "Failed to process image. Check API key or quota."}
