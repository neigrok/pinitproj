
from django.conf.urls import url
from .views import Register
from .views import Login
from .views import logout_view

urlpatterns = [
    url(r'register$', Register.as_view()),
    url(r'login$', Login.as_view()),
    url(r'logout$', logout_view),
]