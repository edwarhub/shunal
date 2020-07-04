import smtplib
import mimetypes

from datetime import datetime
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart

# Mail variables
OrgMail='iot2020unal@gmail.com'
OrgPassword='S$23trPW2&tgmU'
now = datetime.now()

def sendMail(emailDst, dirPhoto="defaultImagen.jpeg"):
    """
    Send message to the destination email, from the default email
    The input parameters are the destination email and the image path
    """

    print("sending email ...")
    #  Object Multipart
    msg = MIMEMultipart()
    msg['From']=OrgMail
    msg['To']=emailDst
    msg['Subject']="Alerta de Seguridad - Posible intruso"
    msg.attach(MIMEText( 'Hoy a las {}:{} horas se detecto un posible intruso por favor tomar las medida necesarias.'.format(now.hour, now.minute)))

    # Attach Image
    part = MIMEApplication(open(dirPhoto,"rb").read())
    part.add_header('Content-Disposition', 'attachment', filename="possibleIntruder."+splitfilename(dirPhoto))
    msg.attach(part)

    #Authentication
    mailServer = smtplib.SMTP('smtp.gmail.com',587)
    mailServer.ehlo()
    mailServer.starttls()
    mailServer.ehlo()
    mailServer.login(OrgMail,OrgPassword)
    #send email
    mailServer.sendmail(OrgMail,emailDst, msg.as_string())

    mailServer.close()
    print("email has been sent successfully")

def splitfilename(filename):
    """
    get file extension
    """
    sname=""
    sext=""
    i=filename.rfind(".")
    if(i!=0):
        n=len(filename)
        j=n-i-1
        sname=filename[0:i]
        sext=filename[-j:]
    return sext
