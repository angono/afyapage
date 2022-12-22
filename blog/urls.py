from django.urls import path, include
from .views import *


urlpatterns = [
	path('', homepage_list_view, name='homepage_list'),
	# Pregnancy
	path('pregnancy-list/', pregnancy_list_view, name='pregnancy_list'),
	path('pregnancy-detail/<str:pk>/', pregnancy_detail_view, name='pregnancy_detail'),
	path('pregnancy-create/', pregnancy_create_view, name='pregnancy_create'),
	path('pregnancy-update/<str:pk>/', pregnancy_update_view, name='pregnancy_update'),
	path('pregnancy-delete/<str:pk>/', pregnancy_delete_view, name='pregnancy_delete'),
	# Menopause
	path('menopause-list/', menopause_list_view, name='menopause_list'),
	path('menopause-detail/<str:pk>/', menopause_detail_view, name='menopause_detail'),
	path('menopause-create/', menopause_create_view, name='menopause_create'),
	path('menopause-update/<str:pk>/', menopause_update_view, name='menopause_update'),
	path('menopause-delete/<str:pk>/', menopause_delete_view, name='menopause_delete'),
	# Intercourse
	path('intercourse-list/', intercourse_list_view, name='intercourse_list'),
	path('intercourse-detail/<str:pk>/', intercourse_detail_view, name='intercourse_detail'),
	path('intercourse-create/', intercourse_create_view, name='intercourse_create'),
	path('intercourse-update/<str:pk>/', intercourse_update_view, name='intercourse_update'),
	path('intercourse-delete/<str:pk>/', intercourse_delete_view, name='intercourse_delete'),
	# Ovulation
	path('ovulation-list/', ovulation_list_view, name='ovulation_list'),
	path('ovulation-detail/<str:pk>/', ovulation_detail_view, name='ovulation_detail'),
	path('ovulation-create/', ovulation_create_view, name='ovulation_create'),
	path('ovulation-update/<str:pk>/', ovulation_update_view, name='ovulation_update'),
	path('ovulation-delete/<str:pk>/', ovulation_delete_view, name='ovulation_delete'),
	# Menstruation
	path('menstruation-list/', menstruation_list_view, name='menstruation_list'),
	path('menstruation-detail/<str:pk>/', menstruation_detail_view, name='menstruation_detail'),
	path('menstruation-create/', menstruation_create_view, name='menstruation_create'),
	path('menstruation-update/<str:pk>/', menstruation_update_view, name='menstruation_update'),
	path('menstruation-delete/<str:pk>/', menstruation_delete_view, name='menstruation_delete'),

]








