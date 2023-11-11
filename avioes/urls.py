from django.urls import path

from . import views

app_name = 'avioes'
urlpatterns = [
    path('<int:aviao_id>/comment/', views.create_comment, name='comment'),]
