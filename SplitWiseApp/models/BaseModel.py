from django.db import models


class BaseModel(models.Model):
    id = models.AutoField(primary_key=True)
    date_created_at = models.DateTimeField(auto_now_add=True)
    date_updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True  # Make sure this line is present to declare it as an abstract model

# Your other models follow here...
