from rest_framework import permissions, generics, viewsets


from .models import *
from .serializers import *
from .permision import *



class UserListView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]
    lookup_field = 'pk'


class CourseListView(generics.ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    ordering = ['-published_at']

    def get_permissions(self):
        self.permission_classes = [permissions.IsAuthenticated]
        if self.request.method == "POST":
            self.permission_classes = [permissions.IsAdminUser]
        return super(CourseListView, self).get_permissions()


class CourseViewSet(viewsets.ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    lookup_field = 'pk'

    def get_permissions(self):
        self.permission_classes = [permissions.IsAuthenticated]
        if self.request.method == "DELETE":
            self.permission_classes = [permissions.IsAdminUser]
        if self.request.method == "PUT":
            self.permission_classes = [CourseUpdatePermision]
        return super(CourseViewSet, self).get_permissions()


class TeacherViewSet(viewsets.ModelViewSet):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = 'pk'


class ReviewViewSet(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)