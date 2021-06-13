from django.urls import path, include, re_path
from mainapp import views
from rest_framework.urlpatterns import format_suffix_patterns


broadcast_id_viewset = views.BroadCastIdViewSet.as_view()

url_patterns = [path('broadcast_id/', broadcast_id_viewset, name = "broadcast-id-url")]

urlpatterns = format_suffix_patterns(url_patterns)

