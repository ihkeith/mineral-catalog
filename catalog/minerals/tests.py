from django.test import TestCase
from django.urls import reverse

from .models import Mineral

# Create your tests here.
class MineralViewsTest(TestCase):
    def setUp(self):
        self.mineral = Mineral.objects.create(
            name = "Ianite",
            image_filename = "crying_stone.gif",
            image_caption = 'Cry cry cry',
            category = 'blah',
            formula = 'blah',
            strunz_classification = 'blah',
            color = 'blah',
            crystal_system = 'blah',
            unit_cell = 'blah',
            crystal_symmetry = 'blah',
            cleavage = 'blah',
            mohs_scale_hardness = 'blah',
            luster = 'blah',
            streak = 'blah',
            diaphaneity = 'blah',
            optical_properties = 'blah',
            refractive_index = 'blah',
            crystal_habit = 'blah',
            specific_gravity = 'blah',
        )

    def test_mineral_list_view(self):
        resp = self.client.get(reverse('minerals:list'))
        self.assertEqual(resp.status_code, 200)
        self.assertIn(self.mineral, resp.context['minerals'])
        self.assertTemplateUsed(resp, 'minerals/mineral_list.html')
        self.assertContains(resp, self.mineral.name)

    def test_mineral_detail_view(self):
        resp = self.client.get(reverse('minerals:detail', kwargs={
            'pk': self.mineral.pk,
        }))
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(self.mineral, resp.context['mineral'])
        self.assertTemplateUsed(resp, 'minerals/mineral_detail.html')
        self.assertContains(resp, self.mineral.name)
