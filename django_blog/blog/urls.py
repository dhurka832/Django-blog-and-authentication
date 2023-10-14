from django.urls import path 
from . import views


urlpatterns = [
    path('',views.index,name="posts"),
    path('create_post/',views.create_post,name="post-create"),
    path('detail_post/<int:id>',views.detail_post,name="post-detail"),
    path('update_post/<int:id>',views.update_post,name="post-update"),
    path('delete_post/<int:id>',views.delete_post,name="post-delete"),
]
