from django.shortcuts import render,  redirect
from .models import chart, index
from django.http import JsonResponse, HttpResponse
from .forms import ChartForm, IndexForm
from operator import mul
import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout

# Create your views here.


@login_required(login_url="/accounts/login/")
def home(request):
    chart_data = chart.objects.filter(user=request.user.id)

    if request.method == 'POST':
        form = ChartForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.user = request.user
            data.save()
            return redirect('home')

    form = ChartForm()

    context = {'cr': chart_data, 'form': form}
    return render(request, 'app/index.html', context)


@login_required(login_url="/accounts/login/")
def chart_view(request, id):
    chart_data = chart.objects.get(id=id)
    chart_item = chart_data.chart_index.all().order_by('-date_create')

    if request.user != chart_data.user:
        return HttpResponse("PAGE NOT FOUND")
    if request.method == 'POST':
        form = IndexForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.chart = chart_data
            data.save()

            return redirect('chart_view', id=id)

    context = {'char': chart_data, 'chart_item': chart_item}
    return render(request, 'app/chart-view.html', context)


def logout_user(request):
    logout(request)
    return redirect("/accounts/login/")


@login_required(login_url="/accounts/login/")
def js_chart(request, id):
    jsObj = []
    chart_data = chart.objects.get(id=id)
    json_chart = chart_data.chart_index.all().order_by('-date_create')

    for i in json_chart:
        if chart_data.choices == 'Time Chart':
            my_time = i.time_value
            my_time = str(my_time)
            print(my_time)
            factors = (60, 1, 1/60)
            t1 = sum(ti*j for ti, j in zip(map(int, my_time.split(':')), factors))
            jsObj.append({i.labels: t1})
        elif chart_data.choices == 'Integer Chart':
            jsObj.append({i.labels: i.int_value})
    jsObj = jsObj[:10]
    return JsonResponse(jsObj, safe=False)
