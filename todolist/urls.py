
from django.urls import path
from . import views
urlpatterns = [
    path("",views.List_Todolist,name = "List_Todolist"),
    path("create/",views.Create_Todolist,name = "Create_Todolist"),
    path("<int:Todolist_id>/edit",views.Edit_Todolist,name = "Edit_Todolist"),
    path("<int:Todolist_id>/delete",views.Delete_Todolist,name = "Delete_Todolist"),
    path("register",views.register,name = "register"),
    path('<int:Todo_id>/completed',views.completed,name='Completed'),
    path('<int:id>/event-completed',views.Event_completed,name="Event_completed"),

    


]