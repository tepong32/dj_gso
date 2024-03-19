from django.shortcuts import render
from django.contrib.auth.models import User
from django.core.paginator import Paginator

# for needing user to be logged-in first before accessing the page requested
from django.contrib.auth.decorators import login_required


@login_required
def home(request):
	users = User.objects.all()[:10],
	items = Item.objects.all().order_by("-date")
	paginator = Paginator(items, 10)  # Show 10 items per page
	page_number = request.GET.get('page')
	items_list = paginator.get_page(page_number)

	context = {
		# 'posts': Post.objects.all().order_by("-date_posted"),
		# 'announcements': Announcement.objects.all().order_by("-date_posted"),
		'users': users,
		'items': items_list
	}

	

	return render(request, 'home/index.html', context)


def about(request):
	user = User
	context = {}
	return render(request, 'home/about.html', context)



##################################################################################################
from django.shortcuts import render, get_object_or_404
from .models import Item, Category, SubCategory
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
	ListView,
	DetailView,
	CreateView,
	UpdateView,
	DeleteView,
	FormView,
	)
from .forms import ItemForm
from django.http import HttpResponseRedirect
from django.urls import reverse





# trying out multiple objects inside one class-based listView template
class HomeView(ListView):
    context_object_name = 'items'    
    template_name = 'home/home.html'
    queryset = Item.objects.all()
    ordering = ['-date_posted']			# filter for newest post first
    paginate_by = 10					# number of posts to show per page

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        '''
        	This function was used to override the "context" variable on the class-based view.
        	Think of this as a way of doing 
        	context = { 'xxx': xxx.objects.all(),
        				'yyy': yyy.objects.all()
        				}
        	in a function-based view.
        	See 'home.views.home' for a better reference.
        '''
        # context['entertainment'] = blogPost.objects.filter(tag="Entertainment").order_by('-date_posted')
        # context['help'] = blogPost.objects.filter(tag="Help!").order_by('-date_posted')
        # context['hobby'] = blogPost.objects.filter(tag="Hobby").order_by('-date_posted')
        # context['jokes'] = blogPost.objects.filter(tag="Jokes").order_by('-date_posted')
        # context['school'] = blogPost.objects.filter(tag="School").order_by('-date_posted')
        # context['social'] = blogPost.objects.filter(tag="Social").order_by('-date_posted')
        # context['reminders'] = BlogReminder.objects.all()
        # and so on for more models
        return context


# class UserPostFilter(ListView):
# 	model = Item 			
# 	template_name = 'home/userposts.html'
# 	context_object_name = 'items'		# getting the 'posts' key from "context = {'items': Item.objects.all(),}"
# 	ordering = ['-date']
# 	paginate_by = 10	

# 	def get_queryset(self):		# this defines the filter for the specific user's posts
# 		user = get_object_or_404(User, username=self.kwargs.get('username'))
# 		return Item.objects.filter(added_by=user).order_by('-date')


class ItemDetailView(DetailView): # LoginRequiredMixin for authed users
	model = Item
	template_name = 'home/itemdetail.html'
	items = Item.objects.all()
	context = {
		'items': items,
		# 'comments': PostComment.objects.filter(post=posts),
	}


class ItemCreateView(LoginRequiredMixin, CreateView):		
	model = Item
	form_class = ItemForm
	template_name = 'home/itemcreateform.html'
	success_message = "Successfully posted!"
	success_url = '/'		# using this takes the user to a specific page after posting

	def form_valid(self, form):			# to automatically get the id of the current logged-in user as the author
		form.instance.added_by = self.request.user 	# set the author to the current logged-in user
		return super().form_valid(form)
		

class ItemUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
	model = Item 
	form_class = ItemForm	# blogPostForm was the one used in the tutorials
	template_name = 'home/itemupdateform.html'
	success_message = "Item updated"
	# success_url = '/blog'

	def form_valid(self, form):			
		form.instance.added_by = self.request.user 	#to automatically get the id of the current logged-in user as the author
		return super().form_valid(form)

	def test_func(self):
		item = self.get_object()

		if self.request.user == item.added_by:
			return True
		return False


class ItemDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):		
	model = Item
	template_name = 'home/itemconfirmdelete.html'
	success_url = '/'

	def form_valid(self, form):
		form.instance.added_by = self.request.user
		return super().form_valid(form)

	def test_func(self):
		item = self.get_object()

		if self.request.user == item.added_by:
			return True
		return False		

