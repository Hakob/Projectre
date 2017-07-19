from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Question


def index(request):
    recent_questions = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('serve/index.html')              # template methods is always looking in 'templates'
    context = {                                                     # directory
        'recent_questions': recent_questions,
    }
    return HttpResponse(template.render(context, request))          # template variable - an instance of Template class


def welcome(request):
    with open('templates/serve/welcome.html') as f:                 # open method looking in current directory
        return HttpResponse(f)


count = 0


def vote(request, question_id):
    global count
    count += 1
    return HttpResponse('You\'re voting on question %s. Now rate of votes are %d' % (question_id, count))


def http404(request):
    return Http404
# now = datetime.datetime.now()
# html = "<html><body>It is now %s.</body></html>" % now
