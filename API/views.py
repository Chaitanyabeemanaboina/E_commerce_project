from .serializers import Product_serializers
from firstapp.models import Products
from rest_framework.permissions import IsAdminUser,IsAuthenticated,BasePermission
from rest_framework.authentication import BaseAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_api_key.models import APIKey
from rest_framework.generics import ListAPIView,CreateAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
class APIKey_create(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        api_key,key = APIKey.objects.create_key(name=request.user.username)
        key_dict = {'key':key}
        return Response(key_dict)
class APIKey_Authorization(BaseAuthentication):
    def authenticate(self, request):
        api_key = request.headers.get('X-API-KEY')
        try:
            api_key_instance = APIKey.objects.get_from_key(api_key)
            return (None, api_key_instance)
        except:
            raise AuthenticationFailed('Invalid API key')
class APIKey_Permit(BasePermission):
    def has_permission(self, request, view):
        api_key = request.headers.get('X-API-KEY')
        if api_key:
            try:
                api_key_instance = APIKey.objects.get_from_key(api_key)
                return True
            except:
                raise AuthenticationFailed('Invalid API-key')
        else:
            raise AuthenticationFailed('API-Key Required')
class Product_list(ListAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [APIKey_Permit, IsAuthenticated]
    queryset = Products.objects.all()
    serializer_class = Product_serializers
class Product_create(CreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [APIKey_Permit,IsAuthenticated, IsAdminUser]
    queryset = Products.objects.all()
    serializer_class = Product_serializers
class Product_update(UpdateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [APIKey_Permit, IsAuthenticated,IsAdminUser]
    queryset = Products.objects.all()
    serializer_class = Product_serializers
class Product_destroy(DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [APIKey_Permit, IsAuthenticated, IsAdminUser]
    queryset = Products.objects.all()
    serializer_class = Product_serializers
    lookup_field = 'id'
