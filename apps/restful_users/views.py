from django.shortcuts import render, redirect
from .models import User

# Create your views here.
def index_and_create(request):
	context = {
		"all_users": User.objects.all()
	}
	if request.method == 'POST':
		User.objects.create(first_name = request.POST ['first_name'], last_name = request.POST ['last_name'], email = request.POST['email'])
		return redirect('/users')

	return render(request, 'restful_users/index.html', context)


def users_new(request): 
	return render(request, 'restful_users/users.html')


def users_show_and_update(request, user_id):
	if request.method == "POST":
		the_user = User.objects.filter(id = user_id)
		the_user.update(first_name = request.POST ['first_name'], last_name = request.POST ['last_name'], email = request.POST['email'])
		return redirect ('/users')
	else:
		the_user = User.objects.get(id=user_id)
		context = {
		"user": the_user
		}
		return render(request,'restful_users/users_show.html', context)

def users_edit(request, user_id): 
	the_user = User.objects.get(id = user_id)
	context = {
	"user": the_user
	}
	return render(request, 'restful_users/users_edit.html', context)

def users_delete(request, user_id):
	User.objects.get(id = user_id). delete()
	return redirect('/users')