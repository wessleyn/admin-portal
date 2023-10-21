# from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
# from users.views import LoginView, LogoutView, Dashboard

urlpatterns = [
   
    # path('login/', LoginView.as_view(), name='login'),
    # path('logout/', LogoutView.as_view(), name='logout'),
    # path('dashboard/', Dashboard.as_view(), name='dashboard'),
    # path('grappelli/', include('grappelli.urls')),  # grappelli URLS
    # path('admin/', admin.site.urls),
    # path('admin/', admin.site.urls),
    # path('setup/',include('setup.urls'))
    path('api/', include('api.urls')),
    path('', include('apps.adminstrator.urls')),
]+ static(settings.MEDIA_URL,  document_root=settings.MEDIA_ROOT)
