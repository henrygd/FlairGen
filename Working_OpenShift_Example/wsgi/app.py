from flask import Flask, request, render_template
import inlineflair

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('form.html')


@app.route('/code', methods=['POST'])
def convert():
    if request.form['mode'] == "normal":
        output = inlineflair.flairgen(request.form['comment'])
    elif request.form['mode'] == "safe":
        output = inlineflair.flairgen_safe(request.form['comment'])
    return render_template('code.html', output=output)

if __name__ == '__main__':
    app.run()
