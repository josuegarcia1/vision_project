import cv2 as cv
import numpy as np

def process(input_path, output_path):
    # Cargar la imagen de entrada
    image = cv.imread(input_path)

    # Inicializar el reconocedor facial SFace
    model_path = 'models/face_recognition_sface/face_recognition_sface_2021dec.onnx'
    recognizer = cv.FaceRecognizerSF.create(model_path, '')

    # Inicializar el detector de rostros YuNet
    detector = cv.FaceDetectorYN.create(
        model='models/face_detection_yunet/face_detection_yunet.onnx',
        config='',
        input_size=(image.shape[1], image.shape[0]),
        score_threshold=0.9,
        nms_threshold=0.3,
        top_k=5000,
        backend_id=cv.dnn.DNN_BACKEND_OPENCV,
        target_id=cv.dnn.DNN_TARGET_CPU
    )
    faces = detector.detect(image)[1]

    # Dibujar cuadros delimitadores y realizar reconocimiento facial
    if faces is not None:
        for face in faces:
            bbox = face[:4].astype(int)
            x, y, w, h = bbox
            face_roi = image[y:y+h, x:x+w]
            # Realizar el reconocimiento facial
            label, confidence = recognizer.predict(face_roi)
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv.putText(image, f'ID: {label} Conf: {confidence:.2f}', (x, y - 10),
                       cv.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Guardar la imagen con los resultados del reconocimiento facial
    cv.imwrite(output_path, image)
