from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path
from . import views

urlpatterns = [
    path("login", views.user_login_view, name="login"),
    path("employee/list-account", views.find_employee, name="list-EmpID"),
    path("employee/create-employee", views.create_employee, name="create-employee"),
    path("employee/update-employee/<str:pk>", views.update_employee, name="update-employee"),
    path("employee/delete-employee/<str:pk>", views.delete_employee, name="delete-employee"),
    path("employee/list-username", views.list_user_password, name="list_user_password"),
    path("", views.a),
    path("account/reset-password/<int:pk>", views.reset_employee_password, name="reset_employee_password"),
    path("employee/list-employee", views.list_employee, name="list-employee"),
    path("account/change-password/<str:pk>", views.change_password, name="change-password"),
    path("account/delete-account/<str:pk>", views.delete_account, name="delete-account"),
    path("account/update-account/<str:pk>", views.update_account, name="update-account"),
    path("forgot/forgot-password", views.forgot_password_view, name="forgot_password"),
    path("forgot/reset-password/<str:token>", views.reset_password_view, name="reset_password"),
    path("employee/birthday", views.get_birthday_employee, name="get-birthday"),
    path("query/employee", views.query_employee, name="query-employee"),
    path("employee/<int:id>", views.EmployeeDetail.as_view(), name="detail-emp-id"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
else:
    urlpatterns += [
        re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    ]
