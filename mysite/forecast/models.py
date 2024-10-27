from django.db import models

# Create your models here.
# This file is reserved for creating database models for the 'forecast' app.
# Models in Django act as the blueprint for your database tables, defining the structure and behavior of data.
# Each model represents a table in the database, and each attribute of the model corresponds to a column in that table.

# Example model:
# Uncomment and modify the following code if you need to create a model for storing data.

# class ForecastData(models.Model):
#     date = models.DateField()  # Date of the forecasted or historical data point
#     closing_price = models.FloatField()  # Stock closing price for the specific date
#     created_at = models.DateTimeField(auto_now_add=True)  # Timestamp for when the record was created

#     def __str__(self):
#         return f"Date: {self.date}, Closing Price: {self.closing_price}"

#     class Meta:
#         verbose_name = 'Forecast Data'
#         verbose_name_plural = 'Forecast Data'

# Note:
# - To use any models, define them in this file, then run the command 'python manage.py makemigrations' 
#   to create migration files for the database.
# - Follow up with 'python manage.py migrate' to apply the changes to the actual database.