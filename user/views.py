from rest_framework.response import Response
from .serializers import CustomUserSerialzer
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError, AuthenticationFailed
import jwt, os, datetime
from .models import CustomUser
from dotenv import load_dotenv



# Load the stored environment variables
load_dotenv()
secret_key = os.getenv('SECRET_KEY')


class RegisterView(APIView):
    def post(self, request):
        print("sdsdsd")
        user_details = request.data
        print(user_details)
        email = user_details.get('email')
        password = user_details.get('password')
        if not all([email, password]):
            return Response({'error': 'Please fill in all the required fields'},
                            status=status.HTTP_400_BAD_REQUEST)
        try:
            serializer = CustomUserSerialzer(data=user_details)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            print(serializer)
            response_data = {
                             'email': serializer.data['email'],
                             }
            return Response({'message': "Your Account Registered Successfully", 'data': response_data})
        
        except ValidationError as e:
            if 'email' in e.detail:
                print(str(e))
                return Response({'error': 'Email already exists'}, status=status.HTTP_409_CONFLICT)
            else:
                print(str(e))
                return Response({'error': 'Registraion Failed, please check the details again'}, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']
       
        print(email)
        print(password)
        if not (email and password):
            return Response({
                'error': 'Email and Password is required'
            })
       
        user = CustomUser.objects.filter(email=email).first()
        if user is None:
            raise AuthenticationFailed({
                'error':'User is not found'
            })
        
        if not user.check_password(password):
            raise AuthenticationFailed({'error':'Incorrrect Password'})
        
        payload = {
            'id':user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat':datetime.datetime.utcnow()
        }
        token = jwt.encode(payload, 'secret', algorithm="HS256")
        response = Response()
    
        response.data = {
            'access': token
        }
    
        return response