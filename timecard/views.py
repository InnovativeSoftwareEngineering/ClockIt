"""
View entrance functions.
"""

# Import system modules
import logging
import datetime

# Import third-party modules
import pytz

# Import Django modules
from django.http import HttpResponse
from django.core import serializers
from django.shortcuts import render
from django.utils import timezone
from django.utils.dateparse import parse_datetime
from django.contrib.auth.decorators import login_required

# Import project modules
from clockit.models import Project, Deliverable, Activity
from timecard.models import Task, TimeCard

__author__ = 'Alex Laird'
__copyright__ = 'Copyright 2014, Innovative Software Engineering'
__version__ = '0.0.1'

logger = logging.getLogger(__name__)


@login_required
def timecard(request):    
    return render(request, "timecard.html")


@login_required
def events_feed(request):
    timezone.activate(pytz.timezone(request.user.time_zone))

    start = datetime.datetime.strptime(request.GET['start'], '%Y-%m-%d').replace(tzinfo=pytz.utc)
    end = datetime.datetime.strptime(request.GET['end'], '%Y-%m-%d').replace(tzinfo=pytz.utc)

    tasks = Task.objects.filter(start__gte=start,
                                end__lte=end,
                                timecard__user_id=request.user.pk)

    return HttpResponse(serializers.serialize('json', tasks.all()))


@login_required
def event(request, id):
    timezone.activate(pytz.timezone(request.user.time_zone))

    event = Task.objects.get(pk=id, timecard__user_id=request.user.pk)

    return HttpResponse(serializers.serialize('json', event))


@login_required
def add_event(request):
    timezone.activate(pytz.timezone(request.user.time_zone))

    event = Task.objects.create(title=request.POST['title'],
                                start=timezone.make_aware(parse_datetime(request.POST['start']),
                                                          timezone.get_current_timezone()).astimezone(pytz.utc),
                                end=timezone.make_aware(parse_datetime(request.POST['end']),
                                                        timezone.get_current_timezone()).astimezone(pytz.utc),
                                description = request.POST['description'],
                                project = Project.objects.get(pk=request.POST['project_id']),
                                deliverable = Deliverable.objects.get(pk=request.POST['deliverable_id']),
                                activity = Activity.objects.get(pk=request.POST['activity_id']),
                                timecard = TimeCard.objects.get(pk=request.POST['timecard_id']),
                                user=request.user)

    return HttpResponse(serializers.serialize('json', event))


@login_required
def edit_event(request, id):
    timezone.activate(pytz.timezone(request.user.time_zone))

    event = Task.objects.get(pk=id, timecard__user_id=request.user.pk)

    if 'title' in request.POST:
        event.title = request.POST['title']
    if 'start' in request.POST:
        event.start = timezone.make_aware(parse_datetime(request.POST['start']),
                                          timezone.get_current_timezone()).astimezone(pytz.utc)
    if 'end' in request.POST:
        event.end = timezone.make_aware(parse_datetime(request.POST['end']),
                                        timezone.get_current_timezone()).astimezone(pytz.utc)
    if 'project_id' in request.POST:
        event.project = Project.objects.get(pk=request.POST['project_id'])
    if 'deliverable_id' in request.POST:
        event.deliverable = Deliverable.objects.get(pk=request.POST['deliverable_id'])
    if 'activity_id' in request.POST:
        event.activity = Activity.objects.get(pk=request.POST['activity_id'])

    event.save()

    return HttpResponse(serializers.serialize('json', event))


@login_required
def delete_event(request, id):
    timezone.activate(pytz.timezone(request.user.time_zone))

    event = Task.objects.get(pk=id, timecard__user_id=request.user.pk)

    event_json = serializers.serialize('json', event)
    event.delete()

    return HttpResponse(event_json)