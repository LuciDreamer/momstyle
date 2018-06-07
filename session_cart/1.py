{% extends 'base.html' %}
{% load staticfiles %}
{% block css %}
    <link rel="stylesheet" href="{% static 'css/category.css' %}">
{% endblock %}

{% block title %}
    <title>Каталог</title>
{% endblock %}

{% block content %}
    <div class="container products-container">
    <!-- products container -->

        <div class="row">
            <!-- navigation and products row -->

            <div class="col-sm-3 category-colomn">
            <!-- navigation colomn -->
                <ul class="list-group category-list">
                    <a class="category-link" href="{% url 'catalog' %}">
                        <li class="list-group-item">
                            <span class="category-name">все</span>
                        </li>
                    </a>
                    {% for category in categories %}
                        <a class="category-link" href="{{ category.get_absolute_url }}">
                            <li class="list-group-item">
                                <span class="category-name">{{ category.name }}</span>
                            </li>
                        </a>
                    {% endfor %}
                </ul>
            <!-- end navigation colomn -->
            </div>

            {% block products %}
                <div class="col-sm-9">
                <!-- products block -->
                    <div class="row">
                        {% for product in key_group %}
                            <div class="col-lg-3 col-md-4 col-sm-6">
                                <a class="product-link" href="{{ product.get_absolute_url }}">
                                    <div class="card product-cell">
                                        <img class="card-img" src="{{ product.image.url }}" alt="">
                                        <div class="card-caption products-card-caption">
                                            <span class="product-name">{{ product.title }}</span><br>
                                            <span class="price">{{ product.price }}</span><br>
                                            <a href="#">в корзину</a>
                                        </div>
                                    </div>
                                </a>
                            </div>
                        {% endfor %}
                    </div>
                <!-- end products block -->
                </div>
            {% endblock %}

        <!-- end navigation and products row -->
        </div>

    <!-- end products container -->
    </div>
{% endblock %}