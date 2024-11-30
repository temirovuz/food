from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAdminOrWaiter(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return getattr(request.user, 'role', None) in ['admin', 'waiter']

