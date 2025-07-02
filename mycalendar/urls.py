
from django.urls import path
from . import views
urlpatterns = [
    path("",views.mycalendar,name = "mycalendar"),
    path("create/",views.create_event,name="create_event"),
    path("<int:eventid>/update/",views.update_event,name="update_event"),
    path("<int:eventid>/delete/",views.delete_event,name="delete_event"),
]