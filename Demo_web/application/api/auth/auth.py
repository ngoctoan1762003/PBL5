import os
from Demo_web.application.utils import check_password, hash_password
import jwt
from flask import Blueprint, request, jsonify
authBP = Blueprint('auth', __name__)

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env'))
secret_key = os.getenv('SECRET_KEY')

from Demo_web.application.db.db import db

@authBP.post("/login")
def login():
    data = request.json
    if not data:
        print("loi")
    print(data)
    email = data.get("email")
    password = data.get("password")
    print(secret_key)
    try:
        user_collection = db['Users']
        if check_password(email, password, user_collection):
            user = user_collection.find_one({'Email': email})
            payload = {'user_id': str(user['_id']), 'role': user['Role']}
            token = jwt.encode(payload, secret_key, algorithm='HS256')
            return {
                "user": {
                    "User_id": str(user['_id']),
                    "Shop_name": user["Shop_name"],
                    "Password": str(user['Password']),
                    "Name": user['Name'],
                    "Image": user['image'],
                    "Email": user['Email'],
                    "Phone": user['Phone'],
                    "Address": user['Address'],
                    "Role": user['Role'],
                    "IsActivate": user['IsActivate'],
                },
                "token": token,
            }
        else:
            return jsonify({'error': "Sai tai khoan hoac mat khau"})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'success': False, 'error': str(e)})

@authBP.post("/register")
def register():
    data = request.json
    if not data:
        print("loi")
    shop_name = ""
    password = data.get('password')
    name = "user"
    email = data.get('email')
    phone = ""
    address = ""
    role = "user"
    image = "https://res.cloudinary.com/di53bdbjf/image/upload/v1714654040/R_vxfsuw.jpg"
    try:
        user_collection = db['Users']
        user = user_collection.find_one({'Email': email})
        if user:
            return jsonify({'message': 'Email already exists'}), 400
        hashed_password = hash_password(password)

        user = user_collection.insert_one({
            'Shop_name': shop_name,
            'Name': name,
            'Email': email,
            "image": image,
            'Password': hashed_password,
            'Phone': phone,
            'Address': address,
            'Role': role,
            "IsActivate": 0
        }).inserted_id
        return "Dang ki thanh cong"
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'success': False, 'error': str(e)})



