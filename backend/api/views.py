from django.http import JsonResponse
from rest_framework.decorators import api_view

@api_view(['GET'])
def line_chart_data(request):
    data = {
        "labels": ["Jan", "Feb", "Mar", "Apr"],
        "data": [10, 20, 15, 25]
    }
    return JsonResponse(data)

@api_view(['GET'])
def bar_chart_data(request):
    data = {
        "labels": ["A", "B", "C", "D"],
        "data": [30, 40, 20, 50]
    }
    return JsonResponse(data)

@api_view(['GET'])
def pie_chart_data(request):
    data = {
        "labels": ["Category 1", "Category 2", "Category 3"],
        "data": [30, 50, 20]
    }
    return JsonResponse(data)

@api_view(['GET'])
def candlestick_data(request):
    data = {
        "data": [
            {"x": "2023-01-01", "open": 30, "high": 40, "low": 25, "close": 35},
            {"x": "2023-01-02", "open": 35, "high": 45, "low": 30, "close": 40},
            {"x": "2023-01-03", "open": 40, "high": 50, "low": 35, "close": 45},
            {"x": "2023-01-04", "open": 45, "high": 55, "low": 40, "close": 50},
            {"x": "2023-01-05", "open": 50, "high": 60, "low": 45, "close": 55},
        ]
    }
    return JsonResponse(data)

@api_view(['GET'])
def kpi_data(request):
    data = {
        "kpis": [
            {"title": "Revenue", "value": "$54,321", "trend": "up"},
            {"title": "Users", "value": "1,234", "trend": "up"},
            {"title": "Conversion", "value": "2.5%", "trend": "down"},
            {"title": "Avg. Session", "value": "5m", "trend": "up"},
        ]
    }
    return JsonResponse(data)