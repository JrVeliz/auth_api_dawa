from marshmallow import Schema, fields, validates, ValidationError

class SignupRequest(Schema):
    cedula = fields.String(required=True)
    nombre = fields.String(required=True)
    apellido = fields.String(required=True)
    correo_personal = fields.String(required=True)
    fecha_nacimiento = fields.String(required=True)
    genero = fields.String(required=True)
    celular = fields.String(required=True)