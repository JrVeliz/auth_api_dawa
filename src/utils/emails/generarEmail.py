import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from ..general.config import Parametros

class generarEmail:
    @staticmethod
    def generarEmailSignup(nombre, cedula, correo_personal, correoInstitucional):
        remitente=Parametros.CORREO
        destinatario= correo_personal
        asunto= 'Creación de nueva cuenta institucional'
        
        # Cuerpo HTML
        cuerpo_html = f"""
        <html>
            <body>
                <p>Hola {nombre} xd,</p>
                <p>Nose si este mensaje llegue pero ahí está tu correo institucional, contraseña y usuario para el SIUG.</p>
                <p>*hace un backflip y se va*</p>
                <p>Correo Institucional: {correoInstitucional}</p>
                <p>Contraseña Institucional: {cedula}</p>
                <p>Usuario SIUG: {cedula}</p>
                <p>Contraseña SIUG: '{cedula}'</p>
                <p>Ayuda, no he dormido bien y veo borroso :D</p>
            </body>
        </html>
        """
        msg=MIMEMultipart()
        msg['Subject']=asunto
        msg['From']=remitente
        msg['To']=destinatario
        msg.attach(MIMEText(cuerpo_html,'html'))

        server =smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(remitente, Parametros.PASS_CORREO)
        server.sendmail(remitente,destinatario,msg.as_string())

        server.quit()

    @staticmethod
    def generarEmailForgotPass(correo_institucional,token):
        remitente=Parametros.CORREO
        destinatario= correo_institucional
        asunto= 'Recuperación de Cuenta'
        
        # Cuerpo HTML
        cuerpo_html = f"""
        <html>
            <body>
                <h1>TOKEN PARA LA VALIDACION DE RECUPERACION DE CUENTA</h1>
                <p>Nose si este mensaje llegue pero ahí está tu token, pegalo en la app.</p>
                <p>*hace un backflip y se va*</p>
                <p>{token}</p>
                <p>Ayuda, no he dormido bien y veo borroso :D</p>
            </body>
        </html>
        """
        msg=MIMEMultipart()
        msg['Subject']=asunto
        msg['From']=remitente
        msg['To']=destinatario
        msg.attach(MIMEText(cuerpo_html,'html'))

        server =smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(remitente, Parametros.PASS_CORREO)
        server.sendmail(remitente,destinatario,msg.as_string())

        server.quit()