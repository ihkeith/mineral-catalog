from django.db import models

# Create your models here.
class Mineral(models.Model):
    name = models.CharField(max_length=255, blank=True)
    image_filename = models.CharField(max_length=255, blank=True)
    image_caption = models.CharField(max_length=255, blank=True)
    category = models.CharField(max_length=255, blank=True)
    formula = models.CharField(max_length=255, blank=True)
    strunz_classification = models.CharField(max_length=255, blank=True)
    color = models.CharField(max_length=255, blank=True)
    crystal_system = models.CharField(max_length=255, blank=True)
    unit_cell = models.CharField(max_length=255, blank=True)
    crystal_symmetry = models.CharField(max_length=255, blank=True)
    cleavage = models.CharField(max_length=255, blank=True)
    mohs_scale_hardness = models.CharField(max_length=255, blank=True)
    luster = models.CharField(max_length=255, blank=True)
    streak = models.CharField(max_length=255, blank=True)
    diaphaneity = models.CharField(max_length=255, blank=True)
    optical_properties = models.CharField(max_length=255, blank=True)
    refractive_index = models.CharField(max_length=255, blank=True)
    crystal_habit = models.CharField(max_length=255, blank=True)
    specific_gravity = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.name
    
    def attrs(self):
        return [
            (field.name.split('_'), field.value_to_string(self))
            for field in Mineral._meta.fields
            if field.name not in ['id', 'image_filename', 'image_caption', 'name']]
    # https://stackoverflow.com/questions/1172722/iterating-over-model-attributes-when-creating-a-template-in-django
    # [(field.name, field.value_to_string(self)) for field in Manors._meta.fields]
