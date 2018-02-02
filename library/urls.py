from django.conf.urls import url

from . import views

urlpatterns = [
    url('library.html', views.LibraryListAll.as_view(), name='library_list'),
    url('library-add.html', views.LibraryAdd.as_view(), name='library_add'),
    url('library-update-<int:pk>.html', views.LibraryUpdate.as_view(), name='library_update'),
    url('library-del.html', views.LibraryDel.as_view(), name='library_del'),
    url('library-detail-<int:pk>.html', views.LibraryDetail.as_view(), name='library_detail'),
]

app_name = "library"
