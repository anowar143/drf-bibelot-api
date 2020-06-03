from django.contrib.auth.models import User # new
from rest_framework import generics, permissions, renderers # new
from rest_framework.decorators import api_view # new
from rest_framework.response import Response # new
from rest_framework.reverse import reverse # new


from .models import Bibelot
from .permissions import IsOwnerOrReadOnly # new
from bibelot.serializers import BibelotSerializer, UserSerializer #new

class BibelotHighlight(generics.GenericAPIView): # new
    queryset = Bibelot.objects.all()
    renderer_classes = (renderers.StaticHTMLRenderer,)

    def get(self, request, *args, **kwargs):
        bibelot = self.get_object()
        return Response(bibelot.highlighted)



@api_view(['GET']) # new
def api_root(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'bibelots': reverse('bibelot-list', request=request, format=format)
    })



class BibelotList(generics.ListCreateAPIView):
    queryset = Bibelot.objects.all()
    serializer_class = BibelotSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,) # new

    def perform_create(self, serializer): # new
        serializer.save(owner=self.request.user)



class BibelotDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Bibelot.objects.all()
    serializer_class = BibelotSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,) # new




class UserList(generics.ListAPIView): # new
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView): # new
    queryset = User.objects.all()
    serializer_class = UserSerializer

