from django.db import models

class DataFile(models.Model):
    main_file = models.FileField(upload_to='data_files/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
    total_downloads = models.IntegerField(default=0)

    def __str__(self):
        return self.main_file.name

