import cv2 as cv

def process(input_path, output_path):
    # Cargar la imagen de entrada
    image = cv.imread(input_path)

    # Inicializar el detector de rostros YuNet
    model_path = 'models/face_detection_yunet/face_detection_yunet_2023mar.onnx'
    detector = cv.FaceDetectorYN.create(
        model=model_path,
        config='',
        input_size=(image.shape[1], image.shape[0]),
        score_threshold=0.9,
        nms_threshold=0.3,
        top_k=5000,
        backend_id=cv.dnn.DNN_BACKEND_OPENCV,
        target_id=cv.dnn.DNN_TARGET_CPU
    )

    # Detección de rostros
    faces = detector.detect(image)[1]

    # Dibujar cuadros delimitadores para cada rostro detectado
    if faces is not None:
        for face in faces:
            bbox = face[:4].astype(int)
            x, y, w, h = bbox
            cv.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)

    # Guardar la imagen con los rostros detectados
    cv.imwrite(output_path, image)
