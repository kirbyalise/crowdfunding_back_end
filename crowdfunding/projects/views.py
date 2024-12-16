from django.shortcuts import render
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404
from .models import Project, Pledge
from .serializers import ProjectSerializer, PledgeSerializer, ProjectDetailSerializer
from rest_framework import status, permissions
from .permissions import IsOwnerOrReadOnly, IsSupporterOrReadOnly
from rest_framework import generics 
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse


class ProjectList(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request):
        projects = Project.objects.all()
        serializer = ProjectSerializer(projects, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProjectSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(owner=request.user)
            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
        )
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
    )


class ProjectDetail(APIView):
    
    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsOwnerOrReadOnly
    ]

    def get_object(self, pk):
        try:
            project = Project.objects.get(pk=pk)
            self.check_object_permissions(self.request, project)
            return project
        except Project.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(project)
        return Response(serializer.data)

    def put(self, request, pk):
        project = self.get_object(pk)
        serializer = ProjectDetailSerializer(
            instance=project,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        project = self.get_object(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class PledgeList(APIView):
    def get(self, request):
        pledges = Pledge.objects.all()
        serializer = PledgeSerializer(pledges, many=True)
        # ----------
        return Response(serializer.data)

    def post(self, request):
        # Check to see if project is opened or not
        # project_id = request.data.get('project')
        # projects = Project.objects.filter(pk=project_id)
        # if projects[0].is_open:
        #     print('open')
        #     serializer = PledgeSerializer(data=request.data)
        #     if serializer.is_valid():
        #         serializer.save(supporter=request.user)
        #         return Response(
        #             serializer.data,
        #             status=status.HTTP_201_CREATED
        #         )
        #     return Response(
        #         serializer.errors,
        #         status=status.HTTP_400_BAD_REQUEST
        #     )
        project_id = request.data.get('project')
        try:
            project = Project.objects.get(pk=project_id)
        except Project.DoesNotExist:
            raise Http404
        
        if project.is_open:
            print('open')
            serializer = PledgeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(supporter=request.user)
                return Response(
                    serializer.data,
                    status=status.HTTP_201_CREATED
                )
            return Response(
                serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )
        else:
            print('closed')
            return Response(
                {"Sorry this project is closed!"},
                status=status.HTTP_403_FORBIDDEN
            )


class PledgeDetail(APIView):

    permission_classes = [
        permissions.IsAuthenticatedOrReadOnly,
        IsSupporterOrReadOnly
    ]
    def get_object(self, pk):
        try:
            # Use 'Pledge' for the model class and 'pledge' for the variable
            pledge = Pledge.objects.get(pk=pk)
            self.check_object_permissions(self.request, pledge)
            return pledge
        except Pledge.DoesNotExist:
            raise Http404 

    def get(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeSerializer(pledge)
        return Response(serializer.data)

    def put(self, request, pk):
        pledge = self.get_object(pk)
        serializer = PledgeSerializer(
            instance=pledge,
            data=request.data,
            partial=True
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    def delete(self, request, pk):
        pledge = self.get_object(pk)
        pledge.delete()
        return Response("Byeeee")


class CustomAuthToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                            context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email,
            'is_superuser': user.is_superuser
        })

# TESTING
class ProjectDetailView(generics.RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'projects': reverse('project-list', request=request, format=format),
        'pledges': reverse('pledge-list', request=request, format=format),
        'users': reverse('user-list', request=request, format=format),
    })