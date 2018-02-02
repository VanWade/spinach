from django.conf.urls import url

from . import views

urlpatterns = [
    url('release.html', views.ReleaseListAll.as_view(), name='release_list'),
    url('release-add.html', views.ReleaseAdd.as_view(), name='release_add'),
    url('release-del.html', views.ReleaseDel.as_view(), name='release_del'),
    url('release-update-<int:pk>.html', views.ReleaseUpdate.as_view(), name='release_update'),
    url('release-upload-<int:pk>.html', views.ReleaseUpload.as_view(), name='release_upload'),
    url('release-upload.html', views.ReleaseUploadPost.as_view(), name='release_upload_post'),
]

app_name = "release"
