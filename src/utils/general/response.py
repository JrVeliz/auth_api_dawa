from flask import jsonify

def response_inserted(datos):
    return{
        'result': True,
        'message': "registro insertado con exito",
        'data': datos,
        'status_code': 201,
    }, 201

def response_not_found():
    return {
        'result': False,
        'message': "No hay datos de consulta",
        'data': {},
        'status_code': 404,
    }, 404

def response_success(datos):
    return {
        'result': True,
        'message': "Exito",
        'data': datos,
        'status_code': 200,
    }, 200

def response_error(mensaje):
    return {
        'result': False,
        'message': mensaje,
        'data': {},
        'status_code': 500,
    }, 500