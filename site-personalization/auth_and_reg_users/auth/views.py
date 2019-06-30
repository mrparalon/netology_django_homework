from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages


def home(request):
    return render(
        request,
        'home.html'
    )

def logout(request):
    return render(request, 'logout.html')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Аккаунт создан!')
            return redirect('home')
    else:
        form = UserCreationForm()

    context = {'form': form}
    return render(
        request,
        'signup.html',
        context=context
    )
