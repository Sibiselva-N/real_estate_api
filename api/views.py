import datetime
import random, string
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import UserModel, EstateModel, ImageModel
from .serializers import UserSerializer, EstateSerializer


def randomword(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))


@api_view(['POST'])
def sign_up(request):
    data = request.data
    if 'name' in data and 'email' in data and 'password' in data and 'number' in data:
        users = UserModel.objects.filter(email=data['email'])
        otp = random.randrange(1000, 9999)
        if len(users) == 0:
            user = UserModel(name=data['name'], email=data['email'], password=data['password'], number=data['number'],
                             time=datetime.datetime.now(), otp=otp, token="")
            if 'profile' in data:
                user.profile = data['profile']
            subject = 'OTP'
            message = f'Hi {data["name"]}, thank you for registering our app.\nOTP is {otp}'
            email_from = settings.EMAIL_HOST_USER
            recipient_list = [data['email'], ]
            send_mail(subject, message, email_from, recipient_list)
            user.save()
            user_ser = UserSerializer(user, many=False)
            return Response({"status": "success", "message": "OTP is sent to your mail address", "data": user_ser.data})
        else:
            return Response({"status": "failed", "message": "email already exists"})
    else:
        return Response({"status": "failed", "message": "Please provide all fields"})


@api_view(['POST'])
def verify_otp(request):
    data = request.data
    if "id" in data and "otp" in data:
        user_list = UserModel.objects.filter(id=data['id'])
        if len(user_list) == 1:
            if data['otp'] == user_list[0].otp:
                user_list[0].token = randomword(16)
                user_list[0].save()
                user_ser = UserSerializer(user_list[0], many=False)
                return Response(
                    {"status": "success", "message": "OTP Verified", "data": user_ser.data})
            else:
                return Response({"status": "failed", "message": "Invalid OTP"})
        else:
            return Response({"status": "failed", "message": "User ID not found"})
    else:
        return Response({"status": "failed", "message": "Please provide all fields"})


@api_view(['POST'])
def login(request):
    data = request.data
    if "email" in data and "password" in data:
        user_list = UserModel.objects.filter(email=data['email'])
        if len(user_list) == 1:
            if data['password'] == user_list[0].password:
                user_list[0].token = randomword(16)
                user_list[0].save()
                user_ser = UserSerializer(user_list[0], many=False)
                return Response(
                    {"status": "success", "message": "Login Success", "data": user_ser.data})
            else:
                return Response({"status": "failed", "message": "Invalid Password"})
        else:
            return Response({"status": "failed", "message": "User not found"})
    else:
        return Response({"status": "failed", "message": "Please provide all fields"})


@api_view(['POST'])
def update_user(request):
    data = request.data
    if 'name' in data and 'email' in data and 'password' in data and 'number' in data and "id" in data:
        users = UserModel.objects.filter(id=data['id'])
        if len(users) == 1:
            users[0].name = data['name']
            users[0].email = data['email']
            users[0].password = data['password']
            users[0].number = data['number']
            if 'profile' in data:
                users[0].profile = data['profile']
            users[0].save()
            user_ser = UserSerializer(users[0], many=False)
            return Response({"status": "success", "message": "User profile updated", "data": user_ser.data})
        else:
            return Response({"status": "failed", "message": "User not found"})
    else:
        return Response({"status": "failed", "message": "Please provide all fields"})


@api_view(['POST'])
def add_estate(request):
    data = request.data
    if 'location' in data and 'size' in data and 'price' in data and 'amenities' in data:

        estate = EstateModel(location=data['location'], size=data['size'], price=data['price'],
                             amenities=data['amenities']
                             )
        if 'images' in data:
            for i in data['images']:
                estate.images.add(ImageModel(image=i))
        estate.save()
        estate_ser = EstateSerializer(estate, many=False)
        return Response({"status": "success", "message": "Estate added", "data": estate_ser.data})

    else:
        return Response({"status": "failed", "message": "Please provide all fields"})


@api_view(['POST'])
def get_estate(request):
    estates = EstateModel.objects.all()
    estate_ser = EstateSerializer(estates, many=True)
    return Response({"status": "success", "message": "Estate fetched", "data": estate_ser.data})


@api_view(['POST'])
def single_estate(request):
    data = request.data
    if 'id' in data:
        estate = EstateModel.objects.filter(id=data['id'])
        if len(estate) == 1:
            estate_ser = EstateSerializer(estate[0], many=False)
            return Response({"status": "success", "message": "Estate fetched", "data": estate_ser.data})
        else:
            return Response({"status": "failed", "message": "Estate not found"})
    else:
        return Response({"status": "failed", "message": "Please provide all fields"})


@api_view(['POST'])
def single_estate(request):
    data = request.data
    if 'id' in data:
        estate = EstateModel.objects.filter(id=data['id'])
        if len(estate) == 1:
            estate_ser = EstateSerializer(estate[0], many=False)
            return Response({"status": "success", "message": "Estate fetched", "data": estate_ser.data})
        else:
            return Response({"status": "failed", "message": "Estate not found"})
    else:
        return Response({"status": "failed", "message": "Please provide all fields"})


@api_view(['POST'])
def update_estate(request):
    data = request.data
    if 'location' in data and 'size' in data and 'price' in data and 'amenities' in data and 'id' in data:
        est = EstateModel.objects.filter(id=data['id'])
        if len(est) == 1:
            est[0].location = data['location']
            est[0].size = data['size']
            est[0].price = data['price']
            est[0].amenities = data['amenities']
            if 'images' in data:
                for i in data['images']:
                    est[0].images.add(ImageModel(image=i))
            est[0].save()
            estate_ser = EstateSerializer(est[0], many=False)
            return Response({"status": "success", "message": "Estate updated", "data": estate_ser.data})
        else:
            return Response({"status": "failed", "message": "Estate not found"})
    else:
        return Response({"status": "failed", "message": "Please provide all fields"})


@api_view(['POST'])
def delete_estate(request):
    data = request.data
    if 'id' in data:
        est = EstateModel.objects.filter(id=data['id'])
        if len(est) == 1:
            est[0].delete()
            return Response({"status": "success", "message": "Estate deleted"})
        else:
            return Response({"status": "failed", "message": "Estate not found"})
    else:
        return Response({"status": "failed", "message": "Please provide all fields"})
