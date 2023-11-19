from rest_framework import serializers
from catalog.models import Genre, Language, BookInstance, Author, Book


class BookModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

class LanguageModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class BookInstanceModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookInstance
        fields = '__all__'

class GenreModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'

class AuthorModelSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Author
        fields = '__all__'

