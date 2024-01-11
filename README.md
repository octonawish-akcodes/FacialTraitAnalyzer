# FacialTraitAnalyzer (Age and Gender Detection Web App) 👦👩🔍

## Overview:
FaceTraitsAnalyzer is a Django web application designed for age and gender detection in images. Leveraging the power of OpenCV and pre-trained models, this application allows users to upload images and receive real-time analysis of facial features. This is a Django web application that performs age and gender detection on uploaded images using OpenCV and pre-trained models.

## Key Features:

- **Age Detection:** Accurately estimates the age range of individuals in uploaded images. 🎂
- **Gender Detection:** Identifies the gender of faces with high precision. ♂️♀️
- **User-Friendly Interface:** Intuitive web interface for seamless image upload and result presentation. 🌐
- **Visual Insights:** Presents detection results overlaid on the uploaded images for a comprehensive analysis. 📊

![image](https://github.com/octonawish-akcodes/FacialTraitAnalyzer/assets/76171953/48156218-fcb4-4914-9d45-ad5fbdf6b92e)

![Screenshot 2023-12-30 132324](https://github.com/octonawish-akcodes/FacialTraitAnalyzer/assets/76171953/3003e559-9b7a-44ed-9e47-0e760e9e6f5e)

## Project Structure 📂

```plaintext
.
├── Dockerfile
├── README.md
├── age_gender_detection_app
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── admin.cpython-310.pyc
│   │   ├── apps.cpython-310.pyc
│   │   ├── forms.cpython-310.pyc
│   │   ├── models.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── views.cpython-310.pyc
│   ├── admin.py
│   ├── age_deploy.prototxt
│   ├── age_net.caffemodel
│   ├── apps.py
│   ├── forms.py
│   ├── gender_deploy.prototxt
│   ├── gender_net.caffemodel
│   ├── migrations
│   │   ├── 0001_initial.py
│   │   ├── __init__.py
│   │   └── __pycache__
│   │       ├── 0001_initial.cpython-310.pyc
│   │       └── __init__.cpython-310.pyc
│   ├── models.py
│   ├── opencv_face_detector.pbtxt
│   ├── opencv_face_detector_uint8.pb
│   ├── templates
│   │   ├── result.html
│   │   └── upload_image.html
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── age_gender_detection_project
│   ├── __init__.py
│   ├── __pycache__
│   │   ├── __init__.cpython-310.pyc
│   │   ├── settings.cpython-310.pyc
│   │   ├── urls.cpython-310.pyc
│   │   └── wsgi.cpython-310.pyc
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── compose.yaml
├── db.sqlite3
├── manage.py
├── media
│   └── uploads
│       ├── 1487718277-screen-shot-2017-02-21-at-60424-pm.png
│       ├── Screenshot_2023-12-26_204504.png
│       ├── istockphoto-1147066751-612x612_h4qn96t.jpg
│       └── result.png
└── requirements.txt
```

## Prerequisites 🛠️

- Python 3
- Django
- OpenCV

## Getting Started 🚀

1. **Clone the repository:**

   ```bash
   git clone https://github.com/octonawish-akcodes/FacialTraitAnalyzer.git
   ```

2. **Install the required dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Apply migrations:**

   ```bash
   python manage.py migrate
   ```

4. **Run the development server:**

   ```bash
   python manage.py runserver
   ```

   The app should be accessible at [http://127.0.0.1:8000/age_gender/](http://127.0.0.1:8000/age_gender/).
   > My 8000 port was busy so I used 8001.

## Docker Usage Section 🐳

1. **Pull the Docker image from Docker Hub:**

   ```bash
   docker pull abhidocker12/age_gender_detection:latest
   ```

2. **Run the Docker container:**

   ```bash
   docker run -p 8000:8000 abhidocker12/age_gender_detection:latest
   ```

   Access the Django application in your web browser at http://localhost:8000/age_gender/upload/.

## Usage 🖼️

1. **Visit [http://127.0.0.1:8000/age_gender/upload/](http://127.0.0.1:8000/age_gender/upload/) in your web browser.**

2. **Upload an image using the provided form.**

3. **Click "Submit" to perform age and gender detection.**

4. **View the detection result, including the detected image, gender, and age.**

