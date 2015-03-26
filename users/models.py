from django.db import models
from pygments.lexers import get_all_lexers
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])


class Article(models.Model):

    created = models.DateTimeField(auto_now_add=True)    
    title = models.CharField(max_length=25, default='')
    description = models.TextField(blank=True, default='')
    language = models.CharField(choices=LANGUAGE_CHOICES,
                                default='python',
                                max_length=100)
    owner = models.ForeignKey('auth.User', related_name='articles')
    highlighted = models.TextField()
    
    class Meta:
        ordering = ('created',)
        
    def save(self, *args, **kwargs):
        lexer = get_lexer_by_name(self.language)
        options = self.title and {'title': self.title} or {}
        formatter = HtmlFormatter(full=True, **options)
        self.highlighted = highlight(self.description, lexer, formatter)
        super(Article, self).save(*args, **kwargs)

    


