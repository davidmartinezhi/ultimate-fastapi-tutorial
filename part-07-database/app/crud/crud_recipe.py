from app.crud.base import CRUDBase
from app.models.recipe import Recipe
from app.schemas.recipe import RecipeCreate, RecipeUpdate

# This class is a CRUD class that will be used to create CRUD operations for the Recipe model
# This inherits from the CRUDBase class and expects the Recipe model and the RecipeCreate and RecipeUpdate schemas
class CRUDRecipe(CRUDBase[Recipe, RecipeCreate, RecipeUpdate]):
    ...

# This instance of the CRUDRecipe class will be used to create CRUD operations for the Recipe model
recipe = CRUDRecipe(Recipe)
