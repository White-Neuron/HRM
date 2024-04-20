from rest_framework import permissions
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.has_permission(request)

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.has_permission()
class IsHrAdminManager(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_hr_admin_manager(request)

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_hr_admin_managern(request)
class IsMe(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        return request.user.EmpID.EmpID == obj.EmpID

class IsHrAdmin(permissions.BasePermission):
    def has_permission(self, request, view):
        return request.user and request.user.is_hr_or_admin(request)

    def has_object_permission(self, request, view, obj):
        return request.user and request.user.is_hr_or_admin(request)


class IsOwnerOrReadonly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.author == request.user


