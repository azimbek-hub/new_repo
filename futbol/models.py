from django.db import models


Product_Type = (
    ('DONA', 'donali'),
    ('LITR', 'litr'),
    ('KG', 'kg')
)


class User(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField()
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.full_name


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    product_type = models.CharField(max_length=100, choices=Product_Type, default="DONA")
    image = models.ImageField(upload_to="products/", null=True, blank=True)

    # ✅ FIXED (loop bermaydi)
    shelf_life = models.CharField(max_length=100, default="unknown")

    description = models.TextField(null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, blank=True)
    discount = models.IntegerField(null=True, blank=True)
    tags = models.ManyToManyField(Tag, blank=True)

    def __str__(self):
        return self.name


class Order(models.Model):
    order_number = models.CharField(max_length=100)

    # ✅ FIXED (loop bermaydi)
    qty_products = models.IntegerField(default=0)
    qty_items = models.IntegerField(default=0)

    amount = models.IntegerField(default=0)
    customer = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.order_number


class OrderItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)
    quantity = models.IntegerField(default=0)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)

    @property
    def total_price(self):
        if self.product:
            return self.quantity * self.product.price
        return 0


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    order = models.ForeignKey(Order, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.user.full_name if self.user else "No user"