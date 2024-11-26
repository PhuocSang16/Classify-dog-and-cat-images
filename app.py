import os
from flask import Flask, request, render_template, redirect
from scripts.predict import predict_image  # Import hàm predict từ scripts/predict.py

# Khởi tạo Flask app
app = Flask(__name__)

# Đường dẫn lưu ảnh upload
UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Route chính (Giao diện upload)
@app.route('/')
def index():
    return render_template('index.html')

# Route xử lý upload và dự đoán
@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        return redirect(request.url)
    if file:
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)  # Lưu ảnh
        result, inference_time = predict_image(file_path)  # Dự đoán ảnh và đo thời gian inference
        return render_template('index.html', uploaded_image=file_path, result=result, inference_time=inference_time)

if __name__ == '__main__':
    app.run(debug=True)
