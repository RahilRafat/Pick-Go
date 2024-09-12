from rest_framework import generics ,permissions,status
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from .models import TotalReciept
from totalreceipt.serializer import RecieptSerializer
from users.models import CustomUser
from supreceipt.models import Supreceipt
from supreceipt.serializer import SubPriceSerializer
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from restaurant.models import Restaurant
from supreceipt.serializer import SubPriceSerializer
from .permissions import IsUser

class RecieptViewSet(viewsets.ModelViewSet):
    queryset=TotalReciept.objects.all()
    serializer_class=RecieptSerializer
    permission_classes = [IsAuthenticated,IsUser]

    def create(self , request,*args,**kwargs):

        data=request.data
        data['user_fk']= request.user.id
      
        serializer = self.get_serializer(data=data)
        serializer.is_valid(raise_exception=True)


        receipt_instance = serializer.save(user_fk=request.user)
        subserializer=RecieptSerializer (data =self.request.data)
        subserializer
        subserializer.is_valid(raise_exception= True)
        usser = CustomUser.objects.get(username = request.user)
        roral_reciept = subserializer.save(user_fk =usser)
   
        subreciet=Supreceipt.objects.filter(total_reciet_fk=receipt_instance)
      
        total_amount = 0
        for subreceipt in subreciet:
            total_amount += subreceipt.totalsupprice

        roral_reciept.total_receipt = total_amount
        roral_reciept.save()

        
        usser = request.user
        restaurant = roral_reciept.res_fk
       
     
        response_data = {
        'order_id': roral_reciept.id,
        'total_receipt': roral_reciept.total_receipt,
        'detail': 'Receipt created and total updated.',
        'username': usser.username
    }
        print(restaurant)
    
        if restaurant:
            response_data['restaurant_name'] = restaurant.name
        else:
            response_data['restaurant_name'] = 'Unknown'

        return Response(response_data)
    


class UserOrderListView(generics.ListAPIView):
    serializer_class = RecieptSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        user=self.request.user
        return TotalReciept.objects.filter(user_fk=user)
    




class UserOrderHistoryView(generics.ListAPIView):
    serializer_class = SubPriceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        user = self.request.user
       
        total_receipts = TotalReciept.objects.filter(user_fk=user)
        
        return Supreceipt.objects.filter(total_reciet_fk__in=total_receipts)
                    
                    
                    
                    

                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
        