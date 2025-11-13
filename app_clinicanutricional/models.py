from django.db import models

# ==========================================
# MODELO: NUTRIÓLOGOS
# ==========================================
class Nutriologo(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    correo = models.EmailField(unique=True)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    experiencia = models.PositiveIntegerField(help_text="Años de experiencia")
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Nutriólogo"
        verbose_name_plural = "Nutriólogos"


# ==========================================
# MODELO: PACIENTES
# ==========================================
class Paciente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=10)
    fechnacimiento = models.DateField()
    correo = models.EmailField(unique=True)
    direccion = models.CharField(max_length=100)
    sexo = models.CharField(
        max_length=10,
        choices=[
            ('Femenino', 'Femenino'),
            ('Masculino', 'Masculino')
        ]
    )
    id_nut = models.ForeignKey(
        Nutriologo,
        on_delete=models.CASCADE,
        related_name='pacientes'
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

    class Meta:
        verbose_name = "Paciente"
        verbose_name_plural = "Pacientes"


# ==========================================
# MODELO: CITAS
# ==========================================
class Cita(models.Model):
    fecha = models.DateField()
    horario = models.TimeField()
    motivo = models.CharField(max_length=200)
    estado = models.CharField(
        max_length=50,
        choices=[
            ('pendiente', 'Pendiente'),
            ('confirmada', 'Confirmada'),
            ('cancelada', 'Cancelada'),
            ('finalizada', 'Finalizada'),
        ]
    )
    observaciones = models.TextField(blank=True, null=True)
    duracion = models.PositiveIntegerField(help_text="Duración en minutos")

    id_nut = models.ForeignKey(
        Nutriologo,
        on_delete=models.CASCADE,
        related_name='citas'
    )
    id_paciente = models.ForeignKey(
        Paciente,
        on_delete=models.CASCADE,
        related_name='citas'
    )

    def __str__(self):
        return f"Cita con {self.id_nut.nombre} y {self.id_nut.nombre} el {self.fecha} a las {self.horario}"

    class Meta:
        verbose_name = "Cita"
        verbose_name_plural = "Citas"

class Receta(models.Model):
    ingredientes = models.TextField()
    tipocomida = models.CharField(max_length=100)
    medicamentos = models.TextField(blank=True, null=True)
    duracion = models.CharField(max_length=100)
    alergias = models.TextField(blank=True, null=True)
    id_paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    id_nutriologo = models.ForeignKey(Nutriologo, on_delete=models.CASCADE)

    def __str__(self):
        return f"Receta de {self.id_paciente.nombre} ({self.tipocomida})"

    class Meta:
        verbose_name = "Receta"
        verbose_name_plural = "Recetas"


class HistorialMedico(models.Model):
    enfermedades = models.TextField()
    alergias = models.CharField(max_length=200, blank=True, null=True)
    diagnostico = models.TextField()
    peso = models.DecimalField(max_digits=5, decimal_places=2)
    id_paciente = models.ForeignKey('Paciente', on_delete=models.CASCADE)

    def __str__(self):
        return f"Historial de {self.id_paciente.nombre}"

