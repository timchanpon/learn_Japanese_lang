from rest_framework import serializers

from .models import Word, Character


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = ('pk', 'word', 'romaji', )


class CharacterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ('pk', 'hiragana', 'romaji', )
