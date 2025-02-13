from django.urls import path
from .views import contact_view

urlpatterns = [
    path('contact/', contact_view, name='contact'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.urls import path
from .views import contact_view, share_cv_email

urlpatterns += [
    path('share/email/<int:cv_id>/', share_cv_email, name='share_cv_email'),
]
