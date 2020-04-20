from rest_framework import generics

from .models import Word, Character
from .serializers import WordSerializer, CharacterSerializer

import random


class WordAPIView(generics.ListAPIView):

    def get_serializer_class(self):
        mode = self.kwargs['mode']
        if mode == 'word':
            return WordSerializer
        else:  # elif mode == 'hiragana'
            return CharacterSerializer

    def get_queryset(self):
        mode = self.kwargs['mode']
        if mode == 'word':
            objects = Word.objects
        else:  # elif mode == 'hiragana'
            objects = Character.objects

        pks = objects.values_list('pk', flat=True)
        pks_list = list(pks)

        prev = self.kwargs['prev']
        if not prev == 'null':
            pk = objects.get(pk=prev).pk
            if pk in pks_list:
                pks_list.remove(pk)

        pks_random = random.sample(pks_list, 4)
        queryset = objects.filter(pk__in=pks_random)

        return queryset
