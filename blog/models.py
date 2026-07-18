from django.db import models
from django.utils import timezone


class Article(models.Model):
    title = models.CharField(max_length=300)
    author = models.CharField(max_length=120, default='Admin')
    summary = models.TextField(blank=True, help_text='Short intro shown in the listing.')
    cover_image = models.ImageField(upload_to='covers/', blank=True, null=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)

    class Meta:
        ordering = ['-created_at']

    def __str__(self):
        return self.title

    @property
    def is_newest(self):
        if not self.id:
            return False
        return not Article.objects.filter(
            is_published=True, created_at__gt=self.created_at
        ).exists()


class Paragraph(models.Model):
    article = models.ForeignKey(Article, related_name='paragraphs', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    text = models.TextField()
    image = models.ImageField(upload_to='paragraphs/', blank=True, null=True)
    image_caption = models.CharField(max_length=240, blank=True)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.article.title} - paragraph {self.order}'


class MediaAttachment(models.Model):
    VIDEO = 'video'
    AUDIO = 'audio'
    FILE = 'file'
    MEDIA_TYPES = [
        (VIDEO, 'Video'),
        (AUDIO, 'Audio (MP3)'),
        (FILE, 'Other file'),
    ]

    article = models.ForeignKey(Article, related_name='media', on_delete=models.CASCADE)
    file = models.FileField(upload_to='media/')
    media_type = models.CharField(max_length=10, choices=MEDIA_TYPES, default=FILE)
    caption = models.CharField(max_length=240, blank=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return f'{self.get_media_type_display()} for {self.article.title}'
