"""URL configuration for blogicum project."""

from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from pages.views import CustomLoginView, registration

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("blog.urls", namespace="blog")),
    path("pages/", include("pages.urls", namespace="pages")),
    path("auth/login/", CustomLoginView.as_view(), name="login"),
    path("auth/", include("django.contrib.auth.urls")),
    path("auth/registration/", registration, name="registration"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # раздача загруженных файлов через джанго сервер

handler404 = 'pages.views.page_not_found'
handler500 = 'pages.views.server_error'
handler403 = 'pages.views.csrf_failure'