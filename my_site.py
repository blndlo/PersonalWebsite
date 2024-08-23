from flask import Flask, render_template, url_for
app = Flask(__name__, template_folder='templates', static_folder='static')
application = app

@app.route('/')
@app.route('/about')
def about():
    return render_template('index.html')

@app.route('/resume')
def resume():
    return render_template('resume.html')

@app.route('/portfolio')
def portfolio():
    return render_template('portfolio.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
