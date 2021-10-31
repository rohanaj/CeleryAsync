from django.urls import path,include
from .views import MyView, TestDriver

urlpatterns = [
           path("test", MyView.as_view(),name="myview"),
            path("driver", TestDriver.as_view(), name="driver")        
        ]
