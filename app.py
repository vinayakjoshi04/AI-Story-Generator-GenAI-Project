from flask import Flask, render_template, request
from transformers import pipeline, set_seed

generator = pipeline('text-generation', model='gpt2-medium')
set_seed(42)

app = Flask(__name__)

@app.route('/', methods=["GET", "POST"])
def index():
    story = ""
    if request.method == "POST":
        user_prompt = request.form["prompt"]
        prompt = f"Once upon a time, {user_prompt.strip().capitalize()}"

        response = generator(prompt,
                             max_length=250,
                             num_return_sequences=1,
                             temperature=0.9,
                             top_p=0.95,
                             do_sample=True,
                             pad_token_id=50256)

        generated = response[0]['generated_text']

        if generated.lower().startswith(prompt.lower()):
            story = generated[len(prompt):].strip().capitalize()
        else:
            story = generated.strip()

        story = prompt + " " + story

    return render_template("index.html", story=story)

if __name__ == "__main__":
    app.run(debug=True)
