from ...utils.general.logs import HandleLogs
from ...utils.database.connection_db import DataBaseHandle
from ...utils.tokens.authToken import authToken
class LoginComponent:
    @staticmethod
    def Login(usuario, contrasena):
        try:
            sql = "SELECT id, fk_tb_estudiante,fk_tb_carrera, nivel_universitario, usuario FROM siug.tb_datos_universitarios_estudiante WHERE usuario = %s AND contrasena = %s"
            record =(usuario, contrasena);
            resultado = DataBaseHandle.getRecords(sql, 1, record)
            if resultado is  None:
                HandleLogs.write_error("Error al obtener los datos del registro - Login")
                return resultado
            else:
                #AQUI SE CREA EL TOKEN
                token = authToken.loginToken(resultado)
                if token is None:
                    HandleLogs.write_error("No se recibio el token para el user:  ", usuario)
                    return None
                else:
                    HandleLogs.write_log("Login Exitoso para usuario: ", usuario)
                    return token   
        except Exception as err:
            HandleLogs.write_error(err)

#if (len(valor)>0):