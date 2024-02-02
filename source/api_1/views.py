from django.http import JsonResponse, HttpResponse, QueryDict
from django.shortcuts import render
import json


def check_input(dict):
    a = dict.get('A')
    b = dict.get('B')

    if a is not None and b is not None:
        try:
            a = float(a)
            b = float(b)
            return a, b
        except ValueError:
            raise Exception('A and B must be numeric!')
    else:
        raise ValueError('A and B must exist!')



def add_view(request, *args, **kwargs):
    try:
        answer = {'A': request.GET.get('A'), 'B': request.GET.get('B')}
        a, b = check_input(answer)
        result = {"answer": a + b}
        return JsonResponse(result, safe=False)
    except ValueError as ve:
        return JsonResponse({'error': str(ve)}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def subtract_view(request, *args, **kwargs):
    try:
        answer = {'A': request.GET.get('A'), 'B': request.GET.get('B')}
        a, b = check_input(answer)
        result = {"answer": a - b}
        return JsonResponse(result, safe=False)
    except ValueError as ve:
        return JsonResponse({'error': str(ve)}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def multiply_view(request, *args, **kwargs):
    try:
        answer = {'A': request.GET.get('A'), 'B': request.GET.get('B')}
        a, b = check_input(answer)
        result = {"answer": a * b}
        return JsonResponse(result, safe=False)
    except ValueError as ve:
        return JsonResponse({'error': str(ve)}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)


def divide_view(request, *args, **kwargs):
    try:
        answer = {'A': request.GET.get('A'), 'B': request.GET.get('B')}
        a, b = check_input(answer)
        result = {"answer": a / b}
        return JsonResponse(result, safe=False)
    except ValueError as ve:
        return JsonResponse({'error': str(ve)}, status=400)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=400)
