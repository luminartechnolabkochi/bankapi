from django.shortcuts import render
from rest_framework.decorators import action

from api.serilaizers import UserProfileSerializer,UserSerializer,TransactionSerializer
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.response import Response
from api .models import Transactions
# Create your views here.
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        serializer=self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return  Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
class FundTransfer(viewsets.ModelViewSet):
    # api/v1/transaction?to_acno=1002
    queryset = Transactions.objects.all()
    serializer_class = TransactionSerializer
    permission_classes = [IsAuthenticated]
    def create(self, request, *args, **kwargs):
        print(request.data)

        serializer=TransactionSerializer(data=request.data,context={"user":request.user.profile})
        if serializer.is_valid():
            serializer.save()
            return Response({"msg":"ok"})
    #     api/v1/fundtransfer/debit_transactions
    @action(methods=["GET"],detail=False)
    def debit_transactions(self,request,*args,**kwargs):
        transactions=Transactions.objects.filter(account=request.user.profile.account_number)
        serializer=TransactionSerializer(transactions,many=True)
        return Response(serializer.data)
