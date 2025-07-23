from rest_framework import serializers
from .models import Agent

class AgentInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Agent
        fields = ['name', 'role', 'deals_in_progress', 'current_month_revenue']
