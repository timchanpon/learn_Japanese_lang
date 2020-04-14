from django.contrib import admin

from .models import Word
from .chars_dict import hiragana


class WordAdmin(admin.ModelAdmin):

    def save_model(self, request, obj, form, change):
        word = obj.word

        # romaji
        romaji = ''
        for char in word:
            if char in hiragana:
                romaji += hiragana[char] + '-'
            else:
                romaji = 'ERROR_'
                break
        romaji = romaji[:-1]

        # word_count
        word_count = len(word)

        obj.romaji = romaji
        obj.word_count = word_count
        obj.save()


admin.site.register(Word, WordAdmin)
