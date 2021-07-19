from django import forms
from .models import UserProfile


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('default_phone_number', 'default_postcode', 
                  'default_town_or_city', 'default_street_address1', 
                  'default_street_address2','default_county',
                  'default_country', 'profile_photo', 'profile_photo_url',)

        labels = {
                'default_phone_number': 'Phone Number',
                'default_postcode': 'Postal Code',
                'default_town_or_city': 'Town or City',
                'default_street_address1': 'Street Address 1',
                'default_street_address2': 'Street Address 2',
                'default_county': 'County, State or Locality',
                'default_country': 'Country',
                'profile_photo': 'Profile Photo',
                'profile_photo_URL': 'Profile Photo URL',
            }
    