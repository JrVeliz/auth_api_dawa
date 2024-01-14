import os
from flask import Flask
from flask_cors import CORS
from flask_restful import Api
from src.utils.general.logs import HandleLogs
from src.api.Routes.Routes import load_routes

app = Flask(__name__)
CORS(app)
api = Api(app)
load_routes(api)

if __name__ == '__main__':
    try:
        HandleLogs.write_log("API - AUTH")
        HandleLogs.write_log("Servicio Iniciado")
        port = int(os.environ.get('PORT', 1001))
        app.run(debug=True, host='0.0.0.0', threaded=True)

    except Exception as err:
        HandleLogs.write_error(err)
    finally:
        HandleLogs.write_log("Servicio Finalizado")
