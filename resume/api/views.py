from rest_framework import generics, permissions
from rest_framework.response import Response
from ..models import Experience, Education
from .serializers import ExperienceSerializer
from .serializers import EducationSerializer


class ExperienceList(generics.ListCreateAPIView):
   serializer_class = ExperienceSerializer
   def get_queryset(self):
      if self.request.user.is_authenticated:
         user = self.request.user
         return Experience.objects.filter(user=user)


class ExperienceDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Experience.objects.all()
   serializer_class = ExperienceSerializer


class EducationList(generics.ListCreateAPIView):
   queryset = Education.objects.all()
   serializer_class = EducationSerializer


class EducationDetail(generics.RetrieveUpdateDestroyAPIView):
   queryset = Education.objects.all()
   serializer_class = EducationSerializer