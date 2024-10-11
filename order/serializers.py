from rest_framework import serializers
from .models import Order
from courses.models import Course

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'price']  # فیلدهای مورد نیاز برای نمایش

class OrderSerializer(serializers.ModelSerializer):
    items = CourseSerializer(many=True)  # سریالایزر برای آیتم‌های داخل سفارش

    class Meta:
        model = Order
        fields = ['id', 'items', 'totalprice']  # فیلدهای سفارش که می‌خواهید نمایش داده شود


class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = ['imageupload']

    def to_representation(self, instance):
        # نمایش URL تصویر به عنوان پاسخ
        representation = super().to_representation(instance)
        representation['imageupload'] = instance.imageupload.url  # فقط URL تصویر را برمی‌گردانیم
        return representation