from django.apps import AppConfig


class ForecastConfig(AppConfig):
    #Configuration class for the 'forecast' app within the Django project.
    #Attributes 
    #default_auto_field (str): Specifies the default primary key field type for models.
    #name (str): Defines the name of the application as 'forecast'.
    
    default_auto_field = 'django.db.models.BigAutoField' # Sets the default primary key field type to BigAutoField
    name = 'forecast' # Name of the app within the project, used for app registration
