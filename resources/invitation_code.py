from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import InvitationCode, User
from flask_restful import Resource

class InvitationCodesApi(Resource):
    def get(self):
        invitation_codes = InvitationCode.objects().to_json()
        return Response(invitation_codes, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        user_id = get_jwt_identity()
        body = request.get_json()
        print(user_id)
        user = User.objects.get(id=user_id)
        invitation_code = InvitationCode(**body, user_for=user).save()
        user.update(push__invitation_codes=invitation_code)
        user.save()
        invitation_code_id = invitation_code.invitation_code_id
        return {'invitation_code_id': str(invitation_code_id)}, 200

class InvitationCodeApi(Resource):
    @jwt_required
    def get(self, invitation_code_id):
        user_id = get_jwt_identity()
        invitation_codes = InvitationCode.objects.get(invitation_code_id=invitation_code_id, user_for=user_id).to_json()
        return Response(invitation_codes, mimetype="application/json", status=200)