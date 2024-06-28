from django.db import models
from datetime import datetime
# Create your models here.


class Data(models.Model):
    """Model definition for Data."""

    class SuratKeteranganTidakMampu(models.IntegerChoices):
        K1 = 1, "Tidak Ada"
        K2 = 2, "Ada"

    class KondisiRumah(models.IntegerChoices):
        KR1 = 1, "Batu Bata Lantai Keramik"
        KR2 = 2, "Batu Bata Lantai Semen"

    class KeaktifanEkstrakurikuler(models.IntegerChoices):
        P1 = 1, "Tidak Aktif"
        P2 = 2, "Jarang"  # Nilai duplikat
        P3 = 3, "Aktif"

    class Penghasilan (models.IntegerChoices):
        PE1 = 1, "> 1.500.000"
        PE2 = 2, ">= 1.500.000 - <= 1.000.000"
        PE3 = 3, "<= 900.000 - >= 500.000"
        PE4 = 4, "Tidak Berpenghasilan"

    class Tanggungan (models.IntegerChoices):
        T1 = 1, "Satu"
        T2 = 2, "Dua"
        T3 = 3, "Tiga"
        T4 = 4, "Empat"

    class Keterangan (models.IntegerChoices):
        Y1 = 1, "Penghasilan OrangTua"
        Y2 = 2, "Yatim"

    nama = models.CharField(
        null=False,
        max_length=50,
        verbose_name="Nama",
    )
 
    surat_keterangan_tidak_mampu = models.IntegerField(
        choices=SuratKeteranganTidakMampu.choices,
        verbose_name="Surat Keterangan Tidak Mampu",
        default=SuratKeteranganTidakMampu.K1  #default value
    )
    kondisi_rumah = models.IntegerField(
        choices=KondisiRumah.choices,
        verbose_name="Kondisi Rumah",
    )
    keaktifan_ekstrakurikuler = models.IntegerField(
        choices=KeaktifanEkstrakurikuler.choices,
        verbose_name="Keaktifan Ekstrakurikuler",
        default=KeaktifanEkstrakurikuler.P1
    )
    penghasilan = models.IntegerField(
        choices=Penghasilan.choices,
        verbose_name="Penghasilan OrangTua",
    )
    tanggungan = models.IntegerField(
        choices=Tanggungan.choices,
        verbose_name="Tanggungan OrangTua",
    )
    keterangan = models.IntegerField(
        choices=Keterangan.choices,
        verbose_name="Keterangan",
    )
    tahun = models.IntegerField(
        verbose_name="Tahun",
        help_text="Tahun data diinput",
        default=datetime.now().year
    )

    class Meta:
        """Meta definition for Data."""

        verbose_name = "Data"
        verbose_name_plural = "Data"

    # def __str__(self):
    #     return self.nama
    def __str__(self):
        return f"{self.nama} -  {self.tahun}" 
