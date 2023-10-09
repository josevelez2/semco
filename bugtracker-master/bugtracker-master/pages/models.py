from django.db import models
from ckeditor.fields import RichTextField

class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name="Orden", default=0)
    created = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de creación")
    updated = models.DateTimeField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering = ['order', 'title']

    def __str__(self):
        return self.title



class Empleado(models.Model):
    primer_nombre = models.CharField(max_length=20) 
    segundo_nombre = models.CharField(max_length=20, blank=True, null=True)
    primer_apellido = models.CharField(max_length=30)
    segundo_apellido = models.CharField(max_length=30)
    cedula = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField()
    sexo = models.CharField(max_length=20, choices=[('masculino', 'Masculino'), ('femenino', 'Femenino'), ('otros', 'Otros')])
    estado_civil = models.CharField(max_length=20, choices=[('soltero', 'Soltero'), ('casado', 'Casado'), ('divorciado', 'Divorciado'), ('union_libre', 'Unión Libre')]) 
    numero_hijos = models.CharField(max_length=20, choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('0', 'Ninguno')])
    estudiante = models.BooleanField(default=False)
    estudios_terminados = models.CharField(max_length=20, choices=[('curso', 'Curso'), ('diplomado', 'Diplomado'), ('tecnica', 'Técnica'), ('tecnologia', 'Tecnología'), ('profesional', 'Profesional'), ('especializacion', 'Especialización'), ('maestria', 'Maestría')])
    eps = models.CharField(max_length=20, choices=[('aliansalud', '1. Aliansalud'), ('cafam', '2. Cafam EPS'), ('capital_salud', '3. Capital Salud EPS'), ('capresoca', '4. Capresoca'), ('colsubsidio', '5. Colsubsidio'), ('comfandi', '6. COMFANDI'), ('compensar', '7. Compensar'), ('coomeva', '8. Coomeva'), ('coosalud', '9. Coosalud'), ('sanitas', '10. EPS Sanitas'), ('sura', '11. EPS Sura'), ('famisanar', '12. Famisanar'), ('medimas', '13. Medimás'), ('mutual_ser', '14. Mutual SER'), ('nueva_eps', '15. Nueva EPS'), ('salud_total', '16. Salud Total'), ('savia_salud', '17. Savia Salud EPS'), ('sisben_IV', '18 SISBEN IV')])
    fondo_pension = models.CharField(max_length=100, choices=[('proteccion', 'Protección'), ('porvenir', 'Porvenir'), ('colfondos', 'Colfondos'), ('old_mutual', 'Old Mutual'), ('colpensiones', 'Colpensiones')])
    fondo_cesantias = models.CharField(max_length=100, choices=[('proteccion', 'Protección'), ('porvenir', 'Porvenir'), ('colfondos', 'Colfondos'), ('old_mutual', 'Old Mutual'), ('colpensiones', 'Colpensiones')])
    banco = models.CharField(max_length=100, choices=[('av_villas', 'AV Villas'), ('banco_de_bogota', 'Banco de Bogotá'), ('banco_de_occidente', 'Banco de Occidente'), ('banco_popular', 'Banco Popular'), ('porvenir', 'Porvenir'), ('bbva', 'BBVA'), ('bancolombia', 'Bancolombia'), ('davivienda', 'Davivienda'), ('banco_santander', 'Banco Santander'), ('banco_agrario', 'Banco Agrario'), ('banco_colpatria', 'Banco Colpatria'), ('credilinea', 'Credilinea')])
    tipo_cuenta = models.CharField(max_length=20, choices=[('ahorros', 'Ahorros'), ('corriente', 'Corriente')])
    numero_cuenta = models.CharField(max_length=100)
    archivo_certificado_bancario = models.FileField(upload_to='archivos_certificados/', blank=True)
    fecha_contratacion = models.DateField()
    
    tipo_contrato = models.CharField(max_length=20, choices=[('termino_fijo', 'Término Fijo'), ('termino_indefinido', 'Término Indefinido'), ('temporal', 'Temporal')])
    duracion_contrato = models.CharField(max_length=20,null=True, blank=True, choices=[('3_meses', '3 meses'),  ('6_meses', '6 meses'), ('1_anio', '1 año')])
    empresa_temporal = models.ManyToManyField('Empresas_Temporales', blank=True)
    correo_empresa = models.EmailField(max_length=100,null=True, blank=True)
    correo_personal = models.EmailField(max_length=100)
    salario_pesos = models.DecimalField(max_digits=10, decimal_places=2)
    persona_a_cargo = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='empleados_subordinados')  
       # ... (campos existentes)

    def __str__(self):
        return f"{self.primer_nombre} {self.primer_apellido} {self.segundo_apellido}"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # Crear registros para los hijos
        if self.numero_hijos != '0':
            num_hijos = int(self.numero_hijos)
            for i in range(1, num_hijos + 1):
                hijo = Hijo(empleado=self, nombre=f'Hijo {i}', fecha_nacimiento=self.fecha_nacimiento)
                hijo.save()
class Hijo(models.Model):
    empleado = models.ForeignKey(Empleado, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    fecha_nacimiento = models.DateField()

    def __str__(self):
        return f"{self.nombre} (Hijo de {self.empleado})"

    
class Empresas_Temporales(models.Model):
    nombre = models.CharField(max_length=100)
    direccion = models.CharField(max_length=20,blank=True, null=True )
    nombre_de_contacto = models.CharField(max_length=20,blank=True, null=True)
    numero_de_contacto = models.CharField(max_length=20,blank=True, null=True)

    def __str__(self):
        return self.nombre


from django.contrib import admin
from .models import Empleado 


