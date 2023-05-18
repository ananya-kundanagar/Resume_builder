# file: todo_project/todo_app/serializers.py

from rest_framework import serializers
from ..models import Experience
from ..models import Education


class ExperienceSerializer(serializers.ModelSerializer):
   class Meta:
      fields = '__all__'
      model = Experience

class EducationSerializer(serializers.ModelSerializer):
   class Meta:
      fields = '__all__'
      model = Education