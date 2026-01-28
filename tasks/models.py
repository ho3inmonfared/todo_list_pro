from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=40, unique=True)
    color = models.CharField(
        max_length=20,
        default='indigo'
    )

    def __str__(self):
        return self.title
    

class Task(models.Model):
    
    text=models.CharField(max_length=500)
    category=models.ForeignKey(Category,on_delete=models.CASCADE,related_name='tasks')
    is_complete=models.BooleanField(default=False)
    created_at=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.text
    
