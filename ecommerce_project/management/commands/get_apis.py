# In core/management/commands/get_apis.py
from django.core.management.base import BaseCommand
from django.urls import get_resolver

class Command(BaseCommand):
    help = 'Prints all APIs exposed by Django REST Framework'

    def handle(self, *args, **options):
        resolver = get_resolver()
        apis = set()

        def traverse_urls(urls, prefix=''):
            for urlpattern in urls.url_patterns:
                if hasattr(urlpattern, 'url_patterns'):
                    traverse_urls(urlpattern, prefix + urlpattern.pattern._route)
                else:
                    apis.add(prefix + urlpattern.pattern._route)

        for app_name in resolver.namespace_dict.keys():
            app_resolver = resolver.namespace_dict[app_name]
            if not app_resolver:
                continue
            traverse_urls(app_resolver)

        self.stdout.write("\n".join(sorted(apis)))
