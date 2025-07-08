from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'super-secret-key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/article')
def article():
    return render_template('article.html')

if __name__ == '__main__':
    app.run(debug=True)
