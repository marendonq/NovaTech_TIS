from typing import List, Dict, Any
from django.contrib.gis.geos import Point
from .models import DailyLog, Restaurant
from .selectors import get_nearby_healthy_restaurants
# Estos son los archivos que ya tienes definidos aparte
from .factories import MealFactory
from .builders import MealPlanBuilder

class MealPlannerService:
    """
    Orquesta la creación de planes de comida respetando 
    las restricciones de macros, alérgenos y ubicación.
    """

    @staticmethod
    def generate_daily_plan(user_profile, user_location: Point) -> Dict[str, Any]:
        # 1. Obtener el estado actual del usuario (Selectors)
        nearby_restaurants = get_nearby_healthy_restaurants(
            user_location=user_location, 
            max_dist_km=5
        )

        # 2. Calcular Macros Restantes (Business Logic)
        # Aquí se aplicaría la ecuación de Mifflin-St Jeor definida en la Wiki
        daily_log, _ = DailyLog.objects.get_or_create(profile=user_profile)
        remaining_macros = user_profile.calculate_remaining_macros(daily_log)

        # 3. Orquestar el Builder (Ensamblaje del Plan)
        # El Builder maneja la complejidad de "encajar" piezas en el puzzle nutricional
        builder = MealPlanBuilder(user=user_profile)
        
        plan = (
            builder
            .set_constraints(remaining_macros)
            .filter_allergens(user_profile.allergens.all())
            .match_with_restaurants(nearby_restaurants)
            .build()
        )

        return plan

    @staticmethod
    def log_selected_meal(user_profile, meal_data: Dict[str, Any]):
        """
        Usa el Factory para persistir la elección del usuario de forma limpia.
        """
        # El Factory se encarga de la instanciación compleja de los modelos
        meal_instance = MealFactory.create_from_data(meal_data)
        
        # Actualizamos el log diario
        daily_log = DailyLog.objects.get(profile=user_profile)
        daily_log.add_meal(meal_instance)
        
        return meal_instan
