from django.conf.urls import include, url
from django.contrib import admin

from names.views import index, login_view, logout
from asset.views import AssetUpload
from django.conf import settings

import xadmin

xadmin.autodiscover()

from xadmin.plugins import xversion

xversion.register_models()

urlpatterns = [
    url('admin/', xadmin.site.urls, name="xadmin"),
    url('dadmin/', admin.site.urls, name="dadmin"),
    url('^$', index),
    url('^login/$', login_view, name="login_view"),
    url('logout.html', logout, name="logout"),
    url('index.html', index),
    url('asset/', include('asset.urls', namespace="asset", ), ),
    url('db/', include('db.urls', namespace="db", ), ),
    url('tasks/', include('tasks.urls', namespace="tasks", ), ),
    url('names/', include('names.urls', namespace="names", ), ),
    url('library/', include('library.urls', namespace="library", ), ),
    url('upload/', AssetUpload.as_view()),
    url('ueditor/', include('DjangoUeditor.urls')),
    url('release/', include('release.urls', namespace="release")),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
]

if settings.DEBUG:
    from django.conf.urls.static import static

    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
