from ..Services.LoginService import Login
from ..Services.SignupService import Signup
from ..Services.ForgotPasswordService import ForgotPassword
from ..Services.ForgotPasswordService import activarRecuperacion
from ..Services.ForgotPasswordService import actualizarCuenta
def load_routes(api):

    api.add_resource(Login, '/security/login')

    api.add_resource(Signup, '/security/create')

    api.add_resource(ForgotPassword, '/security/forgotPassword')
    
    api.add_resource(activarRecuperacion, '/security/activarRecuperacion')

    api.add_resource(actualizarCuenta, '/security/actualizarCuenta')
    