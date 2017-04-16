from models import Question, Answer
from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.core.paginator import Paginator, EmptyPage


def test(request, *args, **kwargs):
    return HttpResponse('OK', status=200)


def new_qa(request):
    new_qas = Question.objects.new()
    base_url = '/?page='
    paginator, page = paginate(request, new_qas, base_url)
    return render(request, 'qa/new_posts.html',
                  {new_qas: page.object_list,
                   paginator: paginator,
                   page: page})


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
