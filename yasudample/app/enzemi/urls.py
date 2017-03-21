from django.conf.urls import include, url
import django.contrib.auth.views
from enzemi.views import views, task, individual, team

from django.conf import settings

"""
URLのルーティング
凡例：url(アクセス先, ビューの該当するやつ（def以下）, {% url 'XXX' %}で呼び出すときの名前)
"""

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^settings$', views.settings, name='settings'),
    url(r'^settings/update$', views.settings_update, name='settings_update'),

    url(r'^task$', task.today, name='task'),
    url(r'^task/today$', task.today, name='task_today'),
    url(r'^task/new$', task.new, name='task_new'),
    url(r'^task/create$', task.create, name='task_create'),
    url(r'^task/edit$', task.edit, name='task_edit'),
    url(r'^task/update$', task.update, name='task_update'),

    url(r'^individual$', individual.analysis, name='individual'),
    url(r'^individual/analysis$', individual.analysis, name='individual_analysis'),

    url(r'^team$', team.analysis, name='team'),
    url(r'^team/analysis$', team.analysis, name='team_analysis'),
]
