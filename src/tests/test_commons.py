import os
from django.test import LiveServerTestCase, Client
from django.conf import settings


class TestCommons(LiveServerTestCase):
    # check that browsable api renderer is not activated in REST_FRAMEWORK_SETTINGS.
    def test_renderer_settings(self):
        RENDERER_CLASSES = ('rest_framework.renderers.JSONRenderer',)
        self.assertTupleEqual(
                         settings.REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'],
                         RENDERER_CLASSES,
                         "Wrong configuration for DEFAULT RENDERER CLASSES")

    # testing if all the vars are correctly set up.
    def test_settings(self):
        self.assertTrue(os.path.exists(settings.STATIC_ROOT), "STATIC_ROOT directory is not set.")
        self.assertTrue(os.path.exists(settings.MEDIA_ROOT), "MEDIA_ROOT directory is not set.")
