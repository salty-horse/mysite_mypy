from django.db import models

# Create your models here.
from djext.blame.models import BaseBlameModel

# Create your models here.

class BaseModel(models.Model):
    some_field = models.CharField()

    def foo(self) -> bool:
        return self.AAA.exists()
    def bar(self) -> bool:
        return self.BBB.exists()

class ForeignModel(BaseBlameModel):
    base_object = models.ForeignKey(BaseModel, related_name='AAA', on_delete=models.CASCADE)

class AbstractModel(models.Model):
    class Meta:
        abstract = True

class AnotherForeignModel(AbstractModel):
    base_object = models.ForeignKey(BaseModel, related_name='BBB', on_delete=models.CASCADE)
