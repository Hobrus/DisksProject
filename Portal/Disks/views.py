from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import render, redirect, get_object_or_404

from .forms import DiskForm
from .models import Disk
from django.contrib.auth.decorators import login_required


# Create your views here.
def disk_list(request):
    disks = Disk.objects.all()
    return render(request, 'list.html', {'disks': disks})


@login_required
def disk_create(request):
    if request.method == 'POST':
        form = DiskForm(request.POST, request.FILES)
        if form.is_valid():
            disk = form.save(commit=False)
            disk.request = request
            disk.save()
            return redirect('disk_list')
    else:
        form = DiskForm()
    return render(request, 'create.html', {'form': form})


def disk_retrive(request, pk):
    disk = get_object_or_404(Disk, pk=pk)
    return render(request, 'retrieve.html', {'disk': disk})
