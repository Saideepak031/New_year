from django.contrib import admin
from .models import Note, Goal, Wish

admin.site.register(Note)
class NoteAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj = ...):
        return super().has_delete_permission(request, obj) and False
admin.site.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj = ...):
        return super().has_delete_permission(request, obj) and False
admin.site.register(Wish)
class WishAdmin(admin.ModelAdmin):
    def has_delete_permission(self, request, obj = ...):
        return super().has_delete_permission(request, obj) and False

