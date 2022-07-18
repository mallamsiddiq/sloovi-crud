from rest_framework.response import Response
from rest_framework import generics, status
from rest_framework.exceptions import AuthenticationFailed
from .serializers import UserSerializer, TemplateSerializer
from .models import User, Template
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class RegisterView(generics.ListCreateAPIView):
    # http_method_names = ['post']
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def post(self, request,):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        user_auth_data=serializer.data
        return Response('boom success!! Account created for %s'%(user_auth_data['first_name']))

class TemplateView(generics.ListCreateAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset = self.get_queryset()
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)
    def post(self, request,):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        serialized_data=serializer.data
        return Response('boom success!! new template created  %s'%(serialized_data['template_name']))

class TemplateDetailView(generics.RetrieveUpdateDestroyAPIView):

    serializer_class = TemplateSerializer
    lookup_url_kwarg = 'template_id'
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        return Template.objects.all()

class TemplateView(generics.ListCreateAPIView):
    queryset = Template.objects.all()
    serializer_class = TemplateSerializer
    permission_classes = (IsAuthenticated,)

class UsersView(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)
    def list(self, request):
        queryset =User.objects.filter(id=request.user.id)
        serializer = self.serializer_class(queryset, many=True)
        return Response(serializer.data)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    lookup_url_kwarg = 'user_id'
    lookup_field = 'id'
    permission_classes = (IsAuthenticated,)
    def get_queryset(self):
        if str(self.request.user.id) != self.kwargs['user_id']:
            raise AuthenticationFailed(f"hey {self.request.user.email} ;   you re unauthorised to interact with this user's comtent, login aappropitately and provide your id. thanks")
        return User.objects.filter(id=self.kwargs['user_id'])

