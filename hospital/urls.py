
from django.contrib import admin
from django.urls import path
from hospitalapp import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('patients',views.patients,name="patient"),
    path('doctor',views.doctors,name='doctors'),
    # path('data',views.data,name='data')
    path('admin',views.admin,name="admin"),
    path('appoint',views.appoint,name="appoint"),
    path('remove_cand/<int:cand_id>',views.remove_cand,name='remove_cand')
]
