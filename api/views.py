from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .services import get_age_and_dob

@csrf_exempt
def human_age_api(request) -> JsonResponse:
    if request.method == 'POST':
        data = request.POST.dict()
        name = data.get('name')
        if name:
            response_data = get_age_and_dob(name)
            return JsonResponse(response_data)
        else:
            return JsonResponse({'error': 'Name parameter is missing'}, status=400)
    else:
        return JsonResponse({'error': 'Only POST method is supported'}, status=405)
