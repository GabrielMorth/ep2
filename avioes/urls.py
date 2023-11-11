from django.urls import path

from . import views

app_name = 'avioes'
urlpatterns = [
    path('', views.AviaoListView.as_view(), name='index'),
    path('create/', views.AviaoCreateView.as_view(), name='create'),
    path('<int:pk>/', views.AviaoDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', views.AviaoUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', views.AviaoDeleteView.as_view(), name='delete'),
    path('<int:aviao_id>/comment/', views.create_comment, name='comment'),
    path('categories/', views.CategoriesListView.as_view(), name='categories'),
    path('category/<int:category_id>/', views.detail_category, name='category'),]
