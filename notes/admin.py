from django.contrib import admin
from notes.models import Todos

# Register your models here.
class TodosAdmin(admin.ModelAdmin):
    list_listview=('todo_name','todo_description')
admin.site.register(Todos,TodosAdmin)