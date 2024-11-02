import uuid
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

class Category(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name

class Size(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name}"

class Color(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name}"

class Product(models.Model):
    STATUS_CHOICES = [
        ('in_stock', 'In Stock'),
        ('on_the_road', 'On the Road'),
        ('not_available', 'Not Available'),
    ]
    SEX_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
        ('unisex', 'Unisex'),
    ]
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=124)
    image = models.ImageField(upload_to="uploads/products/", max_length=255, blank=True, null=True)
    rating = models.IntegerField(
        validators=[
            MinValueValidator(0.0),
            MaxValueValidator(5.0)
        ],
        default=5
    )
    price = models.IntegerField()
    discount = models.IntegerField()
    description = models.TextField()
    colors = models.ManyToManyField(Color)
    sizes = models.ManyToManyField(Size)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    type_of_clothes = models.TextField(default="Unknown")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    availability_status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='in_stock',
    )
    sex = models.CharField(
        max_length=20,
        choices=SEX_CHOICES,
        default="Unisex"
    )
    
    def __str__(self) -> str:
        return f"{self.title}"
    
    def get_color_names(self):
        return [color.name for color in self.colors.all()]

    def get_size_names(self):
        return [size.name for size in self.sizes.all()]

    def get_category_name(self):
        return self.category.name