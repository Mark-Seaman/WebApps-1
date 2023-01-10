from django.views.generic import TemplateView


class AnimalsView(TemplateView):
    template_name = 'index.html'
