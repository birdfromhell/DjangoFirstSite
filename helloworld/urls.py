from . import views
from django.urls import path

app_name = "helloworld"
urlpatterns = [
    path('', views.hello, name='index'),
    path('<int:item_id>/', views.detail, name='detail'),
    path('item/', views.item, name='world'),
    # add item
    path('add', views.create_item, name='create_item'),
    # delete
    path('delete/<int:id>', views.delete_item, name='delete_item')
]
