from flask import Flask, render_template, request
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)

my_email = 'python.testing.br@gmail.com'
password = 'Pass4321'


def send_email(name, email, phone, message):
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        sender = to = 'brett.t.redd@gmail.com'
        msg = MIMEText(f'Name: {name}\nEmail: {email}\nPhone: {phone}\n\nMessage:\n{message}')
        msg['Subject'] = 'Blog Inquiry'
        msg['From'] = my_email
        msg['To'] = to
        connection.sendmail(sender, [to], msg.as_string())


@app.route('/')
def home_page():
    return render_template('index.html')


@app.route('/Contact-Me', methods=['GET', 'POST'])
def contact_me():
    if request.method == 'POST':
        data = request.form
        print(f"{data['name']}\n{data['cell']}\n{data['email']}\n{data['message']}")
        send_email(data['name'], data['cell'], data['email'], data['message'])
        return render_template('Contact-Me.html', success=True)
    return render_template('Contact-Me.html', success=False)


@app.route('/My-Hobbies')
def my_hobbies():
    return render_template('My-Hobbies.html')


if __name__ == '__main__':
    # Run the app in debug mode to auto-reload
    app.run(debug=True)
