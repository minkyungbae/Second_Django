from django.shortcuts import get_object_or_404, render, redirect
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
from django.views import View
from django.http  import JsonResponse, HttpResponse
from django.forms.models import model_to_dict
import json

from .models import MarketModel
from .forms import MarketModelForm
# from .serializers import MarketModelSerializer

# 마켓 정보 가져오기
class MarketInfoView(View):
    
    def get(self, request): # 들고 오기
        print("MarketInfoView.get()")
        # 모든 market 정보 가져오기
        markets = MarketModel.objects.all()
        markets_data = list(markets.values())
        content = {"markets_data":markets_data}
        return render(request, "SpartaMarkets/market_list.html", content)

# 마켓 새로 입력하기
class MarketCreateView(View):   
    def post(self, request): # 입력하기
        form = MarketModelForm(request.POST) # 요청한 데이터를 form에 바인딩
        if form.is_valid():
            form.save() # request 값을 바로 DB에 저장
            return render(request, "SpartaMarkets/create.html")
        # 유효하지 않으면 에러
        return HttpResponse(status=400)
        
        
# 마켓 디테일 보기
class MarketInfoDetailView(View):
    def get(self, request, market_id):
        # 특정 market_id를 가진 정보 들고 오기
        market = get_object_or_404(MarketModel, market_id=market_id)
        data = model_to_dict(market)
        return JsonResponse(data)
        
        
 # 마켓 삭제하기
class MarketDeleteView(View):
    def delete(self, request, market_id): # 삭제하기
        market = get_object_or_404(MarketModel, market_id = market_id) # 기존 거 조회하기
        market.delete()
        return HttpResponse(status=204)


# 마켓 수정하기
class MarketPutView(View):
    def put(self, request, market_id): # 수정하기
        market = get_object_or_404(MarketModel, market_id=market_id) # 기존 거 조회하기
        data = json.loads(request.body)
        # form에 market 조회한 값으로 채워둔 거에 request.data 값 기입
        form = MarketModelForm(data, instance=market)
        if form.is_valid():
            form.save() # 유효하면 저장
            return HttpResponse(status=200)
        # 유효하지 않으면 에러 반환
        return HttpResponse(status=400)
        
        