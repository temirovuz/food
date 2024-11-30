from geopy.distance import geodesic

from config.settings import env
from fastfood.models import OrderItem

grocery_store_lat = env('LONGITUDE')
grocery_store_lon = env('LATITUDE')

def distance(user_lat, user_lon):
    restaurant_coord = (grocery_store_lat, grocery_store_lon)
    user_coord = (user_lat, user_lon)

    distance = geodesic(restaurant_coord, user_coord).kilometers
    return distance


def get_user_order_items_quantity(user):
    order_items = OrderItem.objects.filter(user=user)
    total_quantity = 0
    for item in order_items:
        total_quantity += item.quantity
    return total_quantity


def to_divide_into_a_unit_of_time(time):
    timee = round(time)
    hour = timee // 60
    minut = timee % 60
    if hour != 0:
        return f"{hour} soat {minut} daqiqa"
    else:
        return f"{minut} daqiqa"
