from modeltranslation.translator import register, TranslationOptions
from fastfood.models import Food


@register(Food)
class FoodTranslationOptions(TranslationOptions):
    fields = ('name', 'description')
