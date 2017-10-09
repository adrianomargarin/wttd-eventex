from django.shortcuts import render
from django.shortcuts import get_object_or_404

from eventex.core.models import Talk
from eventex.core.models import Course
from eventex.core.models import Speaker

from django.views.generic import ListView
from django.views.generic import DetailView


home = ListView.as_view(template_name='index.html', model=Speaker)


speaker_detail = DetailView.as_view(model=Speaker)


talk_list = ListView.as_view(model=Talk)
