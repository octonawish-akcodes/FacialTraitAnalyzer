# age_gender_detection_app/views.py
import cv2
import os
import numpy as np
from django.shortcuts import render
from .forms import UploadImageForm
from .models import UploadedImage
from django.conf import settings

def highlightFace(net, frame, conf_threshold=0.7):
    frameOpencvDnn = frame.copy()
    frameHeight = frameOpencvDnn.shape[0]
    frameWidth = frameOpencvDnn.shape[1]
    blob = cv2.dnn.blobFromImage(frameOpencvDnn, 1.0, (300, 300), [104, 117, 123], True, False)

    net.setInput(blob)
    detections = net.forward()
    faceBoxes = []
    for i in range(detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_threshold:
            x1 = int(detections[0, 0, i, 3] * frameWidth)
            y1 = int(detections[0, 0, i, 4] * frameHeight)
            x2 = int(detections[0, 0, i, 5] * frameWidth)
            y2 = int(detections[0, 0, i, 6] * frameHeight)
            faceBoxes.append([x1, y1, x2, y2])
            cv2.rectangle(frameOpencvDnn, (x1, y1), (x2, y2), (0, 255, 0), int(round(frameHeight / 150)), 8)
    return frameOpencvDnn, faceBoxes

def detect_age_gender(image_path):
    faceProto = os.path.join(os.path.dirname(__file__), "opencv_face_detector.pbtxt")
    faceModel = os.path.join(os.path.dirname(__file__), "opencv_face_detector_uint8.pb")
    ageProto = os.path.join(os.path.dirname(__file__), "age_deploy.prototxt")
    ageModel = os.path.join(os.path.dirname(__file__), "age_net.caffemodel")
    genderProto = os.path.join(os.path.dirname(__file__), "gender_deploy.prototxt")
    genderModel = os.path.join(os.path.dirname(__file__), "gender_net.caffemodel")

    MODEL_MEAN_VALUES = (78.4263377603, 87.7689143744, 114.895847746)
    ageList = ['(0-2)', '(4-6)', '(8-12)', '(15-20)', '(25-32)', '(38-43)', '(48-53)', '(60-100)']
    genderList = ['Male', 'Female']

    faceNet = cv2.dnn.readNet(faceModel, faceProto)
    ageNet = cv2.dnn.readNet(ageModel, ageProto)
    genderNet = cv2.dnn.readNet(genderModel, genderProto)

    frame = cv2.imread(image_path)
    resultImg, faceBoxes = highlightFace(faceNet, frame)
    if not faceBoxes:
        print("No face detected")

    for faceBox in faceBoxes:
        face = frame[max(0, faceBox[1] - 20): min(faceBox[3] + 20, frame.shape[0] - 1),
               max(0, faceBox[0] - 20): min(faceBox[2] + 20, frame.shape[1] - 1)]

        blob = cv2.dnn.blobFromImage(face, 1.0, (227, 227), MODEL_MEAN_VALUES, swapRB=False)
        genderNet.setInput(blob)
        genderPreds = genderNet.forward()
        gender = genderList[genderPreds[0].argmax()]
        print(f'Gender: {gender}')

        ageNet.setInput(blob)
        agePreds = ageNet.forward()
        age = ageList[agePreds[0].argmax()]
        print(f'Age: {age[1:-1]} years')

        cv2.putText(resultImg, f'{gender}, {age}', (faceBox[0], faceBox[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.8,
                    (0, 255, 255), 2, cv2.LINE_AA)
    result_path = 'uploads/result.png'
    cv2.imwrite(os.path.join(settings.MEDIA_ROOT, result_path), resultImg)

    # Construct the full URL to the detected image using MEDIA_URL
    result_url = os.path.join(settings.MEDIA_URL, result_path)
    return {'result_path': result_url, 'gender': gender, 'age': age[1:-1]}

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded image
            uploaded_image = form.save()

            # Perform age and gender detection
            image_path = uploaded_image.image.path
            try:
                result = detect_age_gender(image_path)
            except FileNotFoundError as e:
                context = {'form': form, 'error_message': str(e)}
                return render(request, 'upload_image.html', context)

            # Pass the result to the template
            context = {'result': result}
            return render(request, 'result.html', context)
    else:
        form = UploadImageForm()

    context = {'form': form}
    return render(request, 'upload_image.html', context)
