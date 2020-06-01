import json
import requests
from rest_framework.generics import ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q, F
from rest_framework import viewsets
from django.shortcuts import get_object_or_404


from cores.models import Config
from stocks.models import (
    Stock,
    CompanyHistoricalQuote,
    Company
)
from stocks.serializers import (
    StockSerializer,
    StockScanSerializer,
    CompanyHistoricalQuoteSerializer
)

class StockAPIView(ListAPIView):
    serializer_class = StockSerializer
    queryset = Stock.objects.all()

    def get(self, request, *args, **kwargs):
        serializer = StockSerializer(Stock.objects.all(), many=True)
        return Response(serializer.data, status = status.HTTP_200_OK)

    def put(self, request, *args, **kwargs):
        url = "https://svr3.fireant.vn/api/Data/Markets/TradingStatistic"

        headers = {
            'cache-control': 'no-cache'
        }

        response = requests.request('GET', url, headers=headers)
        Stock.objects.all().delete()
        serializer = StockSerializer(data=response.json(), many=True)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        created = serializer.save()
        return Response(serializer.data, status = status.HTTP_201_CREATED)


class StockFilterAPIView(APIView):

    def post(self, request, *args, **kwargs):
        ICBCode = request.data.get('ICBCode')
        Date = request.data.get('Date')
        IsVN30 = request.data.get('IsVN30')
        IsFavorite = request.data.get('IsFavorite')
        
        # if not ICBCode and not Date:
            # return Response({'Error': 'No ICBCode and Date'})
        serializer = None
        result = []
        if ICBCode and Date:
            filteredCompany = Company.objects.filter(ICBCode=ICBCode)
            filteredStocks = Stock.objects.filter(Symbol__in=[i.Symbol for i in filteredCompany])
            result = CompanyHistoricalQuote.objects.filter(Q(Date=Date) & Q(Stock_id__in=[i.id for i in filteredStocks]))
            serializer = CompanyHistoricalQuoteSerializer(result, many=True)
        if Date and not ICBCode:
            result = CompanyHistoricalQuote.objects.filter(Q(Date=Date))
            serializer = CompanyHistoricalQuoteSerializer(result, many=True)
            
        if IsVN30:
            result = Stock.objects.filter(IsVN30=True)
            serializer = StockSerializer(result, many=True)
        if IsFavorite:
            result = Stock.objects.filter(IsFavorite=True)
            serializer = StockSerializer(result, many=True)

        if serializer:
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({})
        

class StockViewSet(viewsets.ViewSet):
    def list(self, request):
        queryset = Stock.objects.all()
        serializer = StockSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        stock = get_object_or_404(Stock, pk=pk)
        serializer = StockSerializer(stock)
        return Response(serializer.data)

    def update(self, request, pk=None):
        pass

    def partial_update(self, request, pk=None):
        stock = get_object_or_404(Stock, pk=pk)
        serializer = StockSerializer(stock, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class StockScanAPIView(APIView):
    def post(self, request, *args, **kwargs):
        Symbol = request.data.get('Symbol')
        type = request.data.get('type')
        TodayCapital = request.data.get('TodayCapital')
        Date = request.data.get('Date')
        Date = '2020-06-01T00:00:00Z'
        print(TodayCapital)
        
        if Symbol:
            filteredStocks = Stock.objects.filter(Symbol__contains=Symbol)
            companyHistoricalQuote = CompanyHistoricalQuote.objects\
                .filter(Date=Date)\
                .filter(Stock_id__in=[i.id for i in filteredStocks])
            serializer = CompanyHistoricalQuoteSerializer(companyHistoricalQuote, many=True)
        elif type:
            if type == 'IsVN30':
                filteredStocks = Stock.objects.filter(IsVN30=True)
                companyHistoricalQuote = CompanyHistoricalQuote.objects\
                    .filter(Date=Date)\
                    .filter(Stock_id__in=[i.id for i in filteredStocks])
                serializer = CompanyHistoricalQuoteSerializer(companyHistoricalQuote, context={'test': True}, many=True)
            elif type == 'IsFavorite':
                filteredStocks = Stock.objects.filter(IsFavorite=True)
                companyHistoricalQuote = CompanyHistoricalQuote.objects\
                    .filter(Date=Date)\
                    .filter(Stock_id__in=[i.id for i in filteredStocks])
                serializer = CompanyHistoricalQuoteSerializer(companyHistoricalQuote, many=True)
            else:
                companyHistoricalQuote = CompanyHistoricalQuote.objects\
                    .filter(Date=Date)\
                    .annotate(TodayCapital=F('PriceClose') * F('DealVolume'))\
                    .filter(TodayCapital__gt=TodayCapital)
                
                serializer = CompanyHistoricalQuoteSerializer(companyHistoricalQuote, many=True)
        else:
            companyHistoricalQuote = CompanyHistoricalQuote.objects\
                .filter(Date=Date)\
                .annotate(TodayCapital=F('PriceClose') * F('DealVolume'))\
                .filter(TodayCapital__gt=TodayCapital)
            
            serializer = CompanyHistoricalQuoteSerializer(companyHistoricalQuote, many=True)
        return Response(serializer.data)