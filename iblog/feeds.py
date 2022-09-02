from django.contrib.syndication.views import Feed
from django.urls import reverse
from iblog.models import Post

class LatestEntriesFeed(Feed):
    title = "blog newest posts"
    link = "/rss/feed/"
    description = "best blog for ever"

    def items(self):
        return Post.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.text_content[:35]

    # item_link is only needed if NewsItem has no get_absolute_url method.
    # def item_link(self, item):
    #     return reverse('news-item', args=[item.pk])