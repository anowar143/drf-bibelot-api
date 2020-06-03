from django.contrib.auth.models import User
from rest_framework import serializers
from bibelot.models import Bibelot, LANGUAGE_CHOICES, STYLE_CHOICES


class BibelotSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username') # new
    highlight = serializers.HyperlinkedIdentityField(view_name='bibelot-highlight', format='html')


    class Meta:
        model = Bibelot
        fields = ('url', 'id', 'highlight', 'title', 'code', 'linenos',
                  'language', 'style', 'owner',)



class UserSerializer(serializers.HyperlinkedModelSerializer):
    bibelots = serializers.HyperlinkedRelatedField(many=True, view_name='bibelot-detail', read_only=True) #new


    class Meta:
        model = User
        fields = ('url', 'id', 'username', 'bibelots') # new
