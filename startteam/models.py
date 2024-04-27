from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import BaseUserManager
from django.contrib.auth.hashers import make_password   


STATUS_CHOICES = (
    ('BUSY', 'BUSY'),
    ('FREE', 'FREE'))

PROJECT_CHOICES = (
    ('STARTED', 'STARTED'),
    ('INPROGRESS', 'INPROGRESS'),
    ('DONE', 'DONE'),
    ('REJECTED', 'REJECTED')
)


class CustomUserManager(BaseUserManager):
    def create_user(self, username, address='', password=None, **extra_fields):
        if not username:
            raise ValueError('The Username field must be set')
        user = self.model(username=username, address=address, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, username, address='', password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(username, address, password, **extra_fields)


class User(AbstractUser):
    
    full_name = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    skills = models.TextField()
    image = models.FileField(upload_to="profile", blank=True, null=True)
    projects_number = models.IntegerField(blank=True, null=True)
    balance = models.FloatField(default=0)
    address = models.CharField(max_length=300, null=True, blank=True)
    status = models.CharField(choices=STATUS_CHOICES, max_length=10)
    contacts = models.TextField(blank=True, null=True)
    education = models.CharField(max_length=400,  blank=True, null=True)
    accepted = models.BooleanField(default=False)
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
    
    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.full_name + ' - ' + self.position

    def has_workers(self):
        return self.workers.exists()
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)


class Images(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)


class Projects(models.Model):
    type = models.CharField(max_length=200, null=True, blank=True)
    name = models.CharField(max_length=200, null=True, blank=True)
    contacts = models.CharField(max_length=900)
    desc = models.TextField(blank=True, null=True)
    desc_to_workers = models.TextField(blank=True, null=True)
    price = models.FloatField(verbose_name="Project's price")
    workers_id = models.ManyToManyField(User, blank=True)
    status = models.CharField(choices=PROJECT_CHOICES, max_length=15)
    paid_money = models.FloatField(default=0)
    images = models.ManyToManyField(Images)
    start_date = models.DateField(blank=True, null=True)
    duration = models.CharField(max_length=200, null=True, blank=True)
    end_date = models.DateField(blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Orders(models.Model):
    order_name = models.CharField(max_length=200)
    desc = models.TextField()
    contacts = models.CharField(max_length=300)
    major = models.CharField(max_length=200, verbose_name="category name")
    address = models.CharField(max_length=400, blank=True, null=True)
    organisation = models.CharField(max_length=400, blank=True, null=True)
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.order_name


class Team(models.Model):
    name = models.CharField(max_length=255)
    team_lead = models.ForeignKey(User, on_delete=models.CASCADE, related_name='leading_teams')
    project_id = models.ForeignKey(Projects, on_delete=models.CASCADE)
    workers_id = models.ManyToManyField(User, related_name='teams')
    summa = models.FloatField()
    paid_money = models.FloatField()
    status = models.BooleanField(default=True)
    telegram_group = models.URLField(default='https://t.me/')
    date = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Telegram(models.Model):
    apiToken = models.CharField(verbose_name="Api Token", max_length=255)
    chatID = models.CharField(verbose_name="Chat Id", max_length=255)
    Date = models.DateTimeField(verbose_name="Date", auto_now_add=True)
    class Meta:
        verbose_name = 'Telegram'
        verbose_name_plural = 'Telegram'


class Proposal(models.Model):
    project = models.ForeignKey(Projects, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField(max_length=10000)
    date = models.DateTimeField(auto_now_add=True)
    joined = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Proposal'
        verbose_name_plural = 'Proposals'
