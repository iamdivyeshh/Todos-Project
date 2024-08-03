from django.contrib import admin
from django.urls import path
from notes.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path('', home , name="home_page"),
    path('login/', login_page , name="login_page"),
    path('logout/', logout_page , name="logout_page"),
    path('register/', signup , name="register"),
    path('todos/', todos , name="todos"),
    path('delete-todo/<id>/', delete_todo , name="delete_todo"),
    path('view_todos/', view_todo , name="view_todo"),
    path('update-todo/<id>/', update_todo , name="update_todo"),
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL,
                          document_root = settings.MEDIA_ROOT)
    
    
