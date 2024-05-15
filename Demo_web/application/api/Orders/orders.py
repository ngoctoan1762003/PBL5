from bson import ObjectId
from flask import Blueprint, request, jsonify
from datetime import datetime
from Demo_web.application import utils
from Demo_web.application.db.db import db

orderBP = Blueprint('order', __name__)

@orderBP.route('/order', methods=['POST'])
def place_order():
    try:
        # Lấy thông tin đơn hàng từ request
        order_data = request.json
        # Kiểm tra dữ liệu đơn hàng
        required_fields = ['userid', 'address', 'status', 'books', 'shipping_id']
        if not order_data or not all(key in order_data for key in required_fields):
            missing_fields = [field for field in required_fields if field not in order_data]
            return jsonify({'success': False, 'error': f'Missing fields: {missing_fields}'}), 400

        # Lấy thông tin người dùng từ token
        token = request.headers.get('Authorization')
        token = utils.extract_token(token)
        user_id = ObjectId(token.get('user_id'))

        # Tạo danh sách các sản phẩm trong đơn hàng và tính tổng giá
        order_items = []
        total_price = 0
        for item in order_data['books']:
            book_id = ObjectId(item['_id'])
            quantity = item['quantity']
            price = item['price']
            title = item['title']

            # Tính tổng giá của từng sản phẩm
            item_total_price = price * quantity
            total_price += item_total_price

            order_items.append({
                'book_id': book_id,
                'quantity': quantity,
                'price': price,
                'title': title,
                'total_price': item_total_price
            })

        # Lấy phí vận chuyển dựa trên shipping_id
        shipping_id = order_data.get('shipping_id')
        shipping_method = db.ShippingMethods.find_one({'_id': ObjectId(shipping_id)})

        if shipping_method is None:
            return jsonify({'success': False, 'error': 'Shipping method not found'}), 404

        shipping_cost = shipping_method.get('Cost', 0)
        total_price += shipping_cost

        # Lưu đơn hàng vào cơ sở dữ liệu
        current_time = datetime.now()

        order = {
            'OrderDate': current_time,
            'OrderAmount': total_price,
            'UserId': user_id,
            'ShippingMethodId': ObjectId(shipping_id)
        }

        # Tạo đơn hàng mới và lưu vào cơ sở dữ liệu
        result = db.Orders.insert_one(order)
        order_id = result.inserted_id

        # Lưu thông tin chi tiết của từng sản phẩm vào bảng OrderDetails
        for item in order_items:
            order_detail = {
                'OrderId': order_id,
                'BookId': item['book_id'],
                'Quantity': item['quantity'],
                'Price': item['price'],
                # 'DiscountId': ObjectId(order_data['shopid'])
            }
            db.OrderDetails.insert_one(order_detail)

        return jsonify({'success': True, 'message': 'Order placed successfully'}), 201

    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500