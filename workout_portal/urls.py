from django.urls import path

from views import Views

# from . import views

controller = Views()

urlpatterns = [
    path('', controller.index, name='index'),
    path('training/add', controller.add_training, name='add_training'),
    path('training/<int:training_id>/', controller.get_training, name='get_training'),
]
