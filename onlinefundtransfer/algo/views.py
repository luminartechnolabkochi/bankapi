from django.shortcuts import render

# Create your views here.
from django.conf import settings
import os
from rest_framework import views
import json
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework import authentication
class Resources(views.APIView):

    def get(self,request):
        filename=request.query_params["filename"]

        path = "algo/static/" + filename
        with open(os.path.join(settings.BASE_DIR, path)) as file:
            file = json.load(file)


            return Response({"data":file})
    def post(self,request):
        # id=request.data.get("id")
        # name=request.data.get("name")
        # identifier=request.data.get("identifier")
        f=open("out.json","w")
        json.dump(request.data, f)


        return Response({"msg":request.data})



