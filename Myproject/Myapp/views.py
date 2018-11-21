from django.shortcuts import render
from django.http import HttpResponse
from .models  import Data
from django.views.decorators.csrf import csrf_exempt,csrf_protect
import json
from django.http import HttpResponseRedirect
from watson_developer_cloud import NaturalLanguageUnderstandingV1
from django.views.decorators.csrf import csrf_exempt
from watson_developer_cloud.natural_language_understanding_v1 \
  import Features, EntitiesOptions, KeywordsOptions
source = ''
Content = {
    'keywords': {
        'text': [],
        'score': []
    },
    'entities': {
        'text': [],
        'score': []
    },
    'categories': {
        'text': [],
        'score': []
    },
}
semantic_roles = []
def CompareSource(comparesource):
    source = Data.objects.get(pk=1).Source
def sync(comparesource):
    fin = comparesource.find('request.getParameter')
    first = comparesource.find('String')
    end = comparesource.find(';',fin)
    a =''
    for i in range(first,end) :
        a +=comparesource[i]
    return  a

def reset(Content):
    for h in ['keywords', 'entities', 'categories']:
        Content[h]['text'].clear()
        Content[h]['score'].clear()
    semantic_roles.clear()

def Know(text):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        username='acdb979b-4643-461e-a34f-02ff2271210a',
        password='5xDqzWdlyeao',
        version='2018-03-16')

    response = natural_language_understanding.analyze(
        text= text,
        features=Features(
        entities=EntitiesOptions(
        emotion=False,

        ),
        categories=EntitiesOptions(
        emotion=False,
        ),
        semantic_roles=EntitiesOptions(
      emotion=False,
      sentiment=False,
      ),
    keywords=KeywordsOptions(
      emotion=False,
      sentiment=False,
      )))

    re = response

    semantic_roles.append(json.dumps(re['semantic_roles'][0]['sentence']))
    for h in ['keywords','entities','categories']:
        for i in re[h]:
            try:
                try:
                    if (float(json.dumps(i['relevance'])) > 0.3):
                        Content[h]['text'].append(i['text'])
                        Content[h]['score'].append(i['relevance'])
                    else:
                        pass
                except:
                    if (float(json.dumps(i['relevance'])) > 0.3):
                        Content[h]['text'].append(i['label'])
                        Content[h]['score'].append(i['relevance'])
                    else:
                        pass

            except:
                try:
                    if (float(json.dumps(i['score'])) > 0.3):
                        Content[h]['text'].append(i['text'])
                        Content[h]['score'].append(i['score'])
                    else:
                        pass
                except:
                    if (float(json.dumps(i['score'])) > 0.3):
                        Content[h]['text'].append(i['label'])
                        Content[h]['score'].append(i['score'])
                    else:
                        pass

    count = Data.objects.count()
    count = count + 1
    data = Data(seq=count, keywords=Content['keywords']['text'][0], entities=Content['entities']['text'],
                categories=Content['categories']['text'],
                desc=semantic_roles[0].__str__().split('"'), source='', etc='')
    data.save()
def source(te):
    re = []
    return te.split(";")[0]

def index(request):
    return render(request, 'tem.html')
def compare(request):
    data = request.GET['text']
    return render(request, 'comparecode.html',{"source" : sync(data)})
def pro(request):

    reset(Content)
    cont = request.POST.get('a')



    return HttpResponse(source(cont))

