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
               pickup_time = pickup.time.time()  
            elif isinstance(pickup.time, datetime.time):
                    pickup_time = pickup.time  
            else:
              raise TypeError("pickup.time should be a datetime.datetime or datetime.time object")
          
            pickup_datetime = datetime.combine(timezone.now().date(), pickup_time)
            print(pickup_datetime)
            
            if timezone.is_naive(pickup_datetime):
                pickup_datetime = timezone.make_aware(pickup_datetime)

            current_time = timezone.now()
            formatted_datetime = current_time.strftime('%Y-%m-%d %H:%M:%S')
            

           
            if current_time >= pickup_datetime:
                pickup.status= str("ready")
                print(pickup.status)
                print(pickup.time)

                pickup.save()

        return Response({'status': pickup.status})
    





    @action(detail=True, methods=['post'])
    def confirm(self, request, pk=None):
        pickup = get_object_or_404(PickUp, id=pk)
        if pickup.status == 'ready' and request.user == pickup.owner_fk:
            pickup.confirmation = True
            pickup.save()
            return Response({'status': 'confirmed', 'confirmation': pickup.confirmation})
        else:
            return Response({'error': 'You are not authorized to confirm this pickup or it is not ready yet.'}, status=403)





   