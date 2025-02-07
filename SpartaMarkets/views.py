from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from .models import MarketModel
from .forms import MarketModelForm

# get, post, delete, put 다 있음
class MarketInfoAPIView(APIView):
    
    def get(self, request, market_id): # 들고 오기
        
        # 특정 market_id를 가진 정보 들고 오기
        if market_id:
            market = get_object_or_404(MarketModel, market_id=market_id)
        
            data = {
                "market_id" : market.market_id,
                "market_zone" : market.market_zone,
                "market_manager" : market.market_manager,
                "market_number" : market.market_number,
                "market_opening_date" : market.market_opening_date,
                "market_employees" : market.market_employees,
            }
            return Response(data, status=status.HTTP_200_OK)

        # 모든 market 정보 가져오기
        markets = MarketModel.objects.all()
        data = {
            "market_id" : markets.market_id,
                "market_zone" : markets.market_zone,
                "market_manager" : markets.market_manager,
                "market_number" : markets.market_number,
                "market_opening_date" : markets.market_opening_date,
                "market_employees" : markets.market_employees,
        }
        return Response(data, status=status.HTTP_200_OK)
    
    
    def post(self, request): # 입력하기
        form = MarketModelForm(request.data) # 요청한 데이터를 form에 바인딩
        if form.is_valid():
            form.save() # request 값을 바로 DB에 저장
            return Response(status=status.HTTP_200_OK)
        # 유효하지 않으면 에러
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
    
    def delete(self, request, market_id): # 삭제하기
        market = get_object_or_404(MarketModel, market_id = market_id) # 기존 거 조회하기
        market.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, market_id): # 수정하기
        market = get_object_or_404(MarketModel, market_id=market_id) # 기존 거 조회하기
        # form에 market 조회한 값으로 채워둔 거에 request.data 값 기입
        form = MarketModelForm(request.data, instance=market)
        if form.is_valid():
            form.save() # 유효하면 저장
            return Response(status=status.HTTP_200_OK)
        # 유효하지 않으면 에러 반환
        return Response(status=status.HTTP_400_BAD_REQUEST)
        
        