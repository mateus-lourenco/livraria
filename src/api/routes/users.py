from os import access, error
from flask import Blueprint, request
from api.utils.responses import response_with
from api.utils import responses as resp
from api.models.users import User, UserSchema
from api.utils.database import db
from flask_jwt_extended import create_access_token
from api.utils.token import generate_verification_token, confirm_verification_token


user_routes = Blueprint("user_routes", __name__)

@user_routes.route("/", methods=["POST"])
def create():
    try:
        data = request.get_json()
        data["password"] = User.generate_hash(data["password"])
        user_schema = UserSchema()
        user, error = user_schema.load(data)
        result = user_schema.dump(user.create()).data
        return response_with(resp.SUCCESS_201)
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)

@user_routes.route("/login", methods=["POST"])
def auth():
    try:
        data = request.get_json()
        if data.get("email"):
            current_user = User.find_by_email(data["email"])
        elif data.get("username"):
            current_user = User.find_by_username(data["username"])
            
        if not current_user:
            return response_with(resp.SERVER_ERROR_404)
        if current_user and not current_user.isVerified:
            return response_with(resp.SERVER_ERROR_404)
            
        if User.verify_hash(data["password"], current_user.passowrd):
            access_token = create_access_token(identity=data["username"])
            return response_with(resp.SUCCESS_201, value={"message":f"Logged in as {current_user.username}", 
                                                        "access_token":access_token})
        else:
            return response_with(resp.UNAUTHORIZED_403)
    except Exception as e:
        print(e)
        return response_with(resp.INVALID_INPUT_422)
    
@user_routes.route("/confirm/<token>", methods=["GET"])
def verify_email(token):
    try:
        email = confirm_verification_token(token)
    except:
        return response_with(resp.SERVER_ERROR_403)
    
    user = User.query.filter_by(email=email).first_or_404()
    
    if user.isVerified:
        return response_with(resp.INVALID_INPUT_422)
    else:
        user.isVerified = True
        db.session.add(user)
        db.session.commit()
        return response_with(resp.SUCCESS_200, value={"message":
                "E-mail verified, you can proceed to login now."})