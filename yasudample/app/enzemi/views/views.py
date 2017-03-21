from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from enzemi.models import EmployeeList
from enzemi.forms import EmployeeListForm

def index(request):
    return render(
        request, 'task/edit.html',
    )

def settings(request):
    employee_list = EmployeeList.objects.get(id=1)
    form = EmployeeListForm(instance=employee_list)

    return render(
        request, 'enzemi/settings.html',
        {
            'employee_list': employee_list,
            'form'       : form,
            'form_action': reverse(settings_update),
        }
    )

def settings_update(request):
    employee_list = EmployeeList.objects.get(id=1)
    form = EmployeeListForm(instance=employee_list)
    print('settings_update called.')

    if request.method == 'POST':
        form = EmployeeListForm(request.POST, instance=employee_list)
        if form.is_valid():
            new_employee_list = form.save(commit=False)
            new_employee_list.id = 1
            success = form.save()
            print(success)
            return HttpResponseRedirect(reverse(settings))

        else:
            return render(
                request, 'enzemi/settings.html',
                {
                    'employee_list': employee_list,
                    'form'       :form,
                    'form_action': reverse(settings),
                }
            )
