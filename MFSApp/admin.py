from django.contrib import admin
from django.apps import apps

models_to_register = apps.get_models()
for model in models_to_register:
    try:
        admin.site.register(model)
    except Exception as e:
        print("Failed to Register ", model, e)
# Register your models here.
