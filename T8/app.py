from flask import Flask, request, render_template
from transformers import T5ForConditionalGeneration, T5Tokenizer, BartForConditionalGeneration, BartTokenizer, PegasusForConditionalGeneration, PegasusTokenizer

app = Flask(__name__)

# Load models and tokenizers
model_t5_small = T5ForConditionalGeneration.from_pretrained('t5-small')
tokenizer_t5_small = T5Tokenizer.from_pretrained('t5-small')

model_t5_base = T5ForConditionalGeneration.from_pretrained('t5-base')
tokenizer_t5_base = T5Tokenizer.from_pretrained('t5-base')

model_t5_large = T5ForConditionalGeneration.from_pretrained('t5-large')
tokenizer_t5_large = T5Tokenizer.from_pretrained('t5-large')

model_bart = BartForConditionalGeneration.from_pretrained('facebook/bart-large-cnn')
tokenizer_bart = BartTokenizer.from_pretrained('facebook/bart-large-cnn')

model_pegasus = PegasusForConditionalGeneration.from_pretrained('google/pegasus-xsum')
tokenizer_pegasus = PegasusTokenizer.from_pretrained('google/pegasus-xsum')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        model_choice = request.form['model_choice']

        if model_choice == 't5-small':
            model = model_t5_small
            tokenizer = tokenizer_t5_small
        elif model_choice == 't5-base':
            model = model_t5_base
            tokenizer = tokenizer_t5_base
        elif model_choice == 't5-large':
            model = model_t5_large
            tokenizer = tokenizer_t5_large
        elif model_choice == 'bart':
            model = model_bart
            tokenizer = tokenizer_bart
        elif model_choice == 'pegasus':
            model = model_pegasus
            tokenizer = tokenizer_pegasus
        else:
            return render_template('index.html', summary="Invalid model selected.")

        inputs = tokenizer.encode("summarize: " + text, return_tensors="pt", truncation=True, max_length=512)
        summary_ids = model.generate(inputs, max_length=150, min_length=40, length_penalty=2.0, num_beams=4, early_stopping=True)
        summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

        return render_template('index.html', summary=summary)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
