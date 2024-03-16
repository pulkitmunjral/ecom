from django.urls import get_resolver
from collections import defaultdict

def get_all_apis():
    # Get the URL resolver for the project
    resolver = get_resolver()

    # Initialize an empty set to store APIs
    apis = set()

    # Traverse through all URL patterns
    def traverse_urls(urls, prefix=''):
        for urlpattern in urls.url_patterns:
            if hasattr(urlpattern, 'url_patterns'):
                # If it's an included URL pattern, traverse recursively
                traverse_urls(urlpattern, prefix + urlpattern.pattern._route)
            else:
                # If it's an API endpoint, add it to the set
                apis.add(prefix + urlpattern.pattern._route)

    # Start traversing through URL patterns
    traverse_urls(resolver)

    return apis

# Retrieve set of all APIs
all_apis = get_all_apis()

# Print the set of all APIs
print(all_apis)
