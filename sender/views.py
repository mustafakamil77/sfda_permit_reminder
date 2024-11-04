from django.shortcuts import redirect, render

from .forms import NewPermitForm
from .models import SdfaPermit

def AllPermit(request):
    Allpermit = SdfaPermit.objects.all()

    return render(request, 'index.html', {'Allpermit': Allpermit})

def PermitForm(request):
    if request.method == 'POST':
        form = NewPermitForm(request.POST)

        if form.is_valid():
            myform = form.save(commit=False)
            myform.save()

            return redirect('index')        
    else:
        form = NewPermitForm()

    return render(request, "forms.html", {'form': form})

def Edit_Permit(request, SdfaPermit_id):
    Editpermit= SdfaPermit.objects.get(pk=SdfaPermit_id)
    form = NewPermitForm(request.POST or None, instance=Editpermit)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('index')  # assuming there is a URL pattern named 'permit-list'

    return render(request, "edit.html", {'Editpermit': Editpermit, 'form': form})

def DeleteSdfaPermit(request, Delete_SdfaPermit):
    Deletepermit= SdfaPermit.objects.get(pk=Delete_SdfaPermit)
    Deletepermit.delete()