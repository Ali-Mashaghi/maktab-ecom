from django.db import models
from decimal import  Decimal
from django.core.validators import MaxValueValidator , MinValueValidator
# Create your models here.
class ProductStatusType(models.IntegerChoices):
    publish = 1 ,("فعال")
    draft = 2 ,("غیرفعال")



class ProductCategory(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode= True) # اگه فارسی بود بتونه اجرا کنه

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title

class ProductModel(models.Model):
    user = models.ForeignKey("accounts.User", on_delete= models.PROTECT ) #یوزر رو دیلیت کردم پروداکتاش بدون صاحب نمونه
    category = models.ManyToManyField(ProductCategory)
    title = models.CharField(max_length=255)
    slug = models.SlugField(allow_unicode= True)
    image = models.ImageField(default="/default/product-image-.png" , upload_to="product/img/")
    description = models.TextField(null=True,blank=True)
    brief_description = models.TextField(null=True,blank=True)

    stock = models.PositiveIntegerField(default= 0 )
    price = models.DecimalField(default=0,max_digits=10,decimal_places=0)
    discount_percent = models.IntegerField(default= 0 , validators= [MinValueValidator(0), MaxValueValidator(100)])
    status = models.IntegerField(choices=ProductStatusType.choices , default= ProductStatusType.draft.value)

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class meta:
        ordering =["-created_date"]
    def __str__(self):
        return self.title


    def get_show_price(self):
        discount_price = self.price * Decimal(self.discount_percent / 100)
        discounted_amount = self.price - discount_price
        return '{:,}'.format(round(discounted_amount)) 
    

    def get_show_raw_price(self):
        return '{:,}'.format(self.price)


    def is_discounted(self):
        self.discount_percent != 0 

class ProductImageModel(models.Model):
    product = models.ForeignKey("accounts.User" , on_delete=models.CASCADE)
    file = models.ImageField( upload_to="product/extra-img/")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)




































































