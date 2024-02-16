from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Subjects(models.Model):
    subject_name=models.CharField(max_length=50)
    def __str__(self) -> str:
        return self.subject_name
    
    class Meta:
        verbose_name ="subject names"
        # get_latest_by=["-subject_name"]
    
class CustomUser(AbstractUser):
    users= [
        ("1","Teacher"), ( "2", "Student")
        ]
    

    phone_number=models.CharField(max_length=10, unique=True)
    user_profile_image=models.ImageField(upload_to="profile_pictures")
    user_type= models.CharField(max_length=10, choices=users)
    email_address=models.EmailField(default="test@test.com")
    
class Marks(models.Model):
    student_id=models.ForeignKey(CustomUser, on_delete=models.DO_NOTHING)
    marks=models.CharField(max_length=10)
    subject_id=models.ForeignKey(Subjects, on_delete=models.DO_NOTHING)
    
