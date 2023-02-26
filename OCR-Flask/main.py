import flask
from flask import Flask, render_template,request
import pytesseract
import PIL
from PIL import Image



app = Flask(__name__)

app.jinja_env.trim_blocks = True
app.jinja_env.lstrip_blocks = True

@app.route("/")
def index():
    return render_template("index.html")
    

@app.route("/upload", methods = ["POST"])
def upload():
    if 'image' not in request.files:
        return 'No file uploaded', 400
    
    file = request.files['image']
    img = Image.open(file)
    ocr_result = pytesseract.image_to_string(img)
    
    if file.mimetype.startswith('image/'):
        image = Image.open(file)
        image_path = 'static/images/' + file.filename
        image.save(image_path)
        # return ocr_result, 200
        return render_template('result2.html', result=ocr_result, image_url=image_path)
    else:
        return 'File is not an image', 400


if __name__ == "__main__":
    app.run(debug = True)