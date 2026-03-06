from django.db import models


class Brand(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['name']
        verbose_name = 'Marca'
        verbose_name_plural = 'Marcas'

    def __str__(self):
        return self.name


class Car(models.Model):
    # Anúncio
    title = models.CharField(max_length=200, blank=True)
    subtitle = models.CharField(max_length=300, blank=True)
    description = models.TextField(blank=True)

    # Identificação
    brand = models.ForeignKey('Brand', on_delete=models.PROTECT, blank=True, null=True, related_name='cars')
    model = models.CharField(max_length=100, blank=True)
    version = models.CharField(max_length=100, blank=True)
    year = models.PositiveIntegerField(blank=True, null=True)
    color = models.CharField(max_length=50, blank=True)
    plate = models.CharField(max_length=10, unique=True, blank=True, null=True)

    # Especificações técnicas
    FUEL_CHOICES = [
        ('gasoline', 'Gasolina'),
        ('ethanol', 'Etanol'),
        ('flex', 'Flex'),
        ('diesel', 'Diesel'),
        ('electric', 'Elétrico'),
        ('hybrid', 'Híbrido'),
    ]
    fuel = models.CharField(max_length=20, choices=FUEL_CHOICES, blank=True)

    TRANSMISSION_CHOICES = [
        ('manual', 'Manual'),
        ('automatic', 'Automático'),
        ('cvt', 'CVT'),
        ('semi_automatic', 'Semi-automático'),
    ]
    transmission = models.CharField(max_length=20, choices=TRANSMISSION_CHOICES, blank=True)

    BODY_CHOICES = [
        ('sedan', 'Sedan'),
        ('hatch', 'Hatch'),
        ('suv', 'SUV'),
        ('pickup', 'Picape'),
        ('coupe', 'Cupê'),
        ('convertible', 'Conversível'),
        ('wagon', 'Station Wagon'),
        ('van', 'Van'),
    ]
    body_type = models.CharField(max_length=20, choices=BODY_CHOICES, blank=True)

    engine = models.CharField(max_length=50, blank=True)
    horsepower = models.PositiveIntegerField(blank=True, null=True)
    mileage = models.PositiveIntegerField(blank=True, null=True)
    doors = models.PositiveSmallIntegerField(blank=True, null=True)

    # Preço
    price = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    is_negotiable = models.BooleanField(default=False)

    # Status do anúncio
    STATUS_CHOICES = [
        ('available', 'Disponível'),
        ('sold', 'Vendido'),
        ('reserved', 'Reservado'),
        ('inactive', 'Inativo'),
    ]
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='available')
    is_featured = models.BooleanField(default=False)

    # Mídia
    thumbnail = models.ImageField(upload_to='cars/thumbnails/', blank=True, null=True)

    # Log
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Carro'
        verbose_name_plural = 'Carros'

    def __str__(self):
        return f'{self.brand} {self.model} {self.year} - {self.title}'


class CarImage(models.Model):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='cars/images/')
    order = models.PositiveSmallIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['order']
        verbose_name = 'Foto'
        verbose_name_plural = 'Fotos'

    def __str__(self):
        return f'Foto {self.order} - {self.car}'
