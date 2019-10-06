from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm


def register(request):
    form = UserRegisterForm(request.POST or None)

    if form.is_valid():
        form.save()
        messages.success(request, 'Your account has been created! '
                                  'You are now able to login.')
        return redirect('login')

    return render(request, 'users/register.html', {'form': form})


@login_required
def profile(request):
    u_form = UserUpdateForm(request.POST or None, instance=request.user)
    p_form = ProfileUpdateForm(request.POST or None, request.FILES,
                               instance=request.user.profile)

    if u_form.is_valid() and p_form.is_valid():
        u_form.save()
        p_form.save()

        messages.success(request, f'Your account has been updated!')
        return redirect('profile')

    context = {
        'u_form': u_form,
        'p_form': p_form
    }
    return render(request, 'users/profile.html', context)
