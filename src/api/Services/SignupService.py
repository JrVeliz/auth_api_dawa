from ...utils.general.logs import HandleLogs
from ..Models.Request.SignupRequest import SignupRequest
from flask import request
from flask_restful import Resource
from ...utils.general.response import response_error, response_success, response_not_found
from ..Components.SignupComponent import SignupCmponent

class Signup(Resource):
    @staticmethod
    def post():
        try:
            HandleLogs.write_log("Ingreso a Registrar estudiante nuevo")
            # Obtengo el Request
            rq_json = request.get_json()
            # Crear una instancia del esquema de validación
            signup_schema = SignupRequest()
            # Validar los datos
            error = signup_schema.validate(rq_json)
            if error:
                HandleLogs.write_error("Error al Validar el Request -> " + str(error))
                return response_error("Error al Validar el Request -> " + str(error))
            #Validar ese Request
            cedula = rq_json.get('cedula')
            nombre = rq_json.get('nombre')
            apellido = rq_json.get('apellido')
            correo_personal = rq_json.get('correo_personal')
            fecha_nacimiento = rq_json.get('fecha_nacimiento')
            genero = rq_json.get('genero')
            celular = rq_json.get('celular')
            resultado = SignupCmponent.signup(cedula, nombre, apellido, correo_personal, fecha_nacimiento, genero, celular)
            if resultado is not None:
                HandleLogs.write_log("Registro Exitoso")
                return response_success("Registro Exitoso, revise su correo")
            else:
                HandleLogs.write_log("Hubo un error al registrar el estudiante los datos del Signup - Service")
                return response_not_found()
        except Exception as err:
            HandleLogs.write_error(err)
