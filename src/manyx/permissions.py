from rest_framework.permissions import BasePermission


# a permission class for giving full access to admin and giving access to each user to change it's own data.
class CanChangeManyxUserModel(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        return request.user.is_superuser or obj.username == request.user.username
