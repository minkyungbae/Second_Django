from django.shortcuts import get_object_or_404, render, redirect
# from rest_framework.response import Response
# from rest_framework import status
# from rest_framework.views import APIView
from django.views import View
# from django.http  import JsonResponse, HttpResponse
# from django.forms.models import model_to_dict
# import json
from django.urls import reverse
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
    
    def get(self, request):
        form = MarketModelForm()
        return render(request, "SpartaMarkets/create.html", {"form":form})
    
    def post(self, request): # 입력하기
        form = MarketModelForm(request.POST) # 요청한 데이터를 form에 바인딩
        if form.is_valid():
            market = form.save() # request 값을 바로 DB에 저장
            return redirect(reverse("spartamarket:detail", args=[market.id]))
        
        content= {"form":form}
        return render(request, "SpartaMarkets/create.html", content)
        
        
# 마켓 디테일 보기
class MarketInfoDetailView(View):
    def get(self, request, market_id):
        # 특정 market_id를 가진 정보 들고 오기
        market = get_object_or_404(MarketModel, id=market_id)
        return render(request, "SpartaMarkets/market_detail.html", {"market":market})
        
        
 # 마켓 삭제하기
class MarketDeleteView(View):
    def post(self, request, market_id): # 삭제하기
        market = get_object_or_404(MarketModel, id=market_id) # 기존 거 조회하기
        market.delete()
        return redirect(reverse("spartamarket:list"))


# 마켓 수정하기
class MarketPutView(View):
    def get(self, request, market_id):
        market = get_object_or_404(MarketModel, id=market_id)
        form = MarketModelForm(instance=market)
        return render(request, "SpartaMarkets/update.html", {"form": form, "market_id": market_id})

    def post(self, request, market_id): # 수정하기
        market = get_object_or_404(MarketModel, id=market_id) # 기존 거 조회하기
        form = MarketModelForm(request.POST, instance=market)
        if form.is_valid():
            form.save() # 유효하면 저장
            return redirect(reverse("spartamarket:detail", args=[market.id]))
        # 유효하지 않으면 에러 반환
        return render(request, "SpartaMarkets/update.html", {"form": form, "market_id": market_id})
        
        
        