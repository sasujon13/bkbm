from django.views.static import serve
from django.conf.urls.static import static
from django.urls import path, re_path
from django.conf import settings
from . import views
from .views import (
    DivisionsView,
    DistrictsView,
    ThanasView,
    TeacherListAPIView,
    StaffListAPIView,
    ExTeacherListAPIView,
    ExStaffListAPIView,
    OtherPeopleListAPIView,
    TeacherHonoursListAPIView,
    NonMpoStaffListAPIView,
    NotificationExistsAPIView,
    TeacherPartListAPIView,
    DeptListAPIView,
    DepartmentDetailView,
    GallaryListView
    
)
urlpatterns = [
    path('divisions/', DivisionsView.as_view(), name='divisions'),
    path('districts/', DistrictsView.as_view(), name='districts'),
    path('thanas/', ThanasView.as_view(), name='thanas'),
    path('dept/', DeptListAPIView.as_view(), name='dept'),
    path('gallary/', GallaryListView.as_view(), name='gallary'),
    path('department/<str:Name>/', DepartmentDetailView.as_view(), name='department-detail'),
    path('teacher/', TeacherListAPIView.as_view(), name='teacher'),
    path('teacherPart/', TeacherPartListAPIView.as_view(), name='teacherPart'),
    path('teacherHonours/', TeacherHonoursListAPIView.as_view(), name='teacherHonours'),
    path('staff/', StaffListAPIView.as_view(), name='staff'),
    path('nonMpoStaff/', NonMpoStaffListAPIView.as_view(), name='nonMpostaff'),
    path('exTeacher/', ExTeacherListAPIView.as_view(), name='exTeacher'),
    path('exStaff/', ExStaffListAPIView.as_view(), name='exStaff'),
    path('otherPeople/', OtherPeopleListAPIView.as_view(), name='otherPeople'),
    path('notification/', NotificationExistsAPIView.as_view(), name='notification'),
    re_path(r'^favicon\.ico$', serve, {'path': 'static/favicon.ico'}),
    # re_path(r'^manage/media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
]

if settings.DEBUG:
    # urlpatterns += static('/manage' + settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    # urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)

# if settings.DEBUG:
#     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


