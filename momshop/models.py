from django.db import models
from django.shortcuts import reverse


class Carousel(models.Model):

    name = models.CharField(max_length=100, default=' ', verbose_name='Название')
    image = models.ImageField(upload_to='carousel/', verbose_name='Изображение')

    class Meta:
        verbose_name = 'Баннер'
        verbose_name_plural = 'Баннеры'

    def __str__(self):
        return self.name

class Reviews(models.Model):
    image = models.ImageField(upload_to='reviews/', verbose_name='Отзыв')

    def __str__(self):
        return 'Отзыв №' + str(self.id)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'


class AboutUsDesc(models.Model):
    description = models.TextField(default='',
                                   verbose_name='Описание на странице "О нас"')

    class Meta:
        verbose_name = 'Описание на странице "О нас"'
        verbose_name_plural = 'Описание на странице "О нас"'


    def __str__(self):
        return 'описание на странице "О нас"'

class AboutUsGallery(models.Model):
    image = models.ImageField(upload_to='about_us', verbose_name='Фото галереи')
    description = models.CharField(max_length=500, verbose_name='Подпись к фото')

    class Meta:
        verbose_name_plural = 'Фотографии галереи'
        verbose_name = 'Фотография галереи'

    def __str__(self):
        return 'фотография ' + str(self.id)

class FAQ(models.Model):
    question = models.CharField(max_length=200, verbose_name='Вопрос', default='')
    answer = models.TextField(verbose_name='Ответ', default='')

    class Meta:
        verbose_name = 'Вопрос страницы "Инфо"'
        verbose_name_plural = 'Вопросы страницы "Инфо"'

    def __str__(self):
        return 'вопрос ' + str(self.id)


class Products(models.Model):
    # products model

    avalability_types = (
        ('a', 'В наличии'),
        ('o', 'Под заказ')
    )

    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(blank=True, null=True, verbose_name='Описание')
    category = models.ForeignKey('Category',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 verbose_name='Категория')
    image = models.ImageField(upload_to='products', verbose_name='Изображение')
    consist = models.CharField(max_length=200, verbose_name='Состав', default='')
    size = models.CharField(max_length=15, blank=True, verbose_name='Размер')
    availability = models.BooleanField(default=True, verbose_name='Доступен на сайте')
    avalability_type = models.CharField(max_length=10,
                                        choices=avalability_types,
                                        default='a',
                                        verbose_name='Наличие')
    prev_price = models.DecimalField(max_digits=7,
                                decimal_places=2,
                                null=True,
                                blank=True,
                                verbose_name='Цена без скидки(по желанию)')
    price = models.DecimalField(max_digits=7,
                                decimal_places=2,
                                default=None,
                                verbose_name='Цена')

    tags = models.ManyToManyField('Keywords', verbose_name='Ключевые слова')
    models_height = models.PositiveIntegerField(default=0, verbose_name='Рост модели')
    creation = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product-detail', args=[str(self.id)])


class Category(models.Model):

    name = models.CharField(max_length=50, verbose_name='Название')
    image = models.ImageField(upload_to='category', default='Категория', verbose_name='Изображение категории')
    description = models.TextField(verbose_name='Описание', default='')

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-view', args=[str(self.id)])


class Keywords(models.Model):

    name = models.CharField(max_length=50,
                            verbose_name='Название',
                            blank=True,)

    class Meta:
        verbose_name = 'Тэг'
        verbose_name_plural = 'Теги'

    def __str__(self):
        return self.name

class Order(models.Model):
    # order model
    name = models.CharField(max_length=350, default=None, verbose_name='Имя')
    phone_number = models.CharField(max_length=20, verbose_name='Номер телефона', default='')
    city = models.CharField(max_length=500, verbose_name='Город', default='')
    total = models.DecimalField(max_digits=7,
                                decimal_places=2,
                                default=None,
                                verbose_name='Итого')
    closed = models.BooleanField(default=False, verbose_name='Исполнен')
    creation_date = models.DateTimeField(auto_now=True, verbose_name='Дата создания')

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.name


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, default=None, blank=True)
    product = models.ForeignKey(Products, on_delete=models.DO_NOTHING,
                                   default=None, verbose_name='Товар')
    quantity = models.PositiveIntegerField(default=1, verbose_name='Количество')

