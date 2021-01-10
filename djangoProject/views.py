import random

from django.http import HttpResponse


def get_random_number_view(request):
    random_number = random.random()
    return HttpResponse('Chosen number: {}'.format(random_number))

