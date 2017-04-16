import logging

from models import Question, Answer
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage
from django.views.decorators.http import require_GET

logger = logging.getLogger('stepic')


def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)


@require_GET
def new_qa(request):
    new_qas = Question.objects.new()
    base_url = '/?page='
    paginator, page = paginate(request, new_qas, base_url)
    return render(request, 'qa/new_qa.html',
                  {'new_qas': page.object_list,
                   'paginator': paginator,
                   'page': page})


@require_GET
def popular_qa(request):
    popular_qas = Question.objects.popular()
    base_url = '/popular/?page='
    paginator, page = paginate(request, popular_qas, base_url)
    return render(request, 'qa/popular_qa.html',
                  {'popular_qas': page.object_list,
                   'paginator': paginator,
                   'page': page})


def question(request, qa_id):
    qa = get_object_or_404(Question, id=qa_id)
    try:
        answer_for_qa = qa.answer_set.all()
    except Answer.DoesNotExist:
        answer_for_qa = None
    return render(request, 'qa/question.html',
                  {'question': qa,
                   'answers': answer_for_qa})


def paginate(request, qs, base_url):
    try:
        limit = int(request.GET.get('limit', 10))
    except ValueError:
        limit = 10
    if limit > 100:
        limit = 10
    try:
        page = int(request.GET.get('page', 1))
    except ValueError:
        raise Http404
    paginator = Paginator(qs, limit)
    paginator.baseurl = base_url
    try:
        page = paginator.page(page)
    except EmptyPage:
        page = paginator.page(paginator.num_pages)
    return paginator, page
