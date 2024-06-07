from rest_framework .views import APIView
from django.http import JsonResponse
from rest_framework import status
from . models import*
from .serializers import*

class getPATIENT(APIView):
    def get(self,request):
        result = list(PATIENT.objects.filter().values())
        return JsonResponse(result,status = status.HTTP_200_OK,safe=False)



class getMEDICINE(APIView):
    def get(self,request):
        result = list(MEDICINE.objects.filter().values())
        return JsonResponse(result,status = status.HTTP_200_OK,safe=False)
    


class CreatePATIENT(APIView):
     def post(self,request):
        userData = CreatePATIENTserializer(data = request.data)
        try:
            if userData.is_valid():
                
                p_name = userData.data['name']
                p_mobile = userData.data['p_mobile']  
                p_address = userData.data['address']
                age = userData.data["age"]
                gender = userData.data["gender"]

                PATIENT.objects.create(
                    p_name = p_name,
                    p_mobile = p_mobile,
                    p_address = p_address,
                    p_age = age,
                    p_gender = gender
                ) 
                message = {"message":"PATIENT sucessfully added "} 
                return JsonResponse(message,status = status.HTTP_201_CREATED)
        except Exception as e:
            message = {"message":"something went wrong","error":str(e)}
            return JsonResponse(message,status.HTTP_400_BAD_REQUEST)
            


class updateAddressPatient(APIView):
     def put(self,request):
        userData = updateAddressPatientserializer(data = request.data)
        try:
            if userData.is_valid():
                p_address = userData.data['address']
                gender = userData.data["gender"]

                patientData = list(PATIENT.objects.filter(p_gender=gender).values())

                for i in patientData:
                    PATIENT.objects.filter(p_id = i["p_id"]).update(p_address=p_address)
                message = {"message":"PATIENT Address updated added "} 
                return JsonResponse(message,status = status.HTTP_201_CREATED)
        except Exception as e:
            message = {"message":"something went wrong","error":str(e)}
            return JsonResponse(message,status.HTTP_400_BAD_REQUEST)
