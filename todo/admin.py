from django.contrib import admin

from todo.models import Todo


@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_done')
    list_filter = ('is_done', 'created_at', 'updated_at')
