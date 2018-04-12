import re

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import jobList, java_job, learning
from datetime import datetime
from django.shortcuts import redirect
from .forms import JobForm, JobDetailForm


# Create your views here.
def homepage(request):
    user = request.user if request.user.is_authenticated() else None
    jobs = jobList.objects.filter(isGetDetail=1)
    jobs_tech = jobList.objects.filter(isGetDetail=1, job_type='技术')
    jobs_untech = jobList.objects.filter(isGetDetail=1, job_type='非技术')
    form = JobForm()
    return render(request, 'mainpage/index.html', locals())


def showjobs(request, name):
    user = request.user if request.user.is_authenticated() else None
    try:
        job = jobList.objects.get(job_name=name, isGetDetail=1)
        nowtime = datetime.now()
        if job != None:
            return render(request, 'mainpage/job.html', locals())
        else:
            return redirect('/')
    except:
        return redirect('/')


keyWordOut = ['以上学历', '以上', '相关', '具备', '了解', '至少', '常用', ]


def keyWordCloud_filter(keyWord_re):
    for x in keyWordOut:
        try:
            keyWord_re.remove(x)
        except:
            continue


def show_job_detail(request, name):
    user = request.user if request.user.is_authenticated() else None
    learn = learning.objects.filter(learnType__icontains=name)
    try:
        job_detail = java_job.objects.filter(jobType=name)
        job_name = name
        keyWord = 'img/' + name + '_keyWord.png'
        job_first_label = job_detail[0].firstType
        job_second_label = job_detail[0].secondType
        data = {}
        workYear = {}
        education = {}
        for x in job_detail:
            if x.workYearAvr == 0:
                incrDictEntry(workYear, '不限', 1)

            else:
                incrDictEntry(workYear, str(x.workYearAvr) + '年', 1)
            incrDictEntry(education, x.education, 1)
            if x.salaryOne >= 40:
                incrDictEntry(data, '40k以上', 1)
            elif x.salaryOne >= 35:
                incrDictEntry(data, '35k-40k', 1)
            elif x.salaryOne >= 30:
                incrDictEntry(data, '30k-35k', 1)
            elif x.salaryOne >= 25:
                incrDictEntry(data, '25k-30k', 1)
            elif x.salaryOne >= 20:
                incrDictEntry(data, '20k-25k', 1)
            elif x.salaryOne >= 15:
                incrDictEntry(data, '15k-20k', 1)
            elif x.salaryOne >= 10:
                incrDictEntry(data, '10k-15k', 1)
            elif x.salaryOne >= 5:
                incrDictEntry(data, '5k-10k', 1)
            else:
                incrDictEntry(data, '5k以下', 1)
        this_job = jobList.objects.filter(job_name__iexact=name)
        keyWord_re = this_job[0].keyWord.split(' ')[:-1]
        keyWordCloud_filter(keyWord_re)
        keyWordCloud = {}
        for i in range(len(keyWord_re)):
            keyWordCloud[keyWord_re[i]] = 1000 - i * 20
        content = {
            'user': user,
            'job_detail': job_detail,
            'job_name': job_name,
            'job_first_label': job_first_label,
            'job_second_label': job_second_label,
            'data': data,
            'learn': learn,
            'keyWord': keyWord,
            'workYear': workYear,
            'keyWordCloud': keyWordCloud,
            'education': education,
        }
        if len(job_detail) != 0:
            return render(request, 'mainpage/job_detail.html', content)
        else:
            return redirect('/')
    except:
        return redirect('/')


def homepage_search(request):
    user = request.user if request.user.is_authenticated() else None
    form = JobForm()

    JobName = request.GET['JobName']
    JobType = request.GET['JobDec']
    if JobType == '所有':
        jobs = jobList.objects.filter(job_name__icontains=JobName, isGetDetail=1)
        jobs_tech = jobList.objects.filter(job_name__icontains=JobName, isGetDetail=1, job_type='技术')
        jobs_untech = jobList.objects.filter(job_name__icontains=JobName, isGetDetail=1, job_type='非技术')
    else:
        jobs = jobList.objects.filter(job_name__icontains=JobName, job_dec=JobType, isGetDetail=1)
        jobs_tech = jobList.objects.filter(job_name__icontains=JobName, job_dec=JobType, isGetDetail=1, job_type='技术')
        jobs_untech = jobList.objects.filter(job_name__icontains=JobName, job_dec=JobType, isGetDetail=1,
                                             job_type='非技术')
    return render(request, 'mainpage/index.html', locals())


