import autocomplete_light
from cities_light.models import City, Country


autocomplete_light.register(
    City,
    search_fields=['search_names'],
    attrs={
        'placeholder': 'Enter city name',
        'data-autocomplete-minimum-characters': 1,
    },
    widget_attrs={
        'data-widget-maximum-values': 4,
    },
)


autocomplete_light.register(
    Country,
    search_fields=['name', 'name_ascii'],
    attrs={
        'placeholder': 'Enter country name',
        'data-autocomplete-minimum-characters': 1,
    },
    widget_attrs={
        'data-widget-maximum-values': 4,
    },
)