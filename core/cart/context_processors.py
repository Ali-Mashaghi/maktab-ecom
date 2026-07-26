from .cart import CartSession

def cart_processor(requset):
    cart = CartSession(requset.session)
    return {'cart': cart} 