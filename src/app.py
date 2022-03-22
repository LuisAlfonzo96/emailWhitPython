from apscheduler.schedulers.background import BackgroundScheduler
from flask import Flask, request
from datetime import datetime, timedelta
import sendEmail

def sensor():
    if datetime.today().strftime('%A')== 'Tuesday':
        sendEmail.emailCheck("luis.rocca96@gmail.com,josees_84@hotmail.com","Reporte semanal ",(datetime.today() - timedelta(days=7)).strftime('%Y-%m-%d %H:%M:%S'), datetime.today().strftime('%Y-%m-%d %H:%M:%S'))
        print("ok")
    else:
        print("ok no")

sched = BackgroundScheduler(daemon=True)
sched.add_job(sensor,'interval',hours=24)
sched.start()

app = Flask(__name__)

@app.route('/email', methods=['POST'])
def sendEmailR():
    email = request.json['email']
    message = request.json['message']
    subject = request.json['subject']
    sendEmail.emailCheck(email,subject)
    return "email"

if __name__ == "__main__":
    app.run()
