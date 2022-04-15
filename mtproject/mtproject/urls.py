from django.contrib import admin
from django.urls import path
from django.urls.conf import include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('mt.urls',namespace="근로장_목록")),
    
    path('근로장_목록/',include('mt.urls',namespace="근로장_목록")),
    path('근로자_목록/',include('mt.urls',namespace="근로자_목록")),



    
    # path('근로자_목록/',include('mt.urls', namespace="근로자_목록")),
    # path('workplace/', 근로장),

]
