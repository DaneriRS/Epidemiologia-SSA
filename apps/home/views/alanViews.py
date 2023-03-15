from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from apps.home.models import *
from apps.home.forms.allForms import *
from django.contrib.auth.models import User

from apps.home.views.allViews import roles_required

@login_required
@roles_required(['Director'])
def assign_groups(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == 'POST':
        form = GroupAssignForm(request.POST, instance=user)
        if form.is_valid():
            form.save()
    else:
        form = GroupAssignForm(instance=user)
    return render(request, 'home/assign_groups.html', {'form': form})