from django.shortcuts import redirect, render
from django.contrib import messages
from django.views import View

from django.utils import timezone
from home.models import YtVideoData

from django.http import HttpResponse

import csv
from django.db.models import Q
from django.db import transaction


class YoutubeVideosSubtitles(View):
    """

    method = [get]

    args : self,request

    return : it will display our all question registered into our application

    Base View


    """

    template_name = "yt/title_search.html"

    def get(self, request):
        message = self.request.GET.get("message")
        error = self.request.GET.get("error")

        search = self.request.GET.get("search")
        vd_lists = []
        filter_come = ""

        if search and search != "None":
            filter_come = "yes"
            search = search.strip()
            vd_append = YtVideoData.objects.filter(
                title__istartswith=search
            ).order_by("-id")
            vd_lists.extend(list(vd_append))

        if not filter_come:
            vd_lists = YtVideoData.objects.all().order_by("-id")

        return render(request, self.template_name, locals())

    def post(self, request):
        try:
            search = self.request.POST.get("search")
            vd_lists = []
            filter_come = ""

            if search and search != "None":
                filter_come = "yes"
                search = search.strip()
                vd_append = YtVideoData.objects.filter(
                    title__istartswith=search
                ).order_by("-id")
                vd_lists.extend(list(vd_append))

            return render(request, self.template_name, locals())
        except :
            return render(request, self.template_name, locals())


class GroupLayout(View):
    """

    method = [get]

    args : self,request

    return : it will display our all question registered into our application

    Base View


    """

    template_name = "yt/group_layout.html"

    def get(self, request):

        return render(request, self.template_name, locals())
