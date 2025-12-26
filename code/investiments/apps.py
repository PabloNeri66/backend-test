from django.apps import AppConfig


class InvestimentsConfig(AppConfig):
    name = 'investiments'

    def ready(self):
        import investiments.signals