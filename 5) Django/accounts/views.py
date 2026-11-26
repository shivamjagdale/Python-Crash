from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

# Create your views here.

def register(request):

    # Check what type of request it is 
    if request.POST != "POST":
        form = UserCreationForm()
    else:
        form = UserCreationForm(data = request.POST)

        if form.is_valid():
            # save the new user
            new_user = form.save()

            # We automatically log them in 
            login(request, new_user)

            # redirect 
            return redirect("learning_log:index")

    # context and render
    context = {"form":form}
    return render(request, "registration/register.html", context)