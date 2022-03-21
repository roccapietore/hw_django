from rest_framework import permissions
from users.models import User


class AdUpdateDeletePermission(permissions.BasePermission):
    message = 'This function is only available for admin and moderator'

    def has_permission(self, request, view):
        if request.user.role in [User.moderator, User.admin]:
            return False
        return True


class IsOwnerPermission(permissions.BasePermission):
    message = 'This function is only available for ad`s owner'

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user

