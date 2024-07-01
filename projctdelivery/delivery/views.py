from django.shortcuts import render
from delivery.models import User

# Create your views here.
u = User(name = 'test', email = 'test@gmail.com', password= '1234')
u.save()