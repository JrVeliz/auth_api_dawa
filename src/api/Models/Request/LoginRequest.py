from marshmallow import Schema, fields

class LoginRequest(Schema):
    usuario = fields.String(required=True)
    contrasena = fields.String(required=True)

