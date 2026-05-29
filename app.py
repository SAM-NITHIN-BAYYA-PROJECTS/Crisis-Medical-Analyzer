import os
import base64
from flask import Flask, render_template, request, jsonify
from openai import OpenAI
from PIL import Image
import io

app = Flask(__name__)

# Initialize the OpenAI client pointing to local LM Studio
client = OpenAI(
    base_url="http://localhost:1234/v1", 
    api_key="lm-studio"
)

def encode_image_to_base64(image_bytes):
    """Converts image bytes to a base64 string for the vision model."""
    return base64.b64encode(image_bytes).decode('utf-8')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text_prompt = request.form.get('text_prompt', '').strip()
    uploaded_file = request.files.get('file')
    
    system_instruction = (
        "You are an offline crisis medical analyzer. "
        "Analyze the provided handwritten notes or text transcript accurately "
        "and structure your findings strictly according to the requested JSON schema."
    )
    
    content_list = []
    
    if uploaded_file and uploaded_file.filename != '':
        file_extension = os.path.splitext(uploaded_file.filename)[1].lower()
        file_bytes = uploaded_file.read()
        
        if file_extension in ['.png', '.jpg', '.jpeg']:
            base64_image = encode_image_to_base64(file_bytes)
            content_list.append({
                "type": "image_url",
                "image_url": {
                    "url": f"data:image/jpeg;base64,{base64_image}"
                }
            })
            content_list.append({
                "type": "text",
                "text": "Transcribe the handwritten text in this image accurately, then analyze it."
            })
            
        elif file_extension in ['.txt']:
            text_prompt += "\n" + file_bytes.decode('utf-8')

    if text_prompt:
        content_list.append({
            "type": "text",
            "text": text_prompt
        })

    if not content_list:
        return jsonify({"error": "Please provide either text data or upload an image/document."}), 400

    try:
        # Request completion from local Gemma using the supported 'json_schema' configuration format
        response = client.chat.completions.create(
            model="local-model",
            messages=[
                {"role": "system", "content": system_instruction},
                {"role": "user", "content": content_list}
            ],
            temperature=0.2,
            response_format={
                "type": "json_schema",
                "json_schema": {
                    "name": "medical_analysis_response",
                    "strict": "true",
                    "schema": {
                        "type": "object",
                        "properties": {
                            "extracted_text": {
                                "type": "string",
                                "description": "The exact transcription of any text detected from the uploaded media."
                            },
                            "summary": {
                                "type": "string",
                                "description": "Brief medical summary overview of the current case."
                            },
                            "critical_flags": {
                                "type": "string",
                                "description": "Any high-risk warnings or emergencies spotted."
                            },
                            "action_items": {
                                "type": "string",
                                "description": "Recommended immediate next steps or supportive instructions."
                            }
                        },
                        "required": ["extracted_text", "summary", "critical_flags", "action_items"]
                    }
                }
            }
        )
        
        return jsonify({"success": True, "data": response.choices[0].message.content})

    except Exception as e:
        return jsonify({"success": False, "error": str(e)}), 500

if __name__ == '__main__':
    # Hosted locally; accessible via local network for other offline devices if needed
    app.run(host='0.0.0.0', port=5000, debug=True)