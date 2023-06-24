from django.contrib import admin
from django.urls import path
from courses import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/accounts/users', views.UserListView.as_view()),
    path('api/courses', views.CourseListView.as_view()),
    path('api/accounts/users/<int:pk>', views.UserViewSet.as_view({'get': 'retrieve', 'put': 'partial_update', 'delete': 'destroy'})),
    path('api/courses/<int:pk>', views.CourseViewSet.as_view({'get': 'retrieve', 'put': 'partial_update', 'delete': 'destroy'})),
    path('api/teachers/<int:pk>/courses', views.TeacherViewSet.as_view({'get': 'retrieve'})),
    path('api/reviews', views.ReviewViewSet.as_view()),
]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)