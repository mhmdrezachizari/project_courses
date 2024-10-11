from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from order.models import Order
from courses.models import Course
class CustomAdmin(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        order = get_object_or_404(Order, user=request.user)
        if order.is_paid:
            courses = order.items.all()
            course_links = [{"name": course.name, "link": course.Linkdore} for course in courses]
            return Response({"courses": course_links}, status=200)
        else:
            return Response({"message": "پرداخت تکمیل نشده است."}, status=403)
