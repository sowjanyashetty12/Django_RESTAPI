from django.shortcuts import render
from django.http import JsonResponse
from projects.models import product
from projects.serializers import product_serializer
from django.forms.models import model_to_dict
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
# just for connecting the request and endpoint
# def api_home(request):
#     return JsonResponse({"message":"this is the api response"})


# def api_home(request):
#    model_data=product.objects.all().order_by("?").first()
# #    data={}
# #    data["title"]=model_data.title
# #    data["description"]=model_data.description
# #    data["price"]=model_data.price
# #    return JsonResponse(data)

# #    data=model_to_dict(model_data)
#    data=model_to_dict(model_data,fields=['id','title','price'])
#    return JsonResponse(data)

#CONVERTING THE ABOVE VIEW TO DJANGO RESTFRAMEWORK VIEW

# @api_view(["GET"])
# def api_home(request):
#  model_data=product.objects.all().order_by("?").first()
#  data=model_to_dict(model_data,fields=['price','sale_price'])
#  return Response(data)


#USING SERIALIZERS

# @api_view(["GET"])
# def api_home(request):
#    instance=product.objects.all().order_by("?").first()
#    responsedata=product_serializer(instance).data 
#    return Response(responsedata)

#POST

@api_view(["POST"])
def api_home(request,*args, **kwargs):
#  data=request.data
 serializer=product_serializer(data=request.data)
 if serializer.is_valid():
   serializer.save()
   print(serializer.data)
   return Response(serializer.data)
 else:
            print(serializer.errors)  # Print errors to debug
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)