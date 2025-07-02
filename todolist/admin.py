from django.contrib import admin
from .models import TodoList,Event_Todo
# Register your models here.
class TodoListAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)
admin.site.register(TodoList,TodoListAdmin)
admin.site.register(Event_Todo)