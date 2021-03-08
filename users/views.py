from django.shortcuts import render
from .forms import CreateUser
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

@login_required
def create_user(request):
    if request.method == 'POST':
        form = CreateUser(request.POST)
        if form.is_valid():
            form.save()
            #username = form.cleaned_data.get('username')
            #messages.succes(request, f'User created for {username}')
            return redirect('dashboard-users')
    else:
        form = CreateUser()
    return render(request, 'users/createUser.html', {'form': form})

