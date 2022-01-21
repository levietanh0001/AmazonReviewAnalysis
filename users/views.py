from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer
from .models import CustomUser
import jwt, datetime
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import AllowAny
from rest_framework import permissions, status, generics
from rest_framework.generics import GenericAPIView


from .serializers import LogoutSerializer




class UserList(APIView):
    def get(self, request):
        email = request.data['email']
        user = CustomUser.objects.filter(email=email).first()
        # user = CustomUser.objects.all()
        serializer = UserSerializer(user)
        return Response(serializer.data)
    

    
class RegisterView(APIView):
    permission_classes = [AllowAny]
    def post(self, request, format='json'):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                json = serializer.data
                return Response(json, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # def post(self, request):
    #     serializer = UserSerializer(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)



class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']

        user = CustomUser.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')

        payload = {
            # 'id': user.id,
            'email': user.email,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token = jwt.encode(payload, 'secret', algorithm='HS256')

        response = Response({'message': 'success'})

        response.set_cookie(key='jwt', value=token, httponly=True)
        
        
        response.data = {
            'jwt': token
        }
        return response



class UserView(APIView):
    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = CustomUser.objects.filter(email=payload['email']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)




# class LogoutView(APIView):
#     permission_classes = [AllowAny]
#     authentication_classes = ()
#     def post(self, request):
#         try:
#             refresh_token = request.data["refresh_token"]
#             token = RefreshToken(refresh_token)
#             token.blacklist()
#             return Response(status=status.HTTP_205_RESET_CONTENT)
#         except Exception as e:
#             print('\nException in logging out:', e)
#             return Response(status=status.HTTP_400_BAD_REQUEST)
        
    # def post(self, request):
    #     response = Response()
    #     response.delete_cookie('jwt')
    #     response.data = {
    #         'message': 'success'
    #     }
    #     return response
    
    
class LogoutView(generics.GenericAPIView):
    # permission_classes = (permissions.IsAuthenticated,)
    permission_classes = [AllowAny]
    authentication_classes = ()

    def post(self, request):
        try:
            refresh_token = request.data["refresh_token"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    # serializer_class = LogoutSerializer

    # permission_classes = (permissions.IsAuthenticated,)

    # def post(self, request):

    #     serializer = self.serializer_class(data=request.data)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()

    #     return Response(status=status.HTTP_204_NO_CONTENT)    
# class LogoutView(GenericAPIView):
#     serializer_class = LogoutSerializer
#     # permission_classes = (permissions.AllowAny, )
#     permission_classes = (permissions.IsAuthenticated, )

#     def post(self, request, *args):
#         sz = self.get_serializer(data=request.data)
#         sz.is_valid(raise_exception=True)
#         sz.save()
#         return Response(status=status.HTTP_204_NO_CONTENT)