from modeltranslation.translator import translator, TranslationOptions,register

from .models import Team, Portfolio, Testimonials

@register(Team)
class TeamsTranslationOptions(TranslationOptions):
    fields = ('position',)

@register(Portfolio)
class TeamsTranslationOptions(TranslationOptions):
    fields = ('name', 'project_title', 'desc')

@register(Testimonials)
class TeamsTranslationOptions(TranslationOptions):
    fields = ('position','advice')