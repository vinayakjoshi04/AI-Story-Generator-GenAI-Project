from flask import Flask, render_template, request
import google.generativeai as genai
import os
from dotenv import load_dotenv

# Load environment variables from .env
load_dotenv()

# Configure the Generative AI API
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Initialize Flask app
app = Flask(__name__)

# List and print available models (optional, for debugging)
models = genai.list_models()
for m in models:
    print(f"Model: {m.name} | Supports: {m.supported_generation_methods}")

# Use a valid supported model
model = genai.GenerativeModel(model_name="models/gemini-1.5-flash")  # You can also use "models/gemini-2.5-pro"

@app.route("/", methods=["GET", "POST"])
def index():
    story = ""
    if request.method == "POST":
        user_prompt = request.form.get("prompt", "").strip()
        if user_prompt:
            prompt = f"Once upon a time, {user_prompt.capitalize()}"
            try:
                response = model.generate_content(prompt)
                story = response.text.strip()
            except Exception as e:
                story = f"❌ Error: {str(e)}"
        else:
            story = "⚠️ Please enter a prompt."

    return render_template("index.html", story=story)

if __name__ == "__main__":
    app.run(debug=True)
