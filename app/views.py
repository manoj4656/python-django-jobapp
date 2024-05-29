from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseNotFound
from django.urls import reverse
from django.template import loader
from app.models import JobPost


job_title = [
    'First job',
    'Second job',
    'Third job'
]

job_description = [
    "First job description",
    "Second job description",
    "Third job description"
]

# Create your views here.
# def hello(request):
#     return HttpResponse('<h1>Hello user</h1>')

class TempClass:
    x = 5

def hello(request):
    # template = loader.get_template('hello.html')
    temp = TempClass()
    list = ['alpha','beta']
    is_authenticated = True
    context = {'name':'Django','first_list':list,'temp_object':temp,'is_authenticated':is_authenticated}
    # return HttpResponse(template.render(context,request))
    return render(request,"hello.html",context)

def job_list(request):
    # list_of_jobs = "<ul>"
    # for j in job_title:
    #     job_id = job_title.index(j)
    #     detail_url = reverse('jobs_detail',args=(job_id,))
    #     list_of_jobs += f"<li><a href='{detail_url}'>{j}</a></li>"
    # list_of_jobs += "</ul>"
    # return HttpResponse(list_of_jobs)
    jobs = JobPost.objects.all()
    context = {"jobs":jobs}
    return render(request,'index.html',context)

def job_detail(request,id):
    try:
        if id == 0:
            return redirect(reverse('jobs_home'))
        # return_html = f"<h1>{job_title[id]}</h1> <h3>{job_description[id]}</h3>"
        job = JobPost.objects.get(id=id)
        context = {"job":job}
        return render(request,'job_detail.html',context)
    except:
        return HttpResponseNotFound("Not Found")
