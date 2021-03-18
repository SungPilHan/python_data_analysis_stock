from rest_framework import viewsets
from rest_framework import permissions
from restapi.api.models import MyTopicInstitut, MyTopicForeign, MyTopicPriceBuy, MyTopicPriceSell, MyTopicNews
from restapi.api.serializers import MyTopicInstitutSerializer, MyTopicForeignSerializer, MyTopicPriceBuySerializer, MyTopicPriceSellSerializer, MyTopicNewsSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth.models import User
from django.shortcuts import render

# Create your views here.

class MyTopicInstitutViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MyTopicInstitut.objects.all()
    serializer_class=MyTopicInstitutSerializer

    permission_classes= [permissions.IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def search(self, request):
        q=request.query_params.get('name', None)
        qs=self.get_queryset().filter(stock_name=q)
        serializer = self.get_serializer(qs, many=True)

        q2=request.query_params.get('code', None)
        qs2=self.get_queryset().filter(stock_code=q2)
        serializer = self.get_serializer(qs2, many=True)

        return Response(serializer.data)

    #기관 순매매량 높은 순으로 데이터 보여주기
    @action(detail=False, methods=['GET'])
    def highlist(self, requset):
        highlist = MyTopicInstitut.objects.all().order_by('institut_trading_volume')
        serializer = self.get_serializer(highlist, many=True)

        return Response(serializer.data)

class MyTopicForeignViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MyTopicForeign.objects.all()
    serializer_class=MyTopicForeignSerializer

    permission_classes= [permissions.IsAuthenticated]
    
    @action(detail=False, methods=['GET'])
    def search(self, request):
        q=request.query_params.get('name', None)
        qs=self.get_queryset().filter(stock_name=q)
        serializer = self.get_serializer(qs, many=True)

        q2=request.query_params.get('code', None)
        qs2=self.get_queryset().filter(stock_code=q2)
        serializer = self.get_serializer(qs2, many=True)
        
        return Response(serializer.data)

    #외국인 순매매량 높은 순으로 데이터 보여주기
    @action(detail=False, methods=['GET'])
    def highlist(self, requset):
        highlist = MyTopicForeign.objects.all().order_by('foreign_trading_volume')
        serializer = self.get_serializer(highlist, many=True)

        return Response(serializer.data)  

class MyTopicPriceBuyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MyTopicPriceBuy.objects.all()
    serializer_class=MyTopicPriceBuySerializer

    permission_classes= [permissions.IsAuthenticated]

    @action(detail=False, methods=['GET'])
    def search(self, request):
        q1=request.query_params.get('name', None)
        qs1=self.get_queryset().filter(stock_name=q1)
        serializer = self.get_serializer(qs1, many=True)

        q2=request.query_params.get('code', None)
        qs2=self.get_queryset().filter(stock_code=q2)
        serializer = self.get_serializer(qs2, many=True)


        return Response(serializer.data)

class MyTopicPriceSellViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MyTopicPriceSell.objects.all()
    serializer_class=MyTopicPriceSellSerializer

    permission_classes= [permissions.IsAuthenticated]
    
    @action(detail=False, methods=['GET'])
    def search(self, request):
        q1=request.query_params.get('name', None)
        qs1=self.get_queryset().filter(stock_name=q1)
        serializer = self.get_serializer(qs1, many=True)

        q2=request.query_params.get('code', None)
        qs2=self.get_queryset().filter(stock_code=q2)
        serializer = self.get_serializer(qs2, many=True)


        return Response(serializer.data)

class MyTopicNewsViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = MyTopicNews.objects.all()
    serializer_class=MyTopicNewsSerializer

    permission_classes= [permissions.IsAuthenticated]
    
    @action(detail=False, methods=['GET'])
    def search(self, request):
        q1=request.query_params.get('code', None)
        qs1=self.get_queryset().filter(stock_name=q1)
        serializer = self.get_serializer(qs1, many=True)

        q2=request.query_params.get('date', None)
        qs2=self.get_queryset().filter(stock_code=q2)
        serializer = self.get_serializer(qs2, many=True)


        return Response(serializer.data)