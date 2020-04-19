from django.db import models

import uuid


class Word(models.Model):

    word = models.CharField(max_length=15, unique=True)
    meaning_id = models.CharField(max_length=30, blank=True, null=True)
    other = models.TextField(max_length=150, blank=True, null=True)

    romaji = models.CharField(max_length=60, blank=True, null=True)
    word_count = models.PositiveSmallIntegerField(blank=True, null=True)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.word


class Character(models.Model):

    hiragana = models.CharField(max_length=2)
    katakana = models.CharField(max_length=2)
    romaji = models.CharField(max_length=3)

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.hiragana
