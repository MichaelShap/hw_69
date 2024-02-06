from django.urls import path, include
from api_1.views import add_view, subtract_view, multiply_view, divide_view, get_token_view

app_name = 'api_1'

urlpatterns = [
    path('add/', add_view, name='add_result' ),
    path('subtract/', subtract_view, name='subtract_result'),
    path('multiply/', multiply_view, name='multiply_result'),
    path('divide/', divide_view, name='divide_result'),
    path('token/', get_token_view, name='token'),
]