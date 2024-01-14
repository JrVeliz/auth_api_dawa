from ...utils.general.logs import HandleLogs
from ...utils.database.connection_db import DataBaseHandle
from ..general.config import Parametros
import pytz
import jwt
import datetime
class authToken:
    tz=pytz.timezone("America/Guayaquil")
    secret=Parametros.JWT_KEY
    @classmethod
    def loginToken(cls, data):
        payload={
            'iat': datetime.datetime.now(tz=cls.tz),
            'exp': datetime.datetime.now(tz=cls.tz) + datetime.timedelta(minutes=30),
            'id':data['id'],
            'fk_tb_estudiante':data['fk_tb_estudiante'],
            'fk_tb_carrera':data['fk_tb_carrera'],
            'correo_institucional':data['correo_institucional'],
            'nivel_universitario':data['nivel_universitario'],
            'usuario':data['usuario'],
            'estado':data['estado']
        }
        try:
            return jwt.encode(payload,cls.secret,algorithm='HS256')
        except Exception as err:
            HandleLogs.write_error("Error al tratar de crear el token login: ",err);
            return None
        


    @classmethod
    def forgotPassToken(cls, data):
        payload={
            'iat': datetime.datetime.now(tz=cls.tz),
            'exp': datetime.datetime.now(tz=cls.tz) + datetime.timedelta(minutes=30),
            'id': data
        }
        try:
            return jwt.encode(payload,cls.secret,algorithm='HS256')
        except Exception as err:
            HandleLogs.write_error("Error al tratar de crear el token login: ",err);
            return None
        


    @classmethod
    def decodeTokenForgotPass(cls,encoded_token):
        try:
            payload=jwt.decode(encoded_token, cls.secret, algorithms='HS256')
            if payload is not None:
                HandleLogs.write_log("Token descifrado con exito")
                print (payload)
                return payload
        except jwt.ExpiredSignatureError:
            HandleLogs.write_error("Error: El token ha expirado.")
            return None
        except jwt.InvalidTokenError as e:
            HandleLogs.write_error(f"Error al tratar de desencriptar el token de acceso: {e}")
            return None
        except Exception as e:
            HandleLogs.write_error(f"Error inesperado al tratar de desencriptar el token de acceso: {e}")
            return None
