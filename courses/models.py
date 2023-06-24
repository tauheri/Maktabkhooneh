from django.db import models
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator
from django.core.exceptions import ValidationError


def validate_course_price(value):
    if value >= 10000.00:
        return value
    else:
        raise ValidationError("You can not add a course cheapper than 10000")
    

class User(AbstractUser):
    email = models.EmailField(unique=True)


class BaseModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updates = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Teacher(BaseModel):
    @property
    def object_class(self):
        return Course
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username


class Course(BaseModel):
    @property
    def object_class(self):
        return Review

    title = models.CharField(max_length=255)
    description = models.TextField()
    teacher = models.ManyToManyField(Teacher)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[validate_course_price])
    published_at = models.DateField()

    def __str__(self) -> str:
        return self.title


class Review(BaseModel):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.PositiveSmallIntegerField(validators=[MaxValueValidator(5)])

    def __str__(self) -> str:
        return self.user.username + " " + self.course.title