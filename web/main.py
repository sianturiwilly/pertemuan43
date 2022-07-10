from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return "Ini halaman home"

@app.route('/prediksi', methods=('GET', 'POST'))
def prediksi():
    if request.method == 'POST':
        sepal_length = request.form['sl']
        sepal_width = request.form['sw']
        petal_length = request.form['pl']
        petal_width = request.form['pw']

        return f"SL = {sepal_length}, SW = {sepal_width}, PL = {petal_length}, PW = {petal_width}"

    return render_template('predict_form.html')

if __name__ == "__main__":
    app.run(debug=True)