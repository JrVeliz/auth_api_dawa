from ...utils.general.logs import HandleLogs
from ..Models.Request.LoginRequest import LoginRequest
from flask import request
from flask_restful import Resource
from ...utils.general.response import response_error, response_success, response_not_found
from ..Components.LoginComponent import LoginComponent


class Login(Resource):

    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ingreso a Validar el Login")
            # Obtengo el Request
            rq_json = request.get_json()
            # Crear una instancia del esquema de validación
            login_schema = LoginRequest()

            # Validar los datos
            error = login_schema.validate(rq_json)
            if error:
                HandleLogs.write_error("Error al Validar el Request -> " + str(error))
                return response_error("Error al Validar el Request -> " + str(error))

            #Validar ese Request con mi modelo
            usuario = rq_json.get('usuario')
            contrasena = rq_json.get('contrasena')
            resultado = LoginComponent.Login(usuario, contrasena)
            if resultado is not None:
                HandleLogs.write_log("Login Exitoso - Service")
                return response_success(resultado)
            else:
                HandleLogs.write_log("Login Fallido - Service")
                return response_not_found()
        except Exception as err:
            HandleLogs.write_error(err)
