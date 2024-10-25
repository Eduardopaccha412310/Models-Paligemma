from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
import base64
from PIL import Image
from Scripts import Paligema

def init_app(app):
    UPLOAD_FOLDER = 'uploads/'
    ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

    if not os.path.exists(UPLOAD_FOLDER):
        os.makedirs(UPLOAD_FOLDER)

    def allowed_file(filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @app.route('/')
    def index():
        return render_template('index.html')


    @app.route('/paligemma', methods=['GET', 'POST'])
    def paligemma(): 
        result = None
        if request.method == 'POST':
            text_input = request.form.get('text_input', '')
            if not text_input:
                print("no ingreso el texto")
                flash('No se ingresó ningún texto')
                return redirect(request.url)
            
            if 'image' not in request.files:
                print("no hay imágen")
                flash('No se subió ninguna imagen')
                return redirect(request.url)
            file = request.files['image']
            if file.filename == '':
                flash('No se seleccionó ninguna imagen')
                return redirect(request.url)
            if file and allowed_file(file.filename):
                print("Estoy en funcion Gemma")
                filename = secure_filename(file.filename)
                filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
                file.save(filepath)
                
                result = Paligemma.process_image(filepath, text_input)
                flash('Imagen y texto procesados correctamente')
        return render_template('Paligemma.html', result=result)


    @app.route('/paligemmacamara', methods=['GET', 'POST'])
    def paligemmacamara():
        
        if request.method == 'POST':
            # Procesar imagen desde la cámara
            text_input = request.form.get('text_input', '')
            image_data = request.form.get('image_data', '')

            if not text_input or not image_data:
                flash('No se ingresó texto o imagen')
                return redirect(request.url)

            # Decodificar la imagen
            image_data = image_data.split(",")[1]  # Quitar el encabezado "data:image/png;base64,"
            image_bytes = base64.b64decode(image_data)
            image = Image.open(io.BytesIO(image_bytes))

            # Aquí puedes procesar la imagen y el texto como desees
            # Paligemma.process_image(image, text_input)

            flash('Imagen y texto procesados correctamente')
            return redirect(url_for('paligemmacamara'))

        return render_template('PaligemmaCamara.html')

