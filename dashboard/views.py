from django.http import HttpResponse
from django.template import loader
from creator.models import Snippet

def todoListView(request):
    allToDos = Snippet.objects.all()
    template = loader.get_template('dashboard/todoListView.html')
    context = {
        'allToDos' : allToDos,
    }
    return HttpResponse(template.render(context, request))