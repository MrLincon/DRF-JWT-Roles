from django.urls import path, include

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('auth/', include('account.urls'))
]
