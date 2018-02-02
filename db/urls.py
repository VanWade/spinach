from django.conf.urls import url
from . import views

urlpatterns = [
    url('db.html', views.DbListAll.as_view(), name='db_list'),
    url('db-add.html', views.DbAdd.as_view(), name='db_add'),
    url('db-del.html', views.DbDel.as_view(), name='db_del'),
    url('db-all-del.html', views.db_all_del, name='db_all_del'),
    url('db-update-<int:pk>.html', views.DbUpdate.as_view(), name='db_update'),
    url('asset-detail-<int:pk>.html', views.DbDetail.as_view(), name='db_detail'),
    url('db-user.html', views.DbUserListAll.as_view(), name='db_user_list'),
    url('db-user-add.html', views.DbUserAdd.as_view(), name='db_user_add'),
    url('db-user-update-<int:pk>.html', views.DbUserUpdate.as_view(), name='db_user_update'),
    url('db-user-del.html', views.DbUserDel.as_view(), name='db_del'),
    url('db-user-detail-<int:pk>.html', views.DbUserDetail.as_view(), name='db_user_detail'),
    url('db-user-db-<int:nid>.html', views.Db_user_db, name='db_user_db'),
]

app_name = "db"
