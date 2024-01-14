from ...utils.general.logs import HandleLogs
from ..Models.Request.ForgotPasswordRequest import generarTokenRequest
from ..Models.Request.ForgotPasswordRequest import actualizarCuentaU
from flask import request
from flask_restful import Resource
from ...utils.general.response import response_error, response_success, response_not_found
from ..Components.ForgotPasswordComponent import ForgotPasswordComponent


class ForgotPassword(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ingreso a Recuperar Cuenta")
            # Obtengo el Request
            rq_json = request.get_json()
            # Crear una instancia del esquema de validación
            generarToken = generarTokenRequest()

            # Validar los datos
            error = generarToken.validate(rq_json)
            if error:
                HandleLogs.write_error("Error al Validar el Request -> " + str(error))
                return response_error("Error al Validar el Request -> " + str(error))

            #Validar ese Request con mi modelo
            correo_institucional = rq_json.get('correo_institucional')
            resultado = ForgotPasswordComponent.recuperarCuenta(correo_institucional)
            if resultado:
                HandleLogs.write_log("Se ha generado el token Exitosamente");
                return response_success("Se ha generado el token Exitosamente, revise su correo")
            else:
                return response_not_found()
        except Exception as err:
            HandleLogs.write_error(err)


class activarRecuperacion(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ingreso a Activación de recuperacion de cuenta")
            # Obtengo el Token
            requestToken = request.headers.get('Authorization')
            if requestToken is None or not requestToken.startswith('Bearer '):
                HandleLogs.write_error("Token de autorización no proporcionado o en formato incorrecto")
                return response_error("Token de autorización no proporcionado o en formato incorrecto")
            token=requestToken.split()[1]
            #Validar ese Request con mi modelo
            resultado = ForgotPasswordComponent.activarRecuperacion(token)
            if resultado:
                HandleLogs.write_log("Se ha validado el token Exitosamente");
                return response_success(resultado)
            else:
                return response_not_found()


        except Exception as err:
            HandleLogs.write_error(err)


class actualizarCuenta(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ingreso a actualizar Cuenta")
            # Obtengo el Request
            rq_json = request.get_json()
            # Crear una instancia del esquema de validación
            actualizarCuenta = actualizarCuentaU()

            # Validar los datos
            error = actualizarCuenta.validate(rq_json)
            if error:
                HandleLogs.write_error("Error al Validar el Request -> " + str(error))
                return response_error("Error al Validar el Request -> " + str(error))

            #Validar ese Request con mi modelo
            id = rq_json.get('id')
            contrasena = rq_json.get('contrasena')
            resultado = ForgotPasswordComponent.actualizarCuentaU(id,contrasena)
            if resultado is not None:
                HandleLogs.write_log("Se ha actualizado la contraseña Exitosamente");
                return response_success("Se ha actualizado la contraseña Exitosamente, revise su correo")
            else:
                HandleLogs.write_error("Se ha generado un errro al actualizar la contraseña");
                return response_not_found()
        except Exception as err:
            HandleLogs.write_error(err)
