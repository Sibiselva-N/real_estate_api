from django.conf.urls.static import static
from django.urls import path

from Real_Estate import settings
from . import views

urlpatterns = [
    path('sign_up', views.sign_up),
    path('verify_otp', views.verify_otp),
    path('login', views.login),
    path('update_user', views.update_user),
    path('add_estate', views.add_estate),
    path('estate_list', views.get_estate),
    path('single_estate', views.single_estate),
    path('update_estate', views.update_estate),
    path('delete_estate', views.delete_estate),
]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
