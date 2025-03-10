from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    return render_template('dashboard.html')

@app.route('/image-captioning')
def image_captioning():
    return render_template('image_captioning.html')

@app.route('/object-detection')
def object_detection():
    return render_template('object_detection.html')

@app.route('/about')
def about():
    return "About Page"

@app.route('/contact')
def contact():
    return "Contact Page"

if __name__ == '__main__':
    app.run(debug=True)
