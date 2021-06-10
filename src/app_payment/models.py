from django.db import models
from django.conf import settings


class BillingAddress(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, )
    address = models.CharField(max_length=264, blank=True, )
    zipcode = models.CharField(max_length=10, blank=True, )
    city = models.CharField(max_length=50, blank=True, )
    country = models.CharField(max_length=55, blank=True, )

    def __str_(self):
        return f'{self.user.profile.username} billing address'

    def is_fully_filled(self):
        field_names = [f.name for f in self._meta.get_fields()]
        for filed_name in field_names:
            value = getattr(self, filed_name)
            if value is None or value == '':
                return False
        return True
    class Meta:
        verbose_name_plural = 'Billing Addresses'            