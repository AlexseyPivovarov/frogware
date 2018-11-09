from django.shortcuts import render, HttpResponse
from django.views import View
from json import loads


# Create your views here.
class MyMeinView(View):

    def get(self, request):
        with open('json/MainPageInfo.json', encoding='utf-8', mode='r') as main_js:
            context = {}
            context['main'] = loads(main_js.read())
            return render(request, template_name='main.html', context=context)

    def post(self, request):
        with open('json/FinishedQuestsLeafs.json', encoding='utf-8', mode='w') as main_js:
            main_js.write(request.body.decode("utf-8"))

        return HttpResponse(status=201)


class MyDetailView(View):

    def get(self, request, alias, globalId):
        context = {}
        context['finished'] = []
        with open('json/GeneralQuestsInfo.json', encoding='utf-8', mode='r') as general_js:
            for item in loads(general_js.read()):
                if item['alias'] == alias and item['globalId'] == globalId:
                    context['general'] = item
                    break
            else:
                return render(request, template_name='not-found.html')
        with open('json/FinishedQuestsLeafs.json', encoding='utf-8', mode='r') as finished_js:
            for item in loads(finished_js.read()):
                if item['questId'] == context['general']['id']:
                    context['finished'].append(item['name'])
        return render(request, template_name='detail.html', context=context)