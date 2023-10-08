from rest_framework import generics, status
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView

class RegistrationApiView(generics.GenericAPIView):
    serializer_class = RegistrationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data.pop("password1", None)
        serializer.save()
        return Response(
            "username %s created successfully" % serializer.validated_data["username"],
            status=status.HTTP_201_CREATED,
        )


class CustomObtainAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        token, created = Token.objects.get_or_create(user=user)
        # if token not exist created will be True
        return Response(
            {"token": token.key, "user_id": user.pk, "username": user.username}
        )


class CustomDiscardAuthToken(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        is_tokened = Token.objects.filter(user=request.user).exists()
        print(is_tokened)
        if is_tokened:
            request.user.auth_token.delete()
            return Response(
                {"details": "token has been deleted successfully"},
                status=status.HTTP_200_OK,
            )
        else:
            return Response(
                {"details": "your accounts do not have any token to delete"},
                status=status.HTTP_400_BAD_REQUEST,
            )


class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs) -> Response:
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.validated_data["username"] = serializer.user.username
        serializer.validated_data["id"] = serializer.user.id
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
