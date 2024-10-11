# استفاده از تصویر پایه Django
FROM python:3.11

# تنظیم مسیر کاری
WORKDIR /app

# کپی کردن فایل‌های مورد نیاز
COPY requirements.txt /app/

# نصب وابستگی‌ها
RUN pip install --no-cache-dir -r requirements.txt

# کپی کردن بقیه کد پروژه
COPY . /app/

# اجرای مایگریشن‌های دیتابیس
RUN python manage.py migrate

# جمع‌آوری فایل‌های استاتیک
RUN python manage.py collectstatic --noinput

# اجرای سرور Django
CMD ["gunicorn", "core.wsgi:application", "--bind", "0.0.0.0:8000"]
