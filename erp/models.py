from django.db import models




class Employees(models.Model):
    full_name = models.CharField(max_length=255)
    phone = models.CharField(max_length=20)
    email = models.EmailField()

    def __str__(self) -> str:
        return self.full_name


class Attendance(models.Model):
    employee = models.ForeignKey(Employees, on_delete=models.CASCADE)
    arrival_time = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.employee.full_name
