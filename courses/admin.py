
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from . import models

@admin.register(models.User)
class UserAdmin(BaseUserAdmin):
    list_display = ['id', 'first_name', 'last_name', 'username', 'email', 'username']


@admin.register(models.Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['user']


@admin.register(models.Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'get_teachers', 'price', 'published_at']

    def get_teachers(self, obj):
        return "\n".join([p.user.username for p in obj.teacher.all()])


@admin.register(models.Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['id', 'course', 'user', 'score']
