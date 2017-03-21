from django import forms
from .models import EmployeeList, MorningTaskMaster, MajorClassificationMaster, SmallClassificationMaster

"""
ここでフォームを自動生成することができる
"""

class EmployeeListForm(forms.ModelForm):
    class Meta:
        model = EmployeeList
        fields = [
            'employee_id',
            'email',
            'pc_address',
            'mobile_address',
            'password',
            'name',
            'position',
            'control_level',
            'work_start_time',
            'work_finish_time',
            'detination',
            'work_day',
        ]

    """
    表示の設定をしたい場合は以下に記入
    """
    name = forms.CharField(required=False, label="名前", widget=forms.TextInput(attrs={'class': 'form-control input-xm'}))
    email = forms.CharField(required=False, label="メール", widget=forms.TextInput(attrs={'class': 'form-control input-xm'}))
    password = forms.CharField(required=False, label="パスワード", widget=forms.TextInput(attrs={'class': 'form-control input-xm'}))
    employee_id = forms.DecimalField(required=False, label="社員ID", widget=forms.TextInput(attrs={'class': 'form-control input-xm'}))
    pc_mail_address = forms.EmailField(required=False, label="メールアドレス（PC）", widget=forms.TextInput(attrs={'class': 'form-control input-xm'}))
    mobile_mail_address = forms.EmailField(required=False, label="メールアドレス（携帯）", widget=forms.TextInput(attrs={'class': 'form-control input-xm'}))

class MorningTaskMasterForm(forms.ModelForm):
    class Meta:
        model = MorningTaskMaster
        fields = [
            "task_name",
            "major_classification",
            "small_classification",
            "importance",
            "start_time",
            "finish_time",
            "remark",
            "comment",
        ]

    task_name = forms.CharField(required=False, label="タスク", widget=forms.TextInput(attrs={'class': 'form-control input-xm'}))
    major_classification = forms.ModelChoiceField(MajorClassificationMaster.objects, empty_label='選択してください', widget=forms.Select(attrs={'class': 'form-control input-xm select'}))
    small_classification = forms.ModelChoiceField(SmallClassificationMaster.objects, empty_label='選択してください', widget=forms.Select(attrs={'class': 'form-control input-xm select'}))
    importance = forms.DecimalField(required=False, widget=forms.TextInput(attrs={'class': 'form-control input-xm'}))
    start_time    = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'form-control input-xm'}))
    finish_time    = forms.DateField(required=False, widget=forms.TextInput(attrs={'class': 'form-control input-xm'}))
    remark = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control input-xm'}))
    comment = forms.CharField(required=False, widget=forms.TextInput(attrs={'class': 'form-control input-xm'}))
