# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    def has_permission(self, request, view):
        """
        Defino si un usuario puede ejecutar el método o acceder a la vista que quiere acceder
        :param request:
        :param view:
        :return:
        """
        if request.method == "POST":
            return True
        if request.user.is_superuser:
            return True
        if view.action in ("retrieve", "update", "destroy"):
            return True
        return False

    def has_object_permission(self, request, view, obj):
        """
        Defino si un usuario puede realizar la operacion que quiere sobre el objeto
        :param request:
        :param view:
        :param obj:
        :return:
        """
        return request.user.is_superuser or request.user == obj
