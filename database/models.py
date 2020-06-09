from .db import db
from flask_bcrypt import generate_password_hash, check_password_hash

class InvitationCode(db.Document):
    user_for = db.ReferenceField('User')
    invitation_code_id = db.StringField(required=True, unique=True)
    is_used = db.BooleanField(required=True)

class User(db.Document):
    name = db.StringField()
    phone=db.StringField()
    email = db.EmailField(unique=True)
    nickname = db.StringField(unique=True)
    about = db.StringField()
    gender = db.IntField() #0=MALE,1=FEMALE,2=UNKNOWN
    birthday = db.DateTimeField()
    profile_image = db.StringField()
    height = db.IntField() # in cms
    friends_preference = db.IntField() #0=MALE,2=FEMALE,2=ANY
    is_verified = db.BooleanField(default=False)
    password = db.StringField(required=True, min_length=6)
    city = db.StringField()
    latlng = db.GeoPointField()

    invitation_codes = db.ListField(db.ReferenceField('InvitationCode', reverse_delete_rule=db.PULL))
    

    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')

    def check_password(self, password):
        return check_password_hash(self.password, password)

User.register_delete_rule(InvitationCode, 'user_for', db.CASCADE)