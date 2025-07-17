from django.shortcuts import render
from rest_framework import generics, permissions
from django.contrib.auth.models import User
from .serializers import RegisterSerializer, UserSerializer
from rest_framework.response import Response
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .models import Habit, HabitCompletion
from .serializers import HabitSerializer, HabitCompletionSerializer
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from datetime import date

# Create your views here.

class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (permissions.AllowAny,)
    serializer_class = RegisterSerializer

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return self.request.user

class HabitViewSet(viewsets.ModelViewSet):
    serializer_class = HabitSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Habit.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['post'], url_path='toggle')
    def toggle(self, request, pk=None):
        habit = self.get_object()
        completion_date = request.data.get('date', str(date.today()))
        obj = HabitCompletion.objects.filter(habit=habit, date=completion_date).first()
        if obj:
            obj.delete()
            return Response({'status': 'unmarked', 'date': completion_date})
        else:
            HabitCompletion.objects.create(habit=habit, date=completion_date)
            return Response({'status': 'completed', 'date': completion_date})

    @action(detail=False, methods=['get'], url_path='statistics')
    def statistics(self, request):
        habits = self.get_queryset()
        total_habits = habits.count()
        completed_today = 0
        longest_streak = 0
        total_completions = 0
        today = date.today()
        streaks = []
        for habit in habits:
            completions = set([c.date for c in habit.completions.all()])
            total_completions += len(completions)
            # Completed today
            if today in completions:
                completed_today += 1
            # Calculate streak
            streak = 0
            current = today
            while current in completions:
                streak += 1
                current = current.fromordinal(current.toordinal() - 1)
            streaks.append(streak)
            if streak > longest_streak:
                longest_streak = streak
        avg_success = (total_completions / (total_habits or 1)) * 100
        return Response({
            'completed_today': completed_today,
            'total_habits': total_habits,
            'longest_streak': longest_streak,
            'average_success': round(avg_success, 2),
        })
