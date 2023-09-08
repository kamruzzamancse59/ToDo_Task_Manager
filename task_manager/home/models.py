from django.db import models

# Create your models here.
class Task(models.Model):
        id=models.AutoField(primary_key=True)
        taskTitle = models.CharField(max_length=30)
        taskDesc = models.TextField()
        date_field= models.DateField()
        time = models.DateField(auto_now_add=True)
        PENDING="Pending"
        COMPLETED="Completed"
        PROGRESS="Progress"
        STATUS=[
                (PENDING,'Pending'), (COMPLETED,'Completed'), (PROGRESS,'Progress')
                
        ]
      
        status=models.CharField(max_length=200, choices=STATUS, default=PENDING)

        def __str__(self):
                return self.taskTitle
                