from django.conf.urls import url
from . import api
from . import views

urlpatterns = [
    url('asset.html', views.AssetListAll.as_view(), name='asset_list'),
    url('asset-add.html', views.AssetAdd.as_view(), name='asset_add'),
    url('asset-del.html', views.AssetDel.as_view(), name='asset_del'),
    url('asset-all-del.html', views.AssetAllDel.as_view(), name='asset_all_del'),
    url('asset-detail-<int:pk>.html', views.AssetDetail.as_view(), name='asset_detail'),
    url('asset-update-<int:pk>.html', views.AssetUpdate.as_view(), name='asset_update'),
    url('asset-hardware-update.html', views.asset_hardware_update, name='asset_hardware_update'),
    url('asset-performance-<int:nid>.html', views.asset_performance, name='asset_performance'),
    url('asset-webssh.html', views.asset_web_ssh, name='asset_web_ssh'),
    url('system-user.html', views.SystemUserListAll.as_view(), name='system_user'),
    url('system-user-asset-<int:nid>.html', views.system_user_asset, name='system_user_asset'),
    url('system-user-add.html', views.system_user_add, name='system_user_add'),
    url('system-user-del.html', views.SystemUserDelete.as_view(), name='system_user_del'),
    url('system-user-detail-<int:nid>.html', views.system_user_detail, name='system_user_detail'),
    url('system-user-update-<int:nid>.html', views.system_user_update, name='system_user_update'),
    url('api/asset.html', api.AssetList.as_view(), name='asset_api_list'),
    url('api/asset-detail-<int:pk>.html', api.AssetDetail.as_view(), name='asset_api_detail'),
    url('asset-export.html', views.export, name='asset_export'),
]

app_name = "asset"
