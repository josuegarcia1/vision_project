from model_handlers.face_detection import process as process_face_detection
from model_handlers.face_recognition import process as process_face_recognition
from model_handlers.pose_estimation import process as process_pose_estimation

def process_image(input_path, output_path, model):
    """
    Procesa una imagen según el modelo especificado y guarda el resultado.

    Parámetros:
    - input_path: Ruta de la imagen de entrada.
    - output_path: Ruta donde se guardará la imagen procesada.
    - model: Modelo a utilizar ('face_detection', 'face_recognition', 'human_pose_estimation').
    """
    if model == 'face_detection':
        process_face_detection(input_path, output_path)
    elif model == 'face_recognition':
        process_face_recognition(input_path, output_path)
    elif model == 'pose_estimation':
        process_pose_estimation(input_path, output_path)
    else:
        raise ValueError(f"Modelo '{model}' no reconocido")
