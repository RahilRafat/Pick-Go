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
# Create your views here.
from rest_framework import viewsets
from restaurant.models import Restaurant
from supreceipt.serializer import SubPriceSerializer

class RecieptViewSet(viewsets.ModelViewSet):
    queryset=TotalReciept.objects.all()
    serializer_class=RecieptSerializer
    permission_classes = [IsAuthenticated]

    def create(self , request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)


        user=request.user
        receipt_instance = serializer.save(user_fk=user)
        subserializer=RecieptSerializer (data =self.request.data)
        subserializer
        subserializer.is_valid(raise_exception= True)
        usser = CustomUser.objects.get(username = request.user)
        roral_reciept = subserializer.save(user_fk =usser)
   
        subreciet=Supreceipt.objects.filter(total_reciet_fk=receipt_instance)
        # print(type(subreciet))
        # for item in subserializer:
        #      roral_reciept.total_receipt += item.total_receipt 
        # return Response( roral_reciept.total_receipt)


        # return Response(subserializer.data)
        total_amount = 0
        for subreceipt in subreciet:
            total_amount += subreceipt.totalsupprice

        # Update the TotalReciept's total_receipt field with the calculated amount
        roral_reciept.total_receipt = total_amount
        roral_reciept.save()

        # Return the updated data
        usser = request.user
        restaurant = roral_reciept.res_fk
       
        # return Response({
        #     'order_id': roral_reciept.id,
        #     'total_receipt': roral_reciept.total_receipt,
        #     'detail': 'Receipt created and total updated.',
        #     'username':usser.username,
        #     # 'restaurant_name': restaurant.name
            
        # })
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
        # Fetch all TotalReceipts for the user
        total_receipts = TotalReciept.objects.filter(user_fk=user)
        # Fetch all Supreceipts related to these TotalReceipts
        return Supreceipt.objects.filter(total_reciet_fk__in=total_receipts)
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
                    
        