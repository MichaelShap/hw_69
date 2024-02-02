from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
import json


def check_input(dict):
    if isinstance(dict.get('A'), (int, float)) and isinstance(dict.get('B'), (int, float)):
        a = dict.get('A')
        b = dict.get('B')
        return a, b
    else:
        raise Exception('A and B must be digits!')


# Create your views here.
def add_view(request, *args, **kwargs):
    answer = {}
    if request.body:
        answer = json.loads(request.body)
    else:
        return JsonResponse({'error': 'No data provided'}, status=400)

    try:
        a, b = check_input(answer)
        result = {
            "answer": a + b,
        }
        return JsonResponse(result, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def subtract_view(request, *args, **kwargs):
    answer = {}
    if request.body:
        answer = json.loads(request.body)
    else:
        return JsonResponse({'error': 'No data provided'}, status=400)

    try:
        a, b = check_input(answer)
        result = {
            "answer": a - b,
        }
        return JsonResponse(result, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def multiply_view(request, *args, **kwargs):
    answer = {}
    if request.body:
        answer = json.loads(request.body)
    else:
        return JsonResponse({'error': 'No data provided'}, status=400)

    try:
        a, b = check_input(answer)
        result = {
            "answer": a * b,
        }
        return JsonResponse(result, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def divide_view(request, *args, **kwargs):
    answer = {}
    if request.body:
        answer = json.loads(request.body)
    else:
        return JsonResponse({'error': 'No data provided'}, status=400)

    try:
        a, b = check_input(answer)
        if b == 0:
            return JsonResponse({'error': 'Division by zero!'}, status=400)
        else:
            result = {
                "answer": a / b,
            }
            return JsonResponse(result, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
