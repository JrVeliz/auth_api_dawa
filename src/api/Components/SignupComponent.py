from ...utils.general.logs import HandleLogs
from ...utils.database.connection_db import DataBaseHandle
from ...utils.emails.generarEmail import generarEmail

class SignupCmponent:
    @staticmethod
    def signup(cedula, nombre, apellido, correo_personal, fecha_nacimiento, genero, celular):
        try:
            status=False
            resultado=ValidarCedula.validar(cedula)

            if resultado is None:
                HandleLogs.write_error("Error al recibir los datos de la cedula verificada - signup")
                return status
            else:
                fk_carrera_postulada = resultado['fk_carrera_postulada']
            id_newEstudiante = RegistrarEstudiante.newEstudiante(cedula, nombre, apellido, correo_personal, fecha_nacimiento, genero, celular)
            if id_newEstudiante is None:
                HandleLogs.write_error("Error al recibir los datos de la nueva cuenta a registrar - signup")
                return status
            dataCuentaU = RegistrarDatosUniversitarios.newUniversitario(id_newEstudiante, fk_carrera_postulada, cedula, nombre, apellido)
            if dataCuentaU:
                status=True
                correoI=dataCuentaU[1]
                generarEmail.generarEmailSignup(nombre, cedula, correo_personal, correoI)
                HandleLogs.write_log("Se creo y se envio el correo - signup")
                return status
        except Exception as err:
            HandleLogs.write_error("Error al registrar un nuevo estudiante: ",err)


class ValidarCedula:
    @staticmethod
    def validar(cedula):
        try: 
            sql = f"SELECT * FROM siug.tb_postulantes_senescy WHERE cedula = '{cedula}'"
            record =(cedula)
            resultado = DataBaseHandle.getRecords(sql, 1, record)
            if resultado is None:
                HandleLogs.write_error("No se encontro un usuario registrado en la Senescy - Validar")
                return False
            else:
                HandleLogs.write_log("Cedula validada [tiene cupo aceptado en la Senescy]")
                return resultado
        except Exception as err:
            HandleLogs.write_error("Error al validar la cedula: ", err)


class RegistrarEstudiante:
    @staticmethod
    def newEstudiante(cedula, nombre, apellido, correo_personal, fecha_nacimiento, genero, celular):
        user_id=None
        try:
            query = "INSERT INTO siug.tb_estudiante (cedula, nombre, apellido, correo_personal, fecha_nacimiento, genero, celular) VALUES (%s, %s, %s, %s, %s, %s, %s)"
            record = (cedula, nombre, apellido, correo_personal, fecha_nacimiento, genero, celular)
            user_id = DataBaseHandle.ExecuteNonQuery(query, record)
            if user_id is None:
                HandleLogs.write_error("Error al obtener el id del estudiante al registrar")
                return None
            else:
                HandleLogs.write_log("Estudiante registrado con exito", user_id)
                return user_id
        except Exception as ex:
            HandleLogs.write_error("Error al registrar un nuevo estudiante: ",ex)
            return None


class RegistrarDatosUniversitarios:
    @staticmethod
    def newUniversitario(id_estudiante, id_carrera, cedula, nombre, apellido):
        user_id=None
        try:
            correoInstitucional=GeneradorCorreoInstitucional.generar(nombre, apellido);
            query = "INSERT INTO siug.tb_datos_universitarios_estudiante (fk_tb_estudiante, fk_tb_carrera, correo_institucional, usuario, contrasena) VALUES (%s,%s,%s,%s,%s)"
            record=(id_estudiante, id_carrera,correoInstitucional,cedula,cedula);
            user_id = DataBaseHandle.ExecuteNonQuery(query, record)
            if user_id is None:
                HandleLogs.write_error("Error al obtener el id del perfil universitario al registrar - newUniversitario ")
                return None
            else:
                dataUniversitario=(cedula, correoInstitucional)
                # generarEmail.generarEmailSignup(nombre, cedula, correo_personal, correoInstitucional)
                HandleLogs.write_log("Correo Enviado - newUniversitario ", user_id)
                HandleLogs.write_log("Perfil universitario creado con exito - newUniversitario ", user_id)
                return dataUniversitario
        except Exception as ex:
            HandleLogs.write_error("Error al crear el perfil universitario: - newUniversitario",ex)
            return None
        
        
class GeneradorCorreoInstitucional:
    @staticmethod
    def generar(nombre, apellido):
        correoNombre= nombre.split()[0].lower() if nombre else ''
        correoApellido=apellido.split()[0].lower() if apellido else ''
        newCorreo = f"{correoNombre}.{correoApellido}@ug.edu.ec"
        return newCorreo

class signupEmail:
    @staticmethod
    def crearEmail(data):
        usuario=data[0]
        contrasenia=data[0]
        correoI=data[1]
    #WEAS DE LA LIBRERIA PA EL CORREO