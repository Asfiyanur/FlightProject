from django.shortcuts import render
from rest_framework import viewsets
from .serializers import FlightSerializer,ReservationSerializer
from .models import Flight,Reservation

from .permission import IsStafforReadOnly


# Create your views here.
class FlightView(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer
    permission_classes = (IsStafforReadOnly,)
    
    
    
class ReservationView(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer