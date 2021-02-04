from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'users',views.UserViewSet)
router.register(r'store',views.StoreViewSet)
router.register(r'position',views.PositionViewSet)
urlpatterns = [
	path('', include(router.urls)),
	# path('api-auth/',include('rest_framework.urls',namespace='rest_framework')),
	# path('create-user',views.create_user),
	path('user',views.UserView.as_view(),name='user'),
	path(r'scanticket',views.ScanTicket.as_view(),name='scanticket'),
	path(r'ticket',views.TicketView.as_view(),name='ticket'),
	path(r'slots',views.SlotsView.as_view(),name='slots'),
	path('session',views.SessionView.as_view(),name='session')
]