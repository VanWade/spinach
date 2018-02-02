from django.conf.urls import url

from . import views

urlpatterns = [
    url('login-history.html', views.login_history, name="login_history"),
    url('password.html', views.password_update, name="password_update"),
    url('web-history.html', views.web_historys, name='web_history'),
    url('cmd-history.html', views.cmd_historys, name='cmd_history'),
]

app_name = "names"
