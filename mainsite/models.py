from django.db import models


# Create your models here.
class jobList(models.Model):
    job_name = models.CharField(max_length=30)
    job_url = models.CharField(max_length=200)
    job_dec = models.CharField(max_length=30, null=True)
    isGetDetail = models.BooleanField(default=False)
    job_type = models.CharField(max_length=30, null=True)
    salaryMean = models.FloatField(null=True)
    salaryMedian = models.FloatField(null=True)
    salaryVar = models.FloatField(null=True)
    salaryStd = models.FloatField(null=True)
    workYearMean = models.FloatField(null=True)
    keyWord = models.TextField(null=True)

    class META:
        ordering = ['job_name']

    def __str__(self):
        return self.job_name


class java_job(models.Model):
    jobType = models.CharField(max_length=30, null=True)
    positionId = models.CharField(max_length=30, unique=True)
    companyFullName = models.CharField(max_length=100)
    detail_url = models.CharField(max_length=200)
    salary = models.CharField(max_length=30)
    district = models.CharField(max_length=30)
    workYear = models.CharField(max_length=30)
    education = models.CharField(max_length=30)
    createTime = models.CharField(max_length=30)
    positionLables = models.CharField(max_length=200)
    positionDetail = models.TextField()
    firstType = models.CharField(max_length=200)
    secondType = models.CharField(max_length=200)
    salaryOne = models.FloatField(default=1.0)
    workYearAvr = models.FloatField(default=0.0)

    class META:
        ordering = ['jobType']

    def __str__(self):
        return self.positionId


class learning(models.Model):
    learnType = models.CharField(max_length=30, null=True)
    learnURL = models.CharField(max_length=200)
    learnLabel = models.CharField(max_length=100, null=True)
    webName = models.CharField(max_length=30, null=True)
    learnDetail = models.CharField(max_length=200, null=True)
    learnLevel = models.CharField(max_length=20, null=True)
    learnPersons = models.CharField(max_length=20, null=True)

    class META:
        ordering = ['learnType']

    def __str__(self):
        return self.learnType + self.learnLabel
