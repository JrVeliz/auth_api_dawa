from marshmallow import Schema, fields

class generarTokenRequest(Schema):
    correo_institucional = fields.String(required=True)

class actualizarCuentaU(Schema):
    id = fields.String(required=True)
    contrasena = fields.String(required=True)