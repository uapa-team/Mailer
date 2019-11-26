import csv
import smtplib
import ssl
import getpass
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from_name = 'Daniel Alejandro Escobar Prieto'
from_addresse_mail = input('Email: ') + '@unal.edu.co'
password = getpass.getpass(prompt='Password: ', stream=None)
context = ssl.create_default_context()
with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    server.login(from_addresse_mail, password)
    with open("contacts_file.csv") as file:
        reader = csv.reader(file)
        next(reader)  # Skip header row
        for name, email in reader:
            message = MIMEMultipart("alternative")
            message["Subject"] = "Encuesta de Satisfacción - Vicedecanatura Académica"
            message["From"] = from_name
            message["To"] = email
            html = """\
                <html>
                    <body>
                        <div dir="ltr"><font face="georgia, serif" size="4" color="#000000">Cordial Saludo,</font><div><font size="4" face="georgia, serif" color="#000000"><br></font></div><div><font size="4" face="georgia, serif" color="#000000">Respetado(a):</font></div><div><font size="4" face="georgia, serif" color="#000000"><br></font></div><div><font size="4" face="georgia, serif">{name}</font></div><div><font size="4" face="georgia, serif"><br></font></div><div><div style="color:rgb(80,0,80)"><div><font size="4" face="georgia, serif" color="#000000">En procura de la mejora continua de nuestros procesos la Vicedecanatura Académica lo invita a participar en la encuesta anual de satisfacción al usuario. Su opinión es importante para nosotros y contribuye a fortalecer la calidad de los servicios prestados.<br></font></div><div><font size="4" face="georgia, serif" color="#000000"><br></font></div><div><div style="text-align:center"><font face="georgia, serif" size="4" color="#000000"><a href="https://forms.gle/BvqSXEpCnYLMSvsr7" target="_blank" data-saferedirecturl="https://www.google.com/url?q=https://forms.gle/BvqSXEpCnYLMSvsr7&amp;source=gmail&amp;ust=1574868620257000&amp;usg=AFQjCNGWXCxENoIygTSpIqoX2e_I307HNA"><img src="https://lh6.googleusercontent.com/heh2RnWTuZQDW-TbNrqJKkgCiFxI76Wbdu4Ew2eZ1hS2oFiFsp9XaE0xd4ulURFSfaXp7tAya4Pnx-1ULtI5gUelTnFgO_OgzqhvqGHEYMbDIfh9X9_EZo8Vw_AW=w1921" alt="Encuesta" width="704" height="247" style="margin-right:0px" data-image-whitelisted="" class="CToWUd"></a><br></font></div></div><div><font size="4" face="georgia, serif" color="#000000"><br></font></div><div><font size="4" face="georgia, serif" color="#000000">Diligencie el formulario y participe en la rifa de diferentes obsequios.</font></div></div></div><div><div dir="ltr" data-smartmail="gmail_signature"><div dir="ltr"><div><br></div><div><img src="https://ci6.googleusercontent.com/proxy/-E3sTYONYlN5HTLD0QBRHoVeWled5kmvqfNe6IYtyad8PxaexYZj2EtAPpozN4yZkSPcRbCo5Z9AICHe5Hg-7cQ3EtS4nJ5wNX0VscEQAVDyVjw93xxt7d8QOdppW3fPn4JpXDETDJj7h9swI7BTo39lvTKKw1Gvczb8koh0vhuX1q6SGiPEyVD1iUGKXyLewaoBlarZ51x28LYWAZS5I8AZVf_1gMqxkyJRCMO4hH4=s0-d-e1-ft#https://firebasestorage.googleapis.com/v0/b/tutoriaspg.appspot.com/o/Firma%20Ingeniero%20Jes%C3%BAs.PNG?alt=media&token=d50b25f2-04d2-4ad9-812e-c4ab040be635" width="420" height="170" class="CToWUd a6T" tabindex="0"><div class="yj6qo"></div><div class="a6S adL" dir="ltr" style="opacity: 0.01;"><div id=":1j2" class="T-I J-J5-Ji aQv T-I-ax7 L3 a5q" title="Download" role="button" tabindex="0" aria-label="Download attachment " data-tooltip-class="a1V"><div class="aSK J-J5-Ji aYr"></div></div></div><div class="adL"><br></div></div></div></div></div></div>
                    </body>
                </html>
            """
            message.attach(MIMEText(html.format(name=name), "html"))
            server.sendmail(
                from_name,
                email,
                message.as_string()
            )
