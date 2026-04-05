from django.contrib.sitemaps import Sitemap
from .models import Blog   # or your model

class BlogSitemap(Sitemap):
    changefreq = "daily"
    priority = 0.8

    def items(self):
        return Blog.objects.all()

    def lastmod(self, obj):
        return obj.updated_at