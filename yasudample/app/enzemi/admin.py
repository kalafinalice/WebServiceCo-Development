from django.contrib import admin
from .models import EmployeeList

"""
ブラウザ上のadminサイトで編集できるものを設定
"""
admin.site.register(EmployeeList)
