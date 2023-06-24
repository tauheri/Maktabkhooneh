from rest_framework import serializers

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'username', 'email']


class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'title', 'description', 'teacher', 'price', 'published_at', 'course_reviews_number', 'avg_course_score']

    
    course_reviews_number = serializers.SerializerMethodField(method_name='calculate_course_reviews_number')
    avg_course_score = serializers.SerializerMethodField(method_name='calculate_avg_course_score')

    def calculate_course_reviews_number(self, course: Course):
        return course.object_class.objects.filter(course=course).count()

    
    def calculate_avg_course_score(self, course: Course):
        reviews = course.object_class.objects.filter(course=course)
        scores = 0
        for review in reviews:
            scores += review.score
        if reviews.count() > 0:
            return scores/reviews.count()
        else:
            return 0


class TeacherSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username')

    class Meta:
        model = Course
        fields = ['id', 'username', 'courses']
    
    courses = serializers.SerializerMethodField(method_name='get_courses')

    def get_courses(self, teacher: Teacher):
        queryset = teacher.object_class.objects.filter(teacher=teacher)
        serializer = CourseSerializer(queryset, many=True) 
        return serializer.data


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'course', 'score']