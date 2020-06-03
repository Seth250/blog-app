from django.shortcuts import render
from django.views.generic import (
	ListView
)

# Create your views here.

def home(request):
	return render(request, 'blog/post_list.html', {})