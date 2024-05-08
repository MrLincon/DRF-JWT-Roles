from django.contrib.auth.models import update_last_login
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserRegistrationSerializer, SuperUserRegistrationSerializer, UserLoginSerializer, \
    PasswordChangeSerializer


class UserRegistrationView(APIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'message': 'User successfully registered!',
                'data': {},
            }

            return Response(response, status=status_code)


class SuperUserRegistration(APIView):
    serializer_class = SuperUserRegistrationSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = self.serializer_class(data=request.data)
        valid = serializer.is_valid(raise_exception=True)

        if valid:
            serializer.save()
            status_code = status.HTTP_201_CREATED

            response = {
                'message': 'User successfully registered!',
                'data': {},
            }

            return Response(response, status=status_code)


class UserLoginView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            update_last_login(None, user)

            response = {
                'message': 'Login successful!',
                'data': {
                    'email': user.email,
                    'role': user.role,
                    'access': access_token
                },
            }
            return Response(response, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PasswordChangeView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            serializer = PasswordChangeSerializer(data=request.data, context={'request': request})

            if serializer.is_valid():
                serializer.save()

                response = {
                    "message": "Password changed successfully.",
                    'data': {},
                }

                return Response(response, status=status.HTTP_200_OK)

            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            print(e)

            response = {
                'message': 'Internal Server Error',
                'data': {},
            }

            return Response(response, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

