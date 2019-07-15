from nps_django.models import Passholder, Pass, Park, Visit
from rest_framework import serializers

class PassholderSerializer(serializers.HyperlinkedModelSerializer):
  passes = serializers.StringRelatedField(many=True)

  class Meta:
    model = Passholder
    fields = ('first_name', 'last_name', 'passes')

class PassSerializer(serializers.HyperlinkedModelSerializer):
  passholder_primary = serializers.StringRelatedField

  class Meta:
    model = Pass
    fields = ('type', 'passholder_primary', 'passholder_secondary', 'expiration_date', 'zip_code', 'email', 'phone_num', 'cost')

class ParkSerializer(serializers.HyperlinkedModelSerializer):
  visits = serializers.StringRelatedField

  class Meta:
    model = Park
    fields = ('name', 'state', 'visits')

class VisitSerializer(serializers.HyperlinkedModelSerializer):
  park = serializers.StringRelatedField
  passholder = serializers.StringRelatedField

  class Meta:
    model = Visit
    fields = ('park', 'passholder', 'date')