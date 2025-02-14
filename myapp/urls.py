from django.urls import path
from .views import create_cv, cv_list, share_cv_email

urlpatterns = [
    path('cv/create/', create_cv, name='create_cv'),
    path('cv/list/', cv_list, name='cv_list'),
    path('cv/share/<int:cv_id>/', share_cv_email, name='share_cv_email'),
]