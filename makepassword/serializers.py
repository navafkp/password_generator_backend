from rest_framework import serializers
from .models import SavePassword

class SavedPasswordSerializer(serializers.ModelSerializer):
    class Meta:
        model = SavePassword
        fields = "__all__"