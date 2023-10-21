from django.urls import path
from classroom import view as views

urlpatterns = [
    path('classrooms', views.class_list, name='class_list'),
    path('<int:class_id>/', views.single_class, name='single_class'),
    path('registration/', views.create_class, name='create_class'),
    path('edit/<int:pk>', views.edit_class, name='edit_class'),
    path('delete/<int:class_id>', views.delete_class, name='delete_class'),
]
