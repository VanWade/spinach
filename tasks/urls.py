from django.conf.urls import url

from . import views

urlpatterns = [
    url('cmd.html', views.cmd, name='cmd'),
    url('tools.html', views.ToolsListAll.as_view(), name='tools'),
    url('tools-add.html', views.tools_add, name='tools_add'),
    url('tools-del.html', views.tools_delete, name='tools_delete'),
    url('tools-bulk-del.html', views.tools_bulk_delte, name='tools_bulk_delte'),
    url('tools-update-<int:nid>.html', views.tools_update, name='tools_update'),
    url('tools-script-<int:nid>.html', views.tools_script_get, name='tools_script_get'),
    url('tools-script.html', views.tools_script_post, name='tools_script_post'),
    url('Inception.html', views.Inception, name='Inception'),
    url('Inception-exe.html', views.Inception_exe, name='Inception_exe'),
    url('Inception-rb.html', views.Inception_rb, name='Inception_rb'),
    url('Inception-query.html', views.Inception_query, name='Inception_query'),
    url('Inception-query-databases.html', views.Inception_query_databases, name='Inception_query_databases'),
]

app_name = "tasks"
