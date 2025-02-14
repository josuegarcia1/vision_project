import cv2 as cv
import numpy as np

def process(input_path, output_path):
    # Cargar la imagen de entrada
    image = cv.imread(input_path)

    # Inicializar el estimador de pose humana Lite-HRNet
    model_path = 'models/pose_estimation_mediapipe/pose_estimation_mediapipi_2023mar.onnx'
    pose_estimator = cv.HumanPoseEstimator.create(model_path, '')

    # Estimación de la pose
    pose = pose_estimator.estimate(image)

    # Dibujar los puntos clave de la pose
    for point in pose:
        x, y = point
        if x >= 0 and y >= 0:
            cv.circle(image, (int(x), int(y)), 5, (0, 255, 0), -1)

    # Guardar la imagen con los resultados de la estimación de pose
    cv.imwrite(output_path, image)
