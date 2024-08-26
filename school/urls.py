from django.urls import path
from .views import student_list
from . import views

# urlpatterns = [
#     path('students/', student_list, name='student_list'),
# ]



urlpatterns = [
    path('', views.index, name='index'),  # Root URL pattern
    path('students/', views.student_list, name='student_list'),
    path('teachers/', views.teacher_list, name='teacher_list'),
    path('classes/', views.class_list, name='class_list'),
    # Other URL patterns...
]
