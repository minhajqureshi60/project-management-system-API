from django.shortcuts import render
from rest_framework import viewsets,generics
from api.models import Project,Employee
from api.serializers import ProjectSerializer,EmployeeSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializers import RegistrationSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers
import uuid




class RegistrationAPIView(generics.GenericAPIView):

    serializer_class = RegistrationSerializer

    def post(self, request):
        serializer = self.get_serializer(data = request.data)
        # serializer.is_valid(raise_exception = True)
        # serializer.save()
        if(serializer.is_valid()):
            serializer.save()
            return Response({
                "RequestId": str(uuid.uuid4()),
                "Message": "User created successfully",
                
                "User": serializer.data}, status=status.HTTP_201_CREATED
                )
        



# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset= Project.objects.all()
    serializer_class=ProjectSerializer
    
    #companies/{projectId}/emplyees
    @action(detail=True,methods=['get'])
    def employees(self,request,pk=None):   
        try:                
            project=Project.objects.get(pk=pk)
            emps=Employee.objects.filter(project=project)
            emps_serializer=EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
        except Exception as e:
            print(e)
            return Response({
                'message':'Project might not exists !! Error'
            })


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer