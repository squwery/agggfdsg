from flask import Flask, render_template, request, redirect, url_for
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

app = Flask(__name__)

# Настройки электронной почты
EMAIL_ADDRESS = 'vadekqwe@gmail.com'  # Ваш email
EMAIL_PASSWORD = 'qvpu ztmo ynpx ffjm'

def send_email(name, email, message):
    # Настройка сообщения
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = EMAIL_ADDRESS
    msg['Subject'] = 'Новая заявка с сайта'

    body = f'Имя: {name}\nEmail: {email}\nСообщение: {message}'
    msg.attach(MIMEText(body, 'plain'))

    # Отправка письма
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)


@app.route('/', methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        # Отправка email
        send_email(name, email, message)

        return redirect(url_for('success'))
    return render_template('form.html')


@app.route('/success')
def success():
    return 'Форма успешно отправлена!'


if __name__ == '__main__':
    app.run(debug=True)