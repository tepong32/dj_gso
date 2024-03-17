from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# for needing user to be logged-in first before accessing the page requested
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
	user = User
	context = {
		# 'posts': Post.objects.all().order_by("-date_posted"),
		# 'announcements': Announcement.objects.all().order_by("-date_posted"),
		'users': User.objects.all()[:5],
	}
	return render(request, 'home/index.html', context)


def about(request):
	user = User
	context = {}
	return render(request, 'home/about.html', context)