def signup(request):
    # if request.user.is_authenticated():  # 已经登陆过的账号
    #     return HttpResponseRedirect(reverse('homepage'))
    # state = None
    if request.method == 'POST':
        password = request.POST.get('password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if password == '' or repeat_password == '':  # 输入密码为空
            state = 'empty'
        elif password != repeat_password:  # 输入的密码前后不一致
            state = 'repeat_error'
        else:
            username = request.POST.get('username', '')  # 获取用户名
            if User.objects.filter(username=username):
                state = 'user_exist'  # 用户名应存在
            else:
                new_user = User.objects.create_user(username=username, password=password,
                                                    email=request.POST.get('email', ''))
                new_user.save()
                state = 'success'
        content = {
            'active_menu': 'homepage',
            'state': state,
            'user': None,
        }
        return render(request, 'mainpage/signup.html', content)
    else:
        return render(request, 'mainpage/signup.html')


def my_login(request):
    # if request.user.is_authenticated():
    #     return HttpResponseRedirect(reverse('homepage'))
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect(reverse('homepage'))
        else:
            state = 'not_exist_or_password_error'
        content = {
            'active_menu': 'homepage',
            'state': state,
            'user': None
        }
        return render(request, 'mainpage/login.html', content)
    else:
        return render(request, 'mainpage/login.html')


def logout(request):
    auth.logout(request)
    return HttpResponseRedirect(reverse('homepage'))


@login_required  # django内置用法，只有登录过的才可以浏览，如果还没有登录就进行访问，就先登录括号中的网址。
def set_password(request):
    user = request.user
    state = None
    if request.method == 'POST':
        old_password = request.POST.get('old_password', '')
        new_password = request.POST.get('new_password', '')
        repeat_password = request.POST.get('repeat_password', '')
        if user.check_password(old_password):
            if not new_password:
                state = 'empty'
            elif new_password != repeat_password:
                state = 'repeat_error'
            else:
                user.set_password(new_password)
                user.save()
                state = 'success'
        else:
            state = 'password_error'
    content = {
        'user': user,
        'active_menu': 'homepage',
        'state': state,
    }
    return render(request, 'mainpage/set_password.html', content)


@login_required  # django内置用法，只有登录过的才可以浏览，如果还没有登录就进行访问，就先登录括号中的网址。
def myInfo(request):
    user = request.user

    return render(request, 'mainpage/info.html', locals())


def incrDictEntry(d, k, v):
    if d.__contains__(k):
        d[k] += v
    else:
        d[k] = v


def job_detail_search(request, name):
    user = request.user if request.user.is_authenticated() else None
    learn = learning.objects.filter(learnType__icontains=name)
    positionLabel = request.GET['positionLabel']
    district = request.GET['district']
    salary = request.GET['salary']
    education = request.GET['education']
    salary_list = []
    if salary == '所有':
        salary_list = [0, 100000]
    elif salary == '35k-40k':
        salary_list = [35, 40]
    elif salary == '30k-35k':
        salary_list = [30, 35]
    elif salary == '25k-30k':
        salary_list = [25, 30]
    elif salary == '20k-25k':
        salary_list = [20, 25]
    elif salary == '15k-20k':
        salary_list = [15, 20]
    elif salary == '10k-15k':
        salary_list = [10, 15]
    elif salary == '5k-10k':
        salary_list = [5, 10]
    else:
        salary_list = [0, 5]
    if positionLabel == '所有':
        job_detail = java_job.objects.filter(jobType=name, district__icontains=district,
                                             salaryOne__gte=salary_list[0],
                                             salaryOne__lte=salary_list[1])
    else:
        job_detail = java_job.objects.filter(jobType=name, district__icontains=district,
                                             salaryOne__gte=salary_list[0],
                                             salaryOne__lte=salary_list[1],
                                             positionDetail__icontains=positionLabel)
    if education != '所有':
        job_detail = job_detail.filter(education__icontains=education)
    # salaryOne__gte=salary[0],salaryOne__lte=salary[1]
    job_name = name
    keyWord = 'img/' + name + '_keyWord.png'
    data = {}
    workYear = {}
    education = {}
    for x in job_detail:
        if x.workYearAvr == 0:
            incrDictEntry(workYear, '不限', 1)

        else:
            incrDictEntry(workYear, str(x.workYearAvr) + '年', 1)
        incrDictEntry(education, x.education, 1)
        if x.salaryOne >= 40:
            incrDictEntry(data, '40k以上', 1)
        elif x.salaryOne >= 35:
            incrDictEntry(data, '35k-40k', 1)
        elif x.salaryOne >= 30:
            incrDictEntry(data, '30k-35k', 1)
        elif x.salaryOne >= 25:
            incrDictEntry(data, '25k-30k', 1)
        elif x.salaryOne >= 20:
            incrDictEntry(data, '20k-25k', 1)
        elif x.salaryOne >= 15:
            incrDictEntry(data, '15k-20k', 1)
        elif x.salaryOne >= 10:
            incrDictEntry(data, '10k-15k', 1)
        elif x.salaryOne >= 5:
            incrDictEntry(data, '5k-10k', 1)
        else:
            incrDictEntry(data, '5k以下', 1)
    this_job = jobList.objects.filter(job_name__iexact=name)
    keyWord_re = this_job[0].keyWord.split(' ')[:-1]
    keyWordCloud_filter(keyWord_re)
    keyWordCloud = {}
    for i in range(len(keyWord_re)):
        keyWordCloud[keyWord_re[i]] = 1000 - i * 20
    # if len(job_detail) != 0:
    job_first_label = java_job.objects.filter(jobType=name)[0].firstType
    job_second_label = java_job.objects.filter(jobType=name)[0].firstType

    return render(request, 'mainpage/job_detail.html', locals())
    # else:
    #     return redirect('/')
