import os
from flask import Flask,request,redirect,url_for,flash
from werkzeug.utils import secure_filename
from flask import render_template
from keras.models import load_model
import sys,keras
import numpy as np
from PIL import Image

classes = ['monkey','boar','crow']
num_classes = len(classes)
image_size = 50

UPLOAD_FOLDER = './uploaded_file'
ALLOWED_EXTENSIONS = set(['png','jpg','gif'])

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
#app.config['SEND_FILE_MAX_AGE_DEFAULT']=0

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/',methods=['GET','POST'])
def return_topPage():
    return render_template('index.html')

@app.route('/contact',methods=['GET','POST'])
def return_contactPage():
    if request.method == 'POST':
        result = request.form
        return render_template('confirm.html') 

    return render_template('contact.html')

@app.route('/result',methods=['GET','POST'])
def return_resultPage():
    return render_template('result.html')


@app.route('/animal_classifier',methods=['GET','POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file found')
            return redirect(request.url)

        file = request.files['file']

        if file.filename =='':
            flash('No file found')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
            #return redirect(url_for('uploaded_file',filename=filename))
            filepath = os.path.join(app.config['UPLOAD_FOLDER'],filename)
    
            model = load_model('./models/animal_cnn_aug_Mon Jul 13 00:47:39 2020.h')

            image = Image.open(filepath)
            image = image.convert('RGB')
            image = image.resize((image_size,image_size))
            data = np.asarray(image)
            _x = []
            _x.append(data)
            _x = np.array(_x) 
            
            result = model.predict([_x])[0]
            predicted = result.argmax()
            percentage = int(result[predicted] * 100)
            
            return 'The image may be {}.  In {}%'.format(classes[predicted],str(percentage))

    return render_template('animal_classifier.html')

from flask import send_from_directory
@app.route('/uploaded_file/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'],filename)    

@app.route('/playball',methods=['GET','POST'])
def return_playball():
    return render_template('play_with_ball.html')

@app.route('/idea',methods=['GET','POST'])
def return_idea():
    return 'idea page'

@app.route('/test',methods=['GET','POST'])
def return_test_page():
    return render_template('test_page.html')

