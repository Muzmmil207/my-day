from django.urls import path
from .views import home, chart_view, js_chart, logout_user

urlpatterns = [
    path('', home, name="home"),
    path('chart-view/<str:id>', chart_view, name="chart_view"),
    path('js-chart/<str:id>', js_chart, name="js-chart"),

]
