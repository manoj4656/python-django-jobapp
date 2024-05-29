from django.urls import path
# from app.views import job_detail
# from . import views
from app import views

urlpatterns = [
    path('',views.job_list,name='jobs_home'),
    path('hello/',views.hello,name='hello'),
    path('job/<int:id>',views.job_detail,name='jobs_detail'),
]