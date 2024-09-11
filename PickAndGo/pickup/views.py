from django.shortcuts import render

# Create your views here.
from django.utils import timezone
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from .models import PickUp
from datetime import datetime
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from .serializer import pickupserializer
from .permissions import IsOwnerOrReadOnly

class pickviews(viewsets.ModelViewSet):

    queryset = PickUp.objects.all()
    serializer_class = pickupserializer
    permission_classes = [IsOwnerOrReadOnly]


  
    def retrieve(self, request, pk=None):
        pickup = get_object_or_404(PickUp, id=pk)

        if pickup.time:
            print(pickup.time)
            if isinstance(pickup.time, datetime):
               pickup_time = pickup.time.time()  # Extract time part
            elif isinstance(pickup.time, datetime.time):
                    pickup_time = pickup.time  # Use directly if already time
            else:
              raise TypeError("pickup.time should be a datetime.datetime or datetime.time object")
            # pickup_datetime = datetime.combine(timezone.now().date(), pickup.time)
            # print(pickup_datetime)
            pickup_datetime = datetime.combine(timezone.now().date(), pickup_time)
            print(pickup_datetime)
            # Ensure pickup_datetime is timezone-aware
            if timezone.is_naive(pickup_datetime):
                pickup_datetime = timezone.make_aware(pickup_datetime)

            current_time = timezone.now()
            formatted_datetime = current_time.strftime('%Y-%m-%d %H:%M:%S')
            # print(formatted_datetime)

            # Update the status if the current time is greater than or equal to the pickup time
            if current_time >= pickup_datetime:
                pickup.status= str("ready")
                print(pickup.status)
                print(pickup.time)

                pickup.save()

        # Return the updated status in the response
        return Response({'status': pickup.status})
    





    @action(detail=True, methods=['post'])
    def confirm(self, request, pk=None):
        pickup = get_object_or_404(PickUp, id=pk)

        # Check if the status is ready and user is the owner
        if pickup.status == 'ready' and request.user == pickup.owner_fk:
            pickup.confirmation = True
            pickup.save()
            return Response({'status': 'confirmed', 'confirmation': pickup.confirmation})
        else:
            return Response({'error': 'You are not authorized to confirm this pickup or it is not ready yet.'}, status=403)





    # def update(self,request, pk=None):
    #     pickup = get_object_or_404(PickUp, id=pk)

    #     if pickup.time:
    #         print(pickup.time)
           
    #         # pickup_datetime = datetime.combine(timezone.now().date(), pickup.time)
    #         if isinstance(pickup.time, datetime):
    #          pickup_time = pickup.time.time() 
    #         elif isinstance(pickup.time, datetime.time):
    #                 pickup_time = pickup.time 
    #     else:
    #         pickup_time = pickup.time

    #         pickup_datetime = datetime.combine(timezone.now().date(), pickup_time)

    #         print(pickup_datetime)
            
    #         if timezone.is_naive(pickup_datetime):
    #             pickup_datetime = timezone.make_aware(pickup_datetime)

    #         current_time = timezone.now()
    #         formatted_datetime = current_time.strftime('%Y-%m-%d %H:%M:%S')
            
    #         if current_time >= pickup_datetime:
    #             pickup.status= str("confirmed")
    #             print(pickup.status)
    #             print(pickup.time)
    #             print(current_time)

    #             pickup.save()
    #         return Response({'status': pickup.status})    
    
