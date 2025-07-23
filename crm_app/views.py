from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Agent

class AgentInfoView(APIView):
    def get(self, request, telegram_id):
        try:
            agent = Agent.objects.get(telegram_id=telegram_id)
            return Response({
                "name": agent.name,
                "role": agent.role,
                "deals_in_progress": agent.deals_in_progress,
                "current_month_revenue": float(agent.current_month_revenue),
            })
        except Agent.DoesNotExist:
            return Response({"error": "Агент не найден."}, status=status.HTTP_404_NOT_FOUND)
