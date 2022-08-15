from django.urls import path,register_converter
from . import views,converters

register_converter(converters.FourDigitYearConverter,'yyyy')
urlpatterns = [
    path('reg/',views.showformdata,name='reg'),
    path('student/<my_id>/',views.studentdetails,name='student')
]