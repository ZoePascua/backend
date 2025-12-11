from django.shortcuts import render, get_object_or_404
import logging

# Create your views here.
from .models import UserRegistration
from .serializer import RegistrationSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

logger = logging.getLogger(__name__)

@api_view(['POST'])
def register_user(request):
    try:
        serializer = RegistrationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        logger.error(f"Register error: {str(e)}")
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET'])
def list_users(request):
    try:
        users = UserRegistration.objects.all()
        serializer = RegistrationSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Exception as e:
        logger.error(f"List users error: {str(e)}")
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(['GET', 'PUT', 'DELETE'])
def user_detail(request, user_id):
    try:
        user = get_object_or_404(UserRegistration, id=user_id)
        
        if request.method == 'GET':
            serializer = RegistrationSerializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        elif request.method == 'PUT':
            logger.info(f"Updating user {user_id} with data: {request.data}")
            serializer = RegistrationSerializer(user, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                logger.info(f"User {user_id} updated successfully")
                return Response(serializer.data, status=status.HTTP_200_OK)
            logger.error(f"Validation errors for user {user_id}: {serializer.errors}")
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif request.method == 'DELETE':
            logger.info(f"Deleting user {user_id}")
            user.delete()
            logger.info(f"User {user_id} deleted successfully")
            return Response({'message': 'User deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Exception as e:
        logger.error(f"User detail error: {str(e)}")
        return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
