from rest_framework import serializers
from .models import *

class UserReadSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('user_id','name','phone_number','email_address','isManager','managed_store_id')
		depth=2
		
class UserWriteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = User
		fields = ('user_id','name','phone_number','email_address','isManager','managed_store_id')

class TicketReadSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ticket
		fields = ('ticket_id','created_at','status','time_of_request','time_of_entry','time_of_exit','assigned_to_user','assigned_to_store','categories_to_visit')
		depth=2
class TicketWriteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Ticket
		fields = ('ticket_id','created_at','status','time_of_request','time_of_entry','time_of_exit','assigned_to_user','assigned_to_store','categories_to_visit')
class PositionSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Position
		fields = ('address','latitude','longitude')
class StoreWriteSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Store
		fields = ('store_id','location','max_customers','current_customers','name')

class StoreReadSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Store
		fields = ('store_id','location','max_customers','current_customers','name')
		depth=2


