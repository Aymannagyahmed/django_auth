from user.api.v01.permission import IsDev
from .serializers import UserSerializer

from rest_framework.response import Response
from rest_framework import status

from rest_framework.authtoken.models import Token

from rest_framework.decorators import api_view


from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes

@api_view(['POST',])
def create( request):
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.save()
        if user:
            token = Token.objects.create(user=user)
            json = serializer.data
            json['token'] = token.key
            return Response(json, status=status.HTTP_201_CREATED)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST',])
@permission_classes([IsAuthenticated])
def logout(request):
    token = Token.objects.get(user=request.user)
    token.delete()
    return Response( data='logout successfully',status=status.HTTP_200_OK)

@api_view(['POST',])
@permission_classes([IsDev])
def logout_all(request):
    token = Token.objects.all().delete()
    return Response( data='All users logged out successfully',status=status.HTTP_200_OK)


