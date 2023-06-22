from django.db import models


class Test(models.Model):
    FIO = models.CharField(max_length=30, verbose_name="фио",
                           help_text="ваша фамилия", null=True)
    resultat = models.CharField(
        max_length=15, null=True, verbose_name="Результат", help_text="ваш результат на ковид")
    data_sdachi = models.DateField(
        verbose_name="Дата сдачи", help_text="дата вашего теста", null=True)
    IO = models.CharField(max_length=30, null=True,
                          verbose_name="номер и серия паспорта", help_text="паспортные данные")

    def __str__(self):
        return f'{self.pk} - {self.FIO}'
