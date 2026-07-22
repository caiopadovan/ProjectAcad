from rest_framework.routers import DefaultRouter
from .views import MuscularGroupViewSet, ExerciseViewSet, TrainingViewSet, TrainingExerciseViewSet, TrainingExecutionViewSet, ExerciseExecutionViewSet
 
router = DefaultRouter()                                         # DefaultRouter - Generate all CRUD URL's
router.register('muscular-groups', MuscularGroupViewSet)         # Recording all the paths
router.register('exercises', ExerciseViewSet)
router.register('trainings', TrainingViewSet)
router.register('training-exercises', TrainingExerciseViewSet)
router.register('training-executions', TrainingExecutionViewSet)
router.register('exercise-executions', ExerciseExecutionViewSet)

urlpatterns = router.urls