from rest_framework.permissions import BasePermission


class ArticlePermission(BasePermission):

    def has_object_permission(self, request, view, obj):
        """
        Defino si un usuario puede realizar la operacion que quiere sobre el artículo
        :param request:
        :param view:
        :param obj:
        :return:
        """
        if view.action == 'retrieve':
            return True
        if request.user.is_superuser or request.user == obj.author:
            return True
