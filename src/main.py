from flask import Flask, render_template, request, redirect, url_for
import os
from utils import process_image  # Importa la función de procesamiento de imagen desde utils.py

app = Flask(__name__, template_folder='/home/josueg/Documentos/vision_project/templates')

# Configuración de las carpetas de carga y salida
app.config['UPLOAD_FOLDER'] = os.path.join('src/static', 'input')
app.config['OUTPUT_FOLDER'] = os.path.join('src/static', 'output')

# Asegura que las carpetas de carga y salida existan
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['OUTPUT_FOLDER'], exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Maneja la carga de archivos y la selección del modelo
        file = request.files.get('input_file')
        model = request.form.get('model')
        if file and model:
            filename = file.filename
            input_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            output_path = os.path.join(app.config['OUTPUT_FOLDER'], filename)
            file.save(input_path)

            # Procesa la imagen con la función importada de utils.py
            process_image(input_path, output_path, model)
            return redirect(url_for('results', filename=filename))
    return render_template('index.html')

@app.route('/results/<filename>')
def results(filename):
    output_url = url_for('static', filename=f'output/{filename}')
    return render_template('results.html', output_image=output_url)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
