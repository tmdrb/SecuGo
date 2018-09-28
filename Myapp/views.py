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

Content = {
    'keywords': {
        'text': [],
        'score': []
    },
    'concepts': {
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

def reset(Content):
    for h in ['keywords', 'concepts', 'entities', 'categories']:
        Content[h]['text'].clear()
        Content[h]['score'].clear()

def Know(text):
    natural_language_understanding = NaturalLanguageUnderstandingV1(
        username='acdb979b-4643-461e-a34f-02ff2271210a',
        password='5xDqzWdlyeao',
        version='2018-03-16')

    response = natural_language_understanding.analyze(
        text= text,
        features=Features(
        concepts=EntitiesOptions(
        emotion=False,

        ),
        categories=EntitiesOptions(
        emotion=False,
        ),
    entities=EntitiesOptions(
      emotion=False,
      sentiment=False,
      ),
    keywords=KeywordsOptions(
      emotion=False,
      sentiment=False,
      )))

    re = response
    for h in ['keywords','concepts','entities','categories']:
        for i in re[h]:
            try:
                if (float(json.dumps(i['relevance'])) > 0.8):
                    Content[h]['text'].append(i['text'])
                    Content[h]['score'].append(i['relevance'])
                else:
                    pass

            except:
                if (float(json.dumps(i['score'])) > 0.8):
                    Content[h]['text'].append(i['text'])
                    Content[h]['score'].append(i['score'])
                else:
                    pass

def index(request):
    return render(request, 'tem.html')

def pro(request):

    reset(Content)
    cont = request.POST.get('a')
    Know(cont)

    data = Data(keywords=Content['keywords']['text'], concepts=Content['concepts']['text'],
                entities=Content['entities']['text'], categories=Content['categories']['text'], source='')
    data.save()
    return HttpResponse(Content.values())

