###
# Libs
###
from django import forms

from app.carwash.models.vehicle_license_plate import VehicleLicensePlate


###
# Admin Form
###


class VehicleLicensePlateForm(forms.ModelForm):
    class Meta:
        model = VehicleLicensePlate
        fields = '__all__'

    def clean_number(self):
        number = self.cleaned_data['number'].upper()
        return number
