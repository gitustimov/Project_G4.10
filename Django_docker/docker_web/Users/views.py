from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views import View


class MyView(View):
    def get(self, request):
        if not User.objects.filter(username='admin',).exists():
            User.objects.create_superuser(username='admin', password='1234567', email='admin@mail.ru')
        return redirect('admin/')
