from django.db import models

# Create your models here.
LISTA_CATEGORIAS = (
    ("historia01", "HISTORIA01"),
    ("historia02", "HISTORIA02"),
    ("historia03", "HISTORIA03"),
    ("OUTROS", "Outros"),)
class Trajetoria(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField(null=True,blank=True)
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    anoInicial = models.DateField(null=True,blank=True)
    codigoTrajetoria = models.CharField(max_length=100,primary_key=True)
    #etapa= models.ForeignKey(Etapa, on_delete = models.CASCADE) #relação representada no diagrama(uma trajetoria é composta por varias etapas)
class Etapa(models.Model):
    numeração = models.IntegerField ()
    status= models.CharField(max_length=100)
    IdEtapa = models.CharField(max_length=100,primary_key=True)
    IdMaterial= models.ManyToManyField("Material")
    trajetoria= models.ForeignKey(Trajetoria,on_delete=models.CASCADE,null=True,blank=True)

    
class Material(models.Model):
    titulo= models.CharField(max_length=200)
    tipo = models.CharField(max_length=200,null=True,blank=True)
    assunto = models.CharField(max_length=200,null=True,blank=True)
    fontevideo = models.URLField(null=True,blank=True)
    fontepdf = models.URLField(null=True,blank=True)
    fontejogo = models.URLField(null=True,blank=True)
    fonteform = models.URLField(null=True,blank=True)
    idMaterial = models.CharField(max_length=100,primary_key=True)
    dataPublicação =models.DateField(null=True,blank=True)

   
class Usuario(models.Model):
  nome= models.CharField(max_length=200)
  email = models.EmailField()
  telefone = models.CharField(max_length=200)
  cpf= models.CharField(primary_key=True,max_length=100)

class Historico (models.Model):
  user= models.ForeignKey(Usuario,on_delete=models.CASCADE)
  etapa= models.ForeignKey(Etapa,on_delete=models.CASCADE)
  Id= models.CharField(max_length=20,primary_key=True)
