from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.conf import settings

from .models import Question


def index(request):
    return HttpResponse(b'Hello World')


def welcome(request):
    with open(settings.BASE_DIR + r'/templates/welcome.html') as f:
        return HttpResponse(f)


def results(request):
    recent_questions = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in recent_questions])
    return HttpResponse(output)


count = 0


def vote(request, question_id):
    global count
    count += 1
    return HttpResponse('You\'re voting on question %s. Now rate of votes are %d' % (question_id, count))


def http404(request):
    return Http404
# now = datetime.datetime.now()
# html = "<html><body>It is now %s.</body></html>" % now
