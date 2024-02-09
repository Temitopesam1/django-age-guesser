from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services import get_age_and_dob

@csrf_exempt
def human_age_api(request):
    if request.method == 'POST':
        try:
            data = request.POST
            name = data.get('name')
            response_data = get_age_and_dob(name)
            return JsonResponse(response_data)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Only POST requests are allowed'}, status=405)
