from rest_framework import permissions

class EsDuenioOSoloLectura(permissions.BasePermission):
    def has_object_permission(self,request,view,obj):
        if request.method in permissions.SAFE_METHODS:
            #A: accede via GET
            return True
        else:
            #A: accede via POST o DELETE
            return obj.user == request.user
