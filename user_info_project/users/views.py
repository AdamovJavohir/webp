from django.shortcuts import render, redirect
from .forms import UserInfoForm

# Create your views here.


def user_form_view(request):
    if request.method == 'POST':
        form = UserInfoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = UserInfoForm()
    return render(request, 'users/user_form.html', {'form': form})

def success_view(request):
    return render(request, 'users/success.html')