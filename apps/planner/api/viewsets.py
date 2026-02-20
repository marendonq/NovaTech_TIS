from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from django.contrib.gis.geos import Point

from .services import MealPlannerService
from .serializers import MealPlanSerializer, UserLocationSerializer

class MealPlanViewSet(viewsets.ViewSet):
    """
    CBV que expone la lógica del Builder y Service a través de la API.
    Cumple con SRP: Solo maneja Request/Response.
    """
    
    # Inyectamos el servicio para seguir el principio de DIP
    service = MealPlannerService()

    @action(detail=False, methods=['post'], url_path='generate-plan')
    def generate_plan(self, request):
        """
        Endpoint: POST /api/meal-planner/generate-plan/
        Cuerpo: {"latitude": 4.60, "longitude": -74.08}
        """
        # 1. Validación de entrada (Input Validation)
        serializer = UserLocationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        # 2. Preparar datos para el servicio
        user_location = Point(
            serializer.validated_data['longitude'],
            serializer.validated_data['latitude']
        )
        
        # 3. Orquestación delegada al Service Layer
        # El ViewSet no sabe NADA de Mifflin-St Jeor ni de PostGIS
        try:
            plan = self.service.generate_daily_plan(
                user_profile=request.user.profile,
                user_location=user_location
            )
            
            # 4. Formateo de respuesta
            response_data = MealPlanSerializer(plan, many=True).data
            return Response(response_data, status=status.HTTP_200_OK)
            
        except Exception as e:
            # Manejo de errores básico (en producción usarías un logger)
            return Response(
                {"error": str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )
