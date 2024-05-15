from flask import Flask
from flask_cors import CORS
import cloudinary.api

from Demo_web.application.api.auth.auth import authBP
from Demo_web.application.api.users.users import usersBP
from Demo_web.application.api.books.books import booksBP
from Demo_web.application.api.comments.comments import commentBP
from Demo_web.application.api.discounts.discounts import discountBP
from Demo_web.application.api.Carts.carts import cartBP
from Demo_web.application.api.Orders.orders import orderBP
from Demo_web.application.api.ShippingMethods.shippingmethods import shipping_methodBP

app = Flask(__name__)
CORS(app, origins="*")

app.register_blueprint(authBP, url_prefix='/auth')
app.register_blueprint(usersBP, url_prefix='/user')
app.register_blueprint(booksBP, url_prefix='/book')
app.register_blueprint(commentBP, url_prefix='/comment')
app.register_blueprint(discountBP, url_prefix='/discount')
app.register_blueprint(cartBP, url_prefix='/cart')
app.register_blueprint(orderBP, url_prefix='/order')
app.register_blueprint(shipping_methodBP, url_prefix='/shipping')
cloudinary.config(
        cloud_name='di53bdbjf',
        api_key='517256683852343',
        api_secret='Y8_JBxk_9VxQ3L3wHcAoeZAt_vw'
)