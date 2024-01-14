from ...utils.general.logs import HandleLogs
from ...utils.database.connection_db import DataBaseHandle
from ...utils.tokens.authToken import authToken
from ...utils.emails.generarEmail import generarEmail


class ForgotPasswordComponent:
    @staticmethod
    def recuperarCuenta(correo_institucional):
        estado=False
        try:
            sql = f"SELECT id FROM siug.tb_datos_universitarios_estudiante WHERE correo_institucional = '{correo_institucional}'"
            record = (correo_institucional)
            resultado = DataBaseHandle.getRecords(sql, 1, record)
            if resultado is None:
                HandleLogs.write_error("No se encontro una cuenta asociada al correo")
            else:
                HandleLogs.write_log("Se encontró la cuenta a recuperar: ")
                id=str(resultado['id'])
                token= authToken.forgotPassToken(id)
                if token is None:
                    HandleLogs.write_error("Error al recibir el token a generar - recuperarCuenta")
                    return estado
                else:
                    estado=True
                    generarEmail.generarEmailForgotPass(correo_institucional, token)
                    HandleLogs.write_log("Token creado con exito, revise el correo - recuperarCuenta")
                    return estado
                    
        except Exception as err:
            HandleLogs.write_error("Se ha generado un error al crear el token de acceso: ", err)

    @staticmethod
    def activarRecuperacion(token):
        try:
            data=authToken.decodeTokenForgotPass(token)
            if data is None:
                HandleLogs.write_error("Se ha generado un error al obtener la decodificacion de token - activarRecuperacion")
            else:
                HandleLogs.write_error("Token decifrado - activarRecuperacion")
                id=data['id']
                dataCuenta=ForgotPasswordComponent.obtenerCuentaRecuperar(id)
                if dataCuenta is None:
                    HandleLogs.write_error("Se ha generado un error al recibir la información de la cuenta - activarRecuperacion")
                else:
                    HandleLogs.write_error("Datos de la cuenta obtenidos- activarRecuperacion")
                    return dataCuenta
                return id
        except Exception as err:
            HandleLogs.write_error("Se ha generado un error al validar el token: ",err)
            return
         
    @staticmethod
    def obtenerCuentaRecuperar(id):
        try:
            sql = f"SELECT id, usuario, contrasena FROM siug.tb_datos_universitarios_estudiante WHERE id = {id}"
            record =(id)
            resultado = DataBaseHandle.getRecords(sql, 1, record)
            if resultado is  None:
                HandleLogs.write_error("Error al obtener los datos de la cuenta a recuperar - obtenerCuentaRecuperar")
                return resultado
            else:
                HandleLogs.write_log("Cuenta a recuperar encontrada- obtenerCuentaRecuperar")
                return resultado
        except Exception as err:
            HandleLogs.write_error(err)
            return None

    @staticmethod
    def actualizarCuentaU(id, contrasena):
        try:
            sql="UPDATE siug.tb_datos_universitarios_estudiante SET contrasena=%s WHERE id = %s"
            record =(contrasena,id)
            resultado = DataBaseHandle.ExecuteNonQuery(sql, record)
            if resultado is  None:
                HandleLogs.write_error("Error al actualizar la contraseña - actualizarCuentaU")
                return None
            else:
                HandleLogs.write_log("Contraseña actualizada- actualizarCuentaU")
                return resultado
        except Exception as err:
            HandleLogs.write_error(err)
            return None