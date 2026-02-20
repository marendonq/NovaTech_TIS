from typing import List, Optional
from .models import Meal, Ingredient
from django.db.models import QuerySet

class MealPlanBuilder:
    """
    Implements a constraint-based algorithm to match restaurant 
    items with user-specific nutritional and geographic needs.
    """
    
    def __init__(self, user):
        self.user = user
        self.remaining_macros = {}
        self.excluded_ingredients = []
        self.available_restaurants = []
        self._plan = []

    def set_constraints(self, remaining_macros: dict) -> 'MealPlanBuilder':
        """Sets target Protein, Carbs, and Fats."""
        self.remaining_macros = remaining_macros
        return self

    def filter_allergens(self, allergens: QuerySet) -> 'MealPlanBuilder':
        """Identifies ingredients that must be excluded from the search."""
        self.excluded_ingredients = list(allergens.values_list('id', flat=True))
        return self

    def match_with_restaurants(self, restaurants: List) -> 'MealPlanBuilder':
        """Filters the pool of potential meals by proximity/location."""
        self.available_restaurants = restaurants
        return self

    def _is_meal_safe(self, meal: Meal) -> bool:
        """Checks if a meal contains any user allergens (Atomic Tracking)."""
        # Based on Wiki Section 4: Atomic tracking of ingredients
        meal_ingredients = meal.ingredients.values_list('id', flat=True)
        return not any(ing in self.excluded_ingredients for ing in meal_ingredients)

    def build(self) -> List[Meal]:
        """
        The core constraint-based algorithm.
        Matches menu items to remaining macros while respecting allergens.
        """
        # 1. Start with meals from nearby restaurants
        potential_meals = Meal.objects.filter(
            restaurant__in=self.available_restaurants
        ).prefetch_related('ingredients')

        for meal in potential_meals:
            # 2. Check Allergen Constraints
            if not self._is_meal_safe(meal):
                continue

            # 3. Check Macro Constraints (Protein, Carbs, Fats)
            # This is a simplified version of the "Constraint-based algorithm"
            if (meal.protein <= self.remaining_macros.get('protein', 0) and
                meal.carbs <= self.remaining_macros.get('carbs', 0) and
                meal.fat <= self.remaining_macros.get('fat', 0)):
                
                self._plan.append(meal)
                
                # Update local remaining macros for the next iteration
                self.remaining_macros['protein'] -= meal.protein
                self.remaining_macros['carbs'] -= meal.carbs
                self.remaining_macros['fat'] -= meal.fat

        return self._plan
