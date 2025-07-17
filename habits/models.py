from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Habit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='habits')
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    color = models.CharField(max_length=20)
    icon = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class HabitCompletion(models.Model):
    habit = models.ForeignKey(Habit, on_delete=models.CASCADE, related_name='completions')
    date = models.DateField()

    class Meta:
        unique_together = ('habit', 'date')

    def __str__(self):
        return f"{self.habit.name} on {self.date}"
