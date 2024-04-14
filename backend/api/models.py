from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.db.models.signals import post_save

# Create your models here.
class User(AbstractUser):
    username= models.CharField(max_length=100)
    email=models.EmailField(unique=True)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=['username']

    def __str__(self):
        return self.username
    
class Profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    full_name = models.CharField(max_length=300)
    bio = models.CharField(max_length=300)
    image = models.ImageField(default="default.jpg",upload_to="user_images")
    verified = models.BooleanField(default=False)

    def __str__(self):
        return self.full_name

    def create_user_profile(sender,instance,created, **kwargs):
        if created:
            Profile.objects.create(user=instance)

    def save_user_profile(sender, instance, **kwargs):
        instance.profile.save()

    post_save.connect(create_user_profile, sender=User)

    post_save.connect(save_user_profile, sender=User)





class Task(models.Model):
    STATUS_CHOICES = (
        ('todo', 'Todo'),
        ('in_progress', 'In Progress'),
        ('completed', 'Completed'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tasks')
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    status = models.CharField(max_length=12, choices=STATUS_CHOICES, default='todo')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class PomodoroSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='pomodoro_sessions')
    task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True, blank=True, related_name='pomodoro_sessions')
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    duration = models.IntegerField(help_text="Duration of the session in minutes")

    def __str__(self):
        return f"{self.user.username}'s session on {self.start_time.strftime('%Y-%m-%d %H:%M')}"