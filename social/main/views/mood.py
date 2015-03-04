import json
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.core import serializers
from ..models.mood import Mood


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
            if 'user' in request.GET:
                # allows getting only moods of user
                data = serializers.serialize("json",
                                             Mood.objects.filter(user__id=request.GET['user']))
            else:
                # all moods regardless of user
                data = serializers.serialize("json", Mood.objects.all())
            return JsonResponse(json.loads(data), status=200, safe=False)
        else:
            one_mood = get_object_or_404(Mood, pk=pk)
            data = serializers.serialize("json", [one_mood])
            return JsonResponse(json.loads(data)[0], status=200, safe=False)

    return HttpResponseNotFound
