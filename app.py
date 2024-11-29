import os
import uuid
from flask import Flask, request, redirect, url_for, send_from_directory, render_template_string

app = Flask(__name__)

# Настройки папки для загрузки файлов
UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Импорт HTML-шаблона из отдельного файла
from templates import HTML_TEMPLATE

# Главная страница для загрузки файлов
@app.route("/", methods=["GET", "POST"])
def upload_file():
    url = None
    if request.method == "POST":
        if "file" not in request.files:
            return "Ошибка: файл не выбран.", 400
        file = request.files["file"]
        if file.filename == "":
            return "Ошибка: файл не выбран.", 400
        if file:
            # Генерация уникального имени файла
            filename = f"{uuid.uuid4().hex}_{file.filename}"
            filepath = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            file.save(filepath)
            # Формирование ссылки на загруженный файл
            url = url_for("uploaded_file", filename=filename, _external=True)
    return render_template_string(HTML_TEMPLATE, url=url)

# Отдача загруженных файлов
@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOAD_FOLDER"], filename)

# Запуск приложения
if __name__ == "__main__":
    app.run(debug=True)
