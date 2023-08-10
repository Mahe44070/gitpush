from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    target_lang = request.form['target_lang']
    translator = Translator()
    translated_text = translator.translate(text, dest=target_lang).text
    return render_template('translate.html', text=text, target_lang=target_lang, translated_text=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
