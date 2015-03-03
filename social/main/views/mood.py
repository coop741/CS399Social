from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from ..models import Mood


def mood(request, pk=None):
    if request.method == 'POST':
        if request.user.is_authenticated():
            # TODO validate
            # TODO add user to mood
            # TODO return created mood object
            return JsonResponse({'error': 'Not Implemented'}, status=501)
        else:
            # anonymous users are not allowed to post moods
            return JsonResponse({'error': 'Unauthorized.'}, status=403)
    if request.method == 'GET':
        if pk is None:
            all_moods = Mood.objects.all()
            # TODO serialize queryset
            return JsonResponse({'error': 'Not Implemented'}, status=501)
        else:
            one_mood = get_object_or_404(Mood, pk=1)
            # TODO serialize queryset
            return JsonResponse({'error': 'Not Implemented'}, status=501)

    return HttpResponseNotFound