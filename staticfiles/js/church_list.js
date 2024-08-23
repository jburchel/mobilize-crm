{% extends 'core/base.html' %}
{% load static %}

{% block extra_css %}
<link rel="stylesheet" href="{% static 'css/church_list.css' %}">
{% endblock %}

{% block content %}
<div class="pipeline-container">
    <h1>Church Pipeline</h1>

    <a href="{% url 'contacts:add_church' %}" class="btn btn-primary">Add New Church</a>

    <div class="search-container">
        <input type="text" id="churchSearch" placeholder="Search churches..." class="form-control">
    </div>

    <div class="pipeline-summary">
        {% for stage, count in pipeline_summary %}
        <div class="summary-item {% if forloop.first %}total-item{% endif %}" title="{{ stage }}">
            <span class="summary-label">{{ stage|truncatechars:15 }}</span>
            <span class="summary-value">{{ count }}</span>
        </div>
        {% endfor %}
    </div>

    <div class="pipeline-grid">
        {% for stage, churches in pipeline_stages.items %}
        <div class="pipeline-stage" data-stage="{{ stage|lower|slugify }}">
            <div class="stage-header">
                <span class="collapse-arrow">▼</span>
                <h2>{{ stage }}</h2>
            </div>
            <div class="stage-content">
                {% for church in churches %}
                <div class="church-card" draggable="true" data-church-id="{{ church.id }}" data-name="{{ church.church_name }}">
                    <div class="church-info">
                        <h3><a href="{% url 'contacts:church_detail' church.id %}" class="church-name-link">{{ church.church_name }}</a></h3>
                        <p>{{ church.email }}</p>
                        <p>Last Contact: {{ church.date_modified|default:"N/A" }}</p>
                    </div>
                    {% if church.image %}
                    <div class="church-image">
                        <a href="{% url 'contacts:church_detail' church.id %}" class="church-image-link">
                            <img src="{{ church.image.url }}" alt="{{ church.church_name }}">
                        </a>
                    </div>
                    {% endif %}
                </div>
                {% empty %}
                <p class="empty-stage">No churches in this stage.</p>
                {% endfor %}
            </div>
        </div>
        {% endfor %}
    </div>
</div>
{% endblock %}

{% block extra_js %}
<script src="{% static 'js/church_list_search.js' %}"></script>
{% endblock %}