from dal import autocomplete

from .models import Project

class ProjectAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        ### Don't forget to filter out results depending on the visitor ! ###
        if not self.request.user.is_authenticated():
            return Project.objects.none()

        qs = Project.objects.all()

        if self.q:
            qs = qs.filter(name__istartswith=self.q)

        return qs