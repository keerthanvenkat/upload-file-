from rest_framework import  serializers
from .models import SharedFiles


class SharedFilesSerailizers(serializers.ModelSerializers):
    class meta:
        model = SharedFiles
        fields = '__all__'

class SharedFilesSerailizersDuplicate(serializers.ModelSerializers):
    class meta:
        model = SharedFiles
        fields = ['docu_name','file']

