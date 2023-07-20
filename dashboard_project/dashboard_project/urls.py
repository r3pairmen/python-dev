from django.contrib import admin
from django.urls import path
from dashboard_app.views import get_filtered_data

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/data/', get_filtered_data, name='get_filtered_data'),
]
