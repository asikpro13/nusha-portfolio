import json

from flask import Flask, render_template, request, redirect
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

application = Flask(__name__)


@application.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'GET':
        return render_template('index.html')
    elif request.method == "POST":
        name = request.form.get('name')
        mail = request.form.get('email')
        contact = request.form.get('phone')
        message = request.form.get('msg')

        fromaddr = "account.pochtovy@mail.ru"
        toaddr = "nusa0310@yandex.ru"
        # mypass = "copsig-zaFsyz-mujra5"
        mypass = "NWaem5MMbv1c4LsFX2Ud"

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = name

        body = f"""{mail}\n{contact}\n{message}"""
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        server.login(fromaddr, mypass)
        server.sendmail(fromaddr, toaddr, text)
        return json.dumps({'status': '200'})
    return render_template('Страница-1.html')


@application.route('/Страница-1.html', methods=['GET', 'POST'])
def page1():
    if request.method == 'GET':
        return render_template('Страница-1.html')
    elif request.method == "POST":
        name = request.form.get('name')
        mail = request.form.get('email')
        contact = request.form.get('phone')
        message = request.form.get('msg')

        fromaddr = "account.pochtovy@mail.ru"
        # toaddr = "nusa0310@yandex.ru"
        toaddr = "nusa0310@yandex.ru"
        # mypass = "copsig-zaFsyz-mujra5"
        mypass = "NWaem5MMbv1c4LsFX2Ud"

        msg = MIMEMultipart()
        msg['From'] = fromaddr
        msg['To'] = toaddr
        msg['Subject'] = name

        body = f"""{mail}\n{contact}\n{message}"""
        msg.attach(MIMEText(body, 'plain'))
        text = msg.as_string()
        server = smtplib.SMTP_SSL('smtp.mail.ru', 465)
        server.login(fromaddr, mypass)
        server.sendmail(fromaddr, toaddr, text)
        return json.dumps({'status': '200'})
    return render_template('Страница-1.html')


@application.route('/Страница-2.html')
def page2():
    return render_template('Страница-2.html')


@application.route('/Страница-3.html')
def page3():
    return render_template('Страница-3.html')


@application.route('/Страница-4.html')
def page4():
    return render_template('Страница-4.html')


if __name__ == '__main__':
    application.run(host='0.0.0.0')
