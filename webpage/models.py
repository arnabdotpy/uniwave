from django.db import models

# Create your models here.
class Announcement(models.Model):
  title = models.CharField(max_length=1000)
  description = models.CharField(max_length=10000)
  author = models.CharField(max_length=1000)
  TAG_CHOICES = [
        ('Academic', 'Academic'),
        ('Clubs & Chapters', 'Clubs & Chapters'),
        ('event', 'Events'),
        ('Placement', 'Placement'),
        ('Scholarship', 'Scholarship'),
        ('Seminar', 'Seminar'),
        ('Workshop', 'Workshop'),
        ('Other', 'Other'),
    ]  
  tag = models.CharField(max_length=100, choices=TAG_CHOICES)
  date = models.DateTimeField(auto_now_add=True)