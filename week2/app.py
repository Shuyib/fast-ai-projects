import os
import base64
from io import BytesIO
from fastai import *
from fastai.vision import *
from flask import Flask, jsonify, request, render_template
from werkzeug.exceptions import BadRequest


# fastai.defaults.device = torch.device('cpu')

def evaluate_image(img) -> str:
	pred_class, pred_idx, outputs = trained_model.predict(img)
	return pred_class

def load_model():
	path = '/floyd/home'
	classes = ['eosinophil', 'lymphocyte', 'monocyte', 'neutrophil']
	data = ImageDataBunch.single_from_classes(path, classes, tfms=get_transforms(), size=200).normalize(imagenet_stats)
	learn = create_cnn(data, models.resnet50)
	learn.load('stage-5')
	return learn

app = Flask(__name__)
app.config['DEBUG'] = False
trained_model = load_model()

@app.route('/', methods=['GET'])
def index():
    """Render the app"""
    return render_template('serving_template.html')

@app.route('/image', methods=['POST'])
def eval_image():
    """Evaluate the image!"""
    input_file = request.files.get('file')
    if not input_file:
        return BadRequest("File is not present in the request")
    if input_file.filename == '':
        return BadRequest("Filename is not present in the request")
    if not input_file.filename.lower().endswith(('.jpg', '.jpeg', '.png')):
        return BadRequest("Invalid file type")
    input_buffer = BytesIO()
    input_file.save(input_buffer)
    
    guess = evaluate_image(open_image(input_buffer))
    return jsonify({
        'guess': guess
    })

if __name__ == "__main__":
	app.run(host='0.0.0.0', threaded=False)
