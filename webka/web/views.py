from django.shortcuts import render, redirect, get_object_or_404
from django.db.models import Sum
from .models import DailyReport, Manager
from .forms import DailyReportForm, ManagerForm
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponseForbidden
from datetime import datetime, timezone


def daily_report(request):
    reports = DailyReport.objects.all().order_by('report_date')
    today = datetime.today()
    return render(request, 'web/index.html', {'reports': reports, 'today': today})

def view_report(request, pk):
    report = get_object_or_404(DailyReport, pk=pk)
    return render(request, 'web/student_list.html', {'report': report})

def daily_create(request):
    if request.method == 'POST':
        form = DailyReportForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report:daily_report')
    else:
        form = DailyReportForm()
    return render(request, 'web/daily_report_form.html', {'form': form})

def edit_report(request, pk):
    report = get_object_or_404(DailyReport, pk=pk)
    form = DailyReportForm(request.POST or None, instance=report)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('report:daily_report')
    return render(request, 'web/daily_report_form.html', context)

def delete_report(request, pk):
    report = get_object_or_404(DailyReport, pk=pk)
    report.delete()
    return redirect('report:daily_report')

def daily_report_filter(request):
    if request.method == 'POST':
        month = request.POST.get('month')
        if month == '0':
            reports = DailyReport.objects.all().order_by('report_date')
        else:
            reports = DailyReport.objects.filter(report_date__month=month)
    else:
        reports = DailyReport.objects.all().order_by('report_date')

    today = datetime.today()
    return render(request, 'web/index.html', {'reports': reports, 'today': today})

def manager_create(request):
    if request.method == 'POST':
        form = ManagerForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('report:daily_report')
    else:
        form = ManagerForm()
    return render(request, 'web/daily_report_form.html', {'form': form})

def edit_manager(request, pk):
    manager = get_object_or_404(Manager, pk=pk)
    form = ManagerForm(request.POST or None, instance=manager)
    context = {'form': form}
    if form.is_valid():
        form.save()
        return redirect('report:daily_report')
    return render(request, 'web/daily_report_form.html', context)

def delete_manager(request, pk):
    report = get_object_or_404(Manager, pk=pk)
    report.delete()
    return redirect('daily_report')

#админка
def daily_report_by_date(request, year, month, day):
    date = datetime.date(year, month, day)
    reports = DailyReport.objects.filter(report_date=date)
    return render(request, 'web/daily_report_by_date.html', {'reports': reports, 'date': date})

@user_passes_test(lambda u: u.is_superuser)
def summary_report(request):
    if request.method == 'POST':
        access_code = request.POST.get('access_code')
        # Проверка кода доступа
        if access_code == 'ваш_код_доступа':
            # Логика для администратора
            pass
        else:
            return HttpResponseForbidden("Доступ запрещен. Неверный код доступа.")
    return render(request, 'web/summary_report.html')

def view_reports_by_date(request):
    if request.method == 'POST':
        report_date = request.POST.get('report_date')
        reports = DailyReport.objects.filter(report_date=report_date)
        return render(request, 'student_db/daily_report_by_date.html', {'reports': reports, 'report_date': report_date})
    else:
        return render(request, 'web/daily_report_by_date.html')


def summary_report_second(request):
    if request.method == 'POST':
        month = request.POST.get('month')
        year = datetime.today().year
        reports = DailyReport.objects.filter(report_date__year=year, report_date__month=month)
        total_sum = reports.aggregate(Sum('report_sum'))['report_sum__sum']
        return render(request, 'web/summary_report.html', {'reports': reports, 'total_sum': total_sum})
    else:
        return render(request, 'web/summary_report.html')