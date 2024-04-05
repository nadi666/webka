from django.urls import path
from . import views

app_name = 'report'

urlpatterns = [

    path('daily_report', views.daily_report, name='daily_report'),

    path('view_report/<int:pk>/', views.view_report, name='view_report'),
    path('daily_create/', views.daily_create, name='daily_create'),
    path('edit_report/<int:pk>/', views.edit_report, name='edit_report'),
    path('delete_report/<int:pk>/', views.delete_report, name='delete_report'),
    path('filter/', views.daily_report_filter, name='daily_report_filter'),
    path('manager_create/', views.manager_create, name='manager_create'),
    path('daily_report/', views.daily_report_by_date, name='daily_report_by_date'),
    path('view_reports_by_date/', views.view_reports_by_date, name='view_reports_by_date'),
    path('summary/', views.summary_report, name='summary_report'),
    path('summary_second/', views.summary_report_second, name='summary_report_second'),

]