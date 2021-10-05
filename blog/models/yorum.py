from django.db import models

from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from blog.models import YazilarModel, yazi
from blog.abstract_models import DateAbstractModel

class YorumModel(DateAbstractModel):
    yazan = models.ForeignKey('account.CustomUserModel',on_delete=models.CASCADE, related_name='yorum')
    yazi = models.ForeignKey(YazilarModel, on_delete=models.CASCADE, related_name='yorumlar')
    yorum = models.TextField()
    

    class Meta:
        verbose_name = 'yorum'
        verbose_name_plural ='Yorum'
        db_table= 'Yorumlar'

        
    def __str__(self):
        return self.yazan.username