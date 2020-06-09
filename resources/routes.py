from .invitation_code import InvitationCodesApi, InvitationCodeApi
from .auth import SignupApi, LoginApi

def initialize_routes(api):
 api.add_resource(InvitationCodesApi, '/invitation_codes')
 api.add_resource(InvitationCodeApi, '/invitation_codes/<invitation_code_id>')

 api.add_resource(SignupApi, '/api/auth/signup')
 api.add_resource(LoginApi, '/api/auth/login')