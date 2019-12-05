from django.urls import path, re_path
from django.conf.urls import include
from django.contrib.auth.models import User

from alumno import views

urlpatterns = [
    re_path(r'alumno_lista/$', views.AlumnoList.as_view()),
    re_path(r'alumno_detalle/(?P<id>[\w\-]+)$', views.AlumnoDetail.as_view()),
    re_path(r'asignaturas/$', views.Asignatura.as_view())
]