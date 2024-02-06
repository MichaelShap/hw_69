from django.http import JsonResponse, HttpResponse, QueryDict, HttpResponseNotAllowed
from django.shortcuts import render
import json
from django.views.decorators.csrf import ensure_csrf_cookie


@ensure_csrf_cookie
def get_token_view(request, *args, **kwargs):
    if request.method == 'GET':
        return HttpResponse()
    return HttpResponseNotAllowed(['GET'])


def data_checking(request_body)-> dict[str, str|float]:
    try:
        data = json.loads(request_body)
        data['A'], data['B'] = float(data['A']), float(data['B'])
    except json.decoder.JSONDecodeError:
        return {'error': 'Not JSON format'}
    except KeyError as e:
        return {'error': f'Data missing {e}'}
    except ValueError:
        return {'error': f'Values must be digits'}
    return data


def add_view(request, *args, **kwargs):
    if request.method == 'POST':
        data = data_checking(request.body)
        if 'error' in data:
            return JsonResponse(data, status=400)
        return JsonResponse({'answer': data['A'] + data['B']}, status=200)



def subtract_view(request, *args, **kwargs):
    if request.method == 'POST':
        data = data_checking(request.body)
        if 'error' in data:
            return JsonResponse(data, status=400)
        return JsonResponse({'answer': data['A'] - data['B']}, status=200)


def multiply_view(request, *args, **kwargs):
    if request.method == 'POST':
        data = data_checking(request.body)
        if 'error' in data:
            return JsonResponse(data, status=400)
        return JsonResponse({'answer': data['A'] * data['B']}, status=200)


def divide_view(request, *args, **kwargs):
    if request.method == 'POST':
        data = data_checking(request.body)
        if 'error' in data:
            return JsonResponse(data, status=400)
        try:
            return JsonResponse({'answer': data['A'] / data['B']}, status=200)
        except ZeroDivisionError:
            return JsonResponse({'error': 'Division by zero'}, status=400)
