import json
from django.http import JsonResponse, HttpResponseNotFound
from django.shortcuts import get_object_or_404
from django.core import serializers
from ..models.mood import Mood

# TODO Custom serializer for queryset


def mood(request, pk=None):
    """
    This view exposes a Mood model as a rest resource.

    :param request: http request
    :param pk: primary key for a mood
    :return:
    """
    if request.method == 'POST':
        if request.user.is_authenticated():
            # TODO validate
            data = json.loads(request.POST['data'])
            description = data['description']

            # Create Mood
            m = Mood(user=request.user, description=description)
            m.save()

            # Return newly created Mood to user
            response_data = serializers.serialize("json", [m])
            return JsonResponse(json.loads(response_data)[0], status=201)
        else:
            # anonymous users are not allowed to post moods
            return JsonResponse({'error': 'Unauthorized.'}, status=403)

    if request.method == 'GET':
        if pk is None:
            # GET MANY
            if 'user' in request.GET:
                # Search based on username
                # allows getting only moods of user
                query = Mood.objects.filter(user__id=request.GET['user'])
                data = serializers.serialize("json", query)
                return JsonResponse(json.loads(data), status=200, safe=False)
            else:
                # GET MANY
                # all moods regardless of user
                query = Mood.objects.all()
                data = serializers.serialize("json", query)
                return JsonResponse(json.loads(data), status=200, safe=False)
        else:
            # GET ONE
            one_mood = get_object_or_404(Mood, pk=pk)
            data = serializers.serialize("json", [one_mood])
            return JsonResponse(json.loads(data)[0], status=200, safe=False)

    if request.method == 'PUT' or request.method == 'PATCH':
        # TODO verify user owns mood or has permission
        return JsonResponse({'error': "Not Implemented"}, status=501)

    if request.method == 'DELETE':
        # TODO verify user owns mood or has permission
        return JsonResponse({'error': "Not Implemented"}, status=501)

    return HttpResponseNotFound
