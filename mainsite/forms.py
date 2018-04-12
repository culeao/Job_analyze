#!/usr/bin/evn python
# _*_ coding:utf-8 _*_
from django import forms


class JobForm(forms.Form):
    TYPE = [
        ['所有', '所有'],
        ['后端开发', '后端开发'],
        ['前端开发', '前端开发'],
        ['人工智能', '人工智能'],
        ['测试', '测试'],
        ['运维', '运维'],
        ['DBA', 'DBA'],
        ['高端职位', '高端职位'],
        ['项目管理', '项目管理'],
        ['硬件开发', '硬件开发'],
        ['企业软件', '企业软件'],
        ['产品经理', '产品经理'],
        ['产品设计师', '产品设计师'],
        ['视觉设计', '视觉设计'],
        ['交互设计', '交互设计'],
        ['用户研究', '用户研究'],
        ['运营', '运营'],
        ['编辑', '编辑'],
        ['客服', '客服'],
        ['市场营销', '市场营销'],
        ['公关', '公关'],
        ['销售', '销售'],
        ['供应链', '供应链'],
        ['采购', '采购'],
        ['投资', '投资'],
        ['人力资源', '人力资源'],
        ['行政', '行政'],
        ['财务', '财务'],
        ['法务', '法务'],
        ['投融资', '投融资'],
        ['风控', '风控'],
        ['审计税务', '审计税务'],
    ]
    JobName = forms.CharField(label='名称', max_length=30)
    JobDec = forms.ChoiceField(label='类型', choices=TYPE)


class JobDetailForm(forms.Form):
    TYPE_salary = [
        ['所有', [0, 100000]],
        ['40k以上', [40, 10000]],
        ['35k-40k', [35, 40]],
        ['30k-35k', [30, 35]],
        ['25k-30k', [25, 30]],
        ['20k-25k', [20, 25]],
        ['15k-20k', [15, 20]],
        ['10k-15k', [10, 15]],
        ['5k-10k', [5, 10]],
        ['5k以下', [0, 5]],
    ]
    TYPE_edu = [
        ['所有', '所有'],
        ['大专', '大专'],
        ['本科', '本科'],
        ['硕士', '硕士'],
        ['博士', '博士'],
        ['不限', '不限'],
    ]
    positionLabel = forms.CharField(label='标签', max_length=30)
    district = forms.CharField(label='地区', max_length=30)
    salary = forms.ChoiceField(label='薪金', choices=TYPE_salary)
    education = forms.ChoiceField(label='学历', choices=TYPE_edu)
