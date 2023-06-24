from rest_framework import permissions



class CourseUpdatePermision(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return (request.user in [teacher.user for teacher in obj.object_class.objects.filter(course=obj)]) or (request.user.is_superuser)