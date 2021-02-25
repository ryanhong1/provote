from django.db import models
from  votes import models as votes_models
from django.utils import timezone

class Photo(models.Model):

    """ Photo Model Definition """

    caption = models.CharField(max_length=80)
    file = models.ImageField(upload_to="post_photos")
    post = models.ForeignKey("Post", related_name="photos", on_delete=models.CASCADE)

    def __str__(self):
        return self.caption


class Post(models.Model):
    "Post Model Definition"

    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField(default=timezone.now)
    video_url = models.URLField(blank=True)
    description = models.TextField(blank=True, null=True)
    vote = models.ForeignKey(votes_models.Question, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title