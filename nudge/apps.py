from django.apps import AppConfig
from material.frontend.apps import ModuleMixin

class NudgeConfig(ModuleMixin, AppConfig):
    name = 'nudge'
    icon = '<i class="material-icons">settings_applications</i>'
