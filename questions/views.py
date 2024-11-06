

# Create your views here.

from rest_framework import generics
from .models import Question, Answer
from .serializers import QuestionSerializer, AnswerSerializer
#APIView, #ListAPIView, CreateAPIView, DeleteAPIView

class QuestionList(generics.ListAPIView):
    """
    Get the list of all questions.
    """
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    

class AnswerList():
    #your code


class FacultyList():
    #your code

# read about serializers!!!!
    