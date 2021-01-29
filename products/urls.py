from django.urls import path
from .views import products_page, order_page, signup, user_page, about_us, contacts_page

urlpatterns = [
    path('',products_page, name='products'),
    path('order/',order_page),
    path('signup/', signup, name='signup'),
    path('user/', user_page),
    path('aboutus/', about_us),
    path('contacts/', contacts_page)
]

