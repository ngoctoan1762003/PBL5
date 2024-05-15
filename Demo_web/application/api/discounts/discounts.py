import os

from bson import ObjectId

from Demo_web.application import utils
from Demo_web.application.utils import check_password, hash_password
import jwt
from flask import Blueprint, request, jsonify
discountBP = Blueprint('discount', __name__)

from dotenv import load_dotenv
load_dotenv(os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), '.env'))
secret_key = os.getenv('SECRET_KEY')

from Demo_web.application.db.db import db

@discountBP.get("/<id>")
def ListDiscount(id):
    try:
        discounts = db.Discounts.find({"ShopId": ObjectId(id)})
        discounts = list(discounts)
        for discount in discounts:
            discount['_id'] = str(discount['_id'])
            del discount['ShopId']
        return jsonify(discounts)
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'success': False, 'error': str(e)})

@discountBP.post("/<id>")
def CreateDiscount(id):
    try:
        token = request.headers.get('Authorization')
        token = utils.extract_token(token)
        if token.get('user_id') == id:

            data = request.json
            code = data.get('discount_code')
            amount = data.get('amount')
            percent = data.get('percent')
            quantity = data.get('quantity')
            start_day = data.get('start_day')
            end_day = data.get('end_day')
            if db.Discounts.find_one({"ShopId": ObjectId(id), "DiscountCode": code}):
                return "Discount code already exists"
            else:
                discount = db.Discounts.insert_one({
                    'DiscountCode': code,
                    'DiscountAmount': amount,
                    'DiscountPercent': percent,
                    "Quantity": quantity,
                    'StartDay': start_day,
                    'EndDay': end_day,
                    'ShopId': ObjectId(id)
                }).inserted_id
        return "create discount success"
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'success': False, 'error': str(e)})

@discountBP.put("/<id>")
def UpdateDiscount(id):
    try:
        token = request.headers.get('Authorization')
        token = utils.extract_token(token)
        discount = db.Discounts.find_one({'_id': ObjectId(id)})
        if discount:
            if token.get('user_id') == str(discount['ShopId']):
                data = request.json

                code = data.get('discount_code')
                amount = data.get('amount')
                percent = data.get('percent')
                quantity = data.get('quantity')
                start_day = data.get('start_day')
                end_day = data.get('end_day')

                db.Discounts.update_one(
                    {
                        "_id": ObjectId(id)
                    },
                    {
                        "$set": {
                            'DiscountCode': code,
                            'DiscountAmount': amount,
                            'DiscountPercent': percent,
                            "Quantity": quantity,
                            'StartDay': start_day,
                            'EndDay': end_day
                        }
                    }
                )
                discount = db.Discounts.find_one({'_id': ObjectId(id)})
                discount['_id'] = str(discount['_id'])
                del discount['ShopId']
            return discount
        else:
            return jsonify({'message': 'Discount code not already exists'}), 400
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'success': False, 'error': str(e)})

@discountBP.delete("/<id>")
def DeleteDiscount(id):
    try:
        token = request.headers.get('Authorization')
        token = utils.extract_token(token)
        discount = db.Discounts.find_one({'_id': ObjectId(id)})
        if discount:
            if token.get('user_id') == str(discount['ShopId']):
                result = db.Discounts.delete_one({'_id': ObjectId(id)})
                if result.deleted_count == 1:
                    return f"Discount code with _id {str(id)} has been deleted successfully."
                else:
                   return f"Discount code with _id {str(id)} not found."
            else:
                return jsonify({"message": "khong du quyen han"})
        else:
            return jsonify({'message': 'Discount code not already exists'}), 400
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({'success': False, 'error': str(e)})
