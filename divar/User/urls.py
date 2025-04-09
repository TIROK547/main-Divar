from django.urls import path
from .views import add_user,update_user_name
urlpatterns =[
    path("add-user",add_user),
    path("update-user-name",update_user_name)
]
