from rest_framework.decorators import api_view
from rest_framework.response import Response
from user.models import  CustomUser
from .serializers import SavedPasswordSerializer
from .models import SavePassword
import jwt


@api_view(['POST'])
def save_password(request):

    access = request.data.get('access')
   
    payload = jwt.decode(access, 'secret', algorithms=["HS256"])
 
    user = CustomUser.objects.filter(id=payload['id']).first()
  
    password=request.data.get("password")
    platform=request.data.get("field")
    
    saves=SavePassword.objects.create(user=user,
                                     password=password,platform=platform)
    saves.save()
    return Response({"msg": "Saved successfully"})
    

@api_view(['GET'])
def get_password( request):
  print(request, 'asasasas')
  token = request.query_params.get('access')
  

  print(token)
  payload = jwt.decode(token, 'secret', algorithms=["HS256"])
  try:
        token = request.data.get('token')
        user = CustomUser.objects.filter(id=payload['id']).first()
        saved_password_object = SavePassword.objects.filter(user=user)
        print(saved_password_object)
        for i in saved_password_object:
            print(i.password)
    
        serializer = SavedPasswordSerializer(saved_password_object,many=True)
        print(serializer.data)
        
        
        return Response(serializer.data)
    
  except saved_password_object.DoesNotExist:

      return Response({"msg": "SavePassword object not found"}, status=404)
  
  except Exception as e:
  
      return Response({"msg": str(e)}, status=500)