from .models import *
from rest_framework import serializers


class PeopleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = People
        fields = ('url','Names')

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('url','Name','Surname','Reg_Number','Password')

class QuestionSelializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Question
        fields = ('url','asker','topic','body')

class AnswerSelializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Answer
        fields = ('url','answerer','qn','body')
