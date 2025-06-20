from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
from dotenv import load_dotenv
from fpdf import FPDF
from gtts import gTTS
import io
import re
import base64

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

app = Flask(__name__)

available_models = [
    m.name for m in genai.list_models() if 'generateContent' in m.supported_generation_methods
]

@app.route("/")
def index():
    return render_template("index.html", models=available_models)

@app.route("/generate", methods=["POST"])
def generate():
    try:
        data = request.json
        user_prompt = data.get("prompt", "").strip()
        model_name = data.get("model_name", "models/gemini-1.5-flash")
        genre = data.get("genre", "Adventure")
        character_name = data.get("character_name", "Alex")
        character_type = data.get("character_type", "explorer")
        length = data.get("length", "medium")
        language = data.get("language", "English")

        if not user_prompt:
            return jsonify({"error": "Please enter a prompt."}), 400

        model = genai.GenerativeModel(model_name=model_name)
        prompt = (
            f"Write a {length}, {genre.lower()} story in {language} about a {character_type} named {character_name}. "
            f"The story should start with: {user_prompt}"
        )

        response = model.generate_content(prompt)
        story = response.text.strip()

        title_prompt = f"Give a short, exciting title for this {genre.lower()} story in {language}: {prompt}"
        title_response = model.generate_content(title_prompt)
        title = title_response.text.strip().replace('"', '').replace('\n', '').replace('\r', '')

        return jsonify({"title": title, "story": story})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/continue", methods=["POST"])
def continue_story():
    try:
        data = request.json
        current_story = data.get("story", "").strip()
        model_name = data.get("model_name", "models/gemini-1.5-flash")

        if not current_story:
            return jsonify({"error": "No story found to continue."}), 400

        model = genai.GenerativeModel(model_name=model_name)
        continuation_prompt = f"Continue this story: {current_story}"
        response = model.generate_content(continuation_prompt)
        extended_story = response.text.strip()

        return jsonify({"continued_story": extended_story})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/speak", methods=["POST"])
def speak():
    try:
        story = request.json.get("story", "").strip()
        language = request.json.get("language", "English")

        if not story:
            return jsonify({"error": "No story to convert to speech."}), 400

        lang_code = {
            "English": "en", "Hindi": "hi", "Spanish": "es",
            "French": "fr", "German": "de"
        }.get(language, "en")

        tts = gTTS(text=story[:4000], lang=lang_code)
        audio = io.BytesIO()
        tts.write_to_fp(audio)
        audio.seek(0)
        base64_audio = base64.b64encode(audio.read()).decode('utf-8')

        return jsonify({"audio_base64": base64_audio})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route("/download", methods=["POST"])
def download():
    title = request.form.get("title", "Story").strip()
    story = request.form.get("story", "")
    format_type = request.form.get("format", "txt")

    safe_title = re.sub(r'[^\w\s-]', '', title).strip().replace(' ', '_')[:50]

    if format_type == "pdf":
        def clean_text(text):
            return text.encode("latin-1", "replace").decode("latin-1")

        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)
        content = clean_text(f"{title}\n\n{story}")
        pdf.multi_cell(0, 10, content)

        pdf_bytes = pdf.output(dest='S').encode('latin-1')
        response = app.response_class(pdf_bytes, mimetype='application/pdf')
        response.headers["Content-Disposition"] = f"attachment; filename={safe_title}.pdf"
        return response

    else:
        content = f"{title}\n\n{story}"
        response = app.response_class(content, mimetype='text/plain; charset=utf-8')
        response.headers["Content-Disposition"] = f"attachment; filename={safe_title}.txt"
        return response

if __name__ == "__main__":
    app.run(debug=True)
