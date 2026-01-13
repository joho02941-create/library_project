from rest_framework import serializers
from rest_framework.exceptions import ValidationError

from .models import Book

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = '__all__'

    def validate(self, data):
        title = data.get('title', None)
        author = data.get('author', None)

        # checks if title items contains only alphabetical chars
        if not title.isalpha():
            raise ValidationError(
                {
                    'status' : False,
                    'message' : 'Sarlavha harflardan iborat bolihi kerak!'
                }
            )

        # checks if title and author does not exist on database
        if Book.objects.filter(title=title, author=author).exists():
            raise ValidationError(
                {
                    'status': False,
                    'message': 'Sarlavha va yozuvchi bir hil bolgan kitobni yuklay olmaysiz!'
                }
            )

        return data

    def validate_price(self, price):
        if price <= 0 or price >= 99999999999:
            raise ValidationError(
                {
                    'status': False,
                    'message': 'Narx notogri kiritilgan'
                }
            )