from django.db import models


class Path(models.Model):
    path = models.TextField()

    def __str__(self):
        return self.path

class Table(models.Model):
    name = models.CharField(max_length=64)
    width = models.IntegerField()
    number = models.IntegerField()

    def __str__(self):
        return self.name

    def get_path():
        path = Path.objects.all().first()
        if not path:
            print("No path found")
            path = None
        else:
            path = path.path
        return path

    def set_path(csv_path):
        path = Path.objects.all().first()
        if path:
            path.path = csv_path
        else:
            path = Path(path=csv_path)
        path.save()
        return path
