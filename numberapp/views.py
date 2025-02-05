from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from . import logic
import re


@api_view(["GET"])
@permission_classes([AllowAny])
def detailnum(request):
    number = request.query_params.get("number")


    #if number is missing
    if number is None:

        return Response(
            {

                "number":"Missing number",
                "error": True
            },
            status=status.HTTP_400_BAD_REQUEST
        )
    
    # Validate number format (allow negative integers but not decimals)
    if not re.match(r"^-?\d+$", number):
        return Response(
            {"message": number, "error": True},
            status=status.HTTP_400_BAD_REQUEST,
        )
    
    #convert 'number' to an integer
    number = int(number)

    data = {
        "number": number,
        "is_prime": logic.is_num_prime(abs(number)),
        "is_perfect": logic.is_num_perfect(abs(number)),
        "properties":logic.return_num_properties(abs(number)),
        "digit_sum": logic.sum_number_digit(abs(number)),
        "fun_fact":logic.get_funfact_for_number(number)
    }

    return Response(data=data, status=status.HTTP_200_OK)
