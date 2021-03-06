from student.models import Student
from rest_framework import viewsets
from student.serializers import StudentSerializer

class StudentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
