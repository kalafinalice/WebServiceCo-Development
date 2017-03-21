from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse

from enzemi.models import MorningTaskMaster, NightTaskMaster
from enzemi.forms import MorningTaskMasterForm

def new(request):
    form_morning = MorningTaskMasterForm()

    return render(
        request, 'task/new.html',
        {
            "form_morning": form_morning,
        }
    )

def today(request):
    user = 3263512
    date = "2017/03/01"
    morning_task = MorningTaskMaster.get_task()
    #night_task_json = MorningTaskMaster.get_task(user, date)
    return render(
        request, 'task/show.html',
        {
            "morning_task": morning_task,
        }
    )


def today_json(request):
    """
    jsonなどに吐き出したい場合
    """
    # user = 3263512
    # date = "2017/03/01"
    # #morning_task_json = MorningTaskMaster.get_task(user, date)
    # #night_task_json = MorningTaskMaster.get_task(user, date)
    # return JsonResponse(morning_task_json, safe=False)
    pass


def create(request):
    if request.method == 'POST':
        form_morning = MorningTaskMasterForm(request.POST)

        if form_morning.is_valid():
            new_morning_task_master_form = form_morning.save(commit=False)
            # new_morning_task_master_form.create_user = request.user.id
            # new_morning_task_master_form.update_user = request.user.id

            success = form_morning.save()
            #logger.info('name: {0} id: {1} userid: {2}'.format(success.name, success.id, request.user.id))
            #views.message_create(success.id, success.name, request)

            return HttpResponseRedirect(reverse(new))

        else:
            #messages.error(request, 'エラー：更新されていません')

            return render(
                request, 'task/show.html',
                {
                    'form_morning':  form_morning,
                }
            )


def edit(request):
    return render(
        request, 'task/edit.html',
    )


def update(request):
    pass
