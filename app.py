# import libraries
from flask import Flask, render_template, request
from googletrans import Translator
import openai
import yapf

# create a Flask app
app = Flask(__name__)
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/getcode',methods=["POST","GET"])
def getcode():
    if request.method == "POST":
        result = request.form.get('code')

        # Set up the GPT-3 API
        openai.api_key = "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"

        model_engine = "text-davinci-002"

        completions = openai.Completion.create(
            engine=model_engine,
            prompt=result,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5
        )
        code = completions.choices[0].text
        # Postprocess the summary
        code = code.strip()
        lines = code.split('\n')

        # Iterate over the list of lines and append the string you want to add to the end of each line
        modified_lines = []
        for line in lines:
            modified_lines.append(line + ' <br>')

        # Join the modified lines back into a single string
        modified_contents = '\n'.join(modified_lines)
        return render_template("index.html",code=modified_contents)
        # Save or display the summary
    

if __name__ == '__main__':
    app.run(debug=False,host="0.0.0.0")