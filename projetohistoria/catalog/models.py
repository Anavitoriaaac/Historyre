from django.db import models
from django.contrib.auth.models import AbstractUser, Permission, Group

# parte onde eu criei meus modelos tudo de acordo com o meu diagrama
LISTA_CATEGORIAS = (
    ("historia01", "HISTORIA01"),
    ("historia02", "HISTORIA02"),
    ("historia03", "HISTORIA03"),
    ("OUTROS", "Outros"),)

class Trajetoria(models.Model):
    nome = models.CharField(max_length=100)
    imagem = models.ImageField( upload_to='trumb_trajetoria',null=True,blank=True)
    descricao = models.TextField(max_length=1000)
    categoria = models.CharField(max_length=15, choices=LISTA_CATEGORIAS)
    anoInicial = models.DateField(null=True,blank=True)
    codigoTrajetoria = models.CharField(max_length=100,primary_key=True)

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

   
class Usuario(AbstractUser):
  nome= models.CharField(max_length=200)
  email = models.EmailField()
  telefone = models.CharField(max_length=200)
  cpf= models.CharField(primary_key=True,max_length=100)
  password = models.CharField(max_length=128, default='0')
  username = models.CharField(max_length=128, default='0')
    

 
  groups = models.ManyToManyField(Group, related_name='usuarios')
  user_permissions = models.ManyToManyField(Permission, related_name='usuarios')

class Historico (models.Model):
  user= models.ForeignKey(Usuario,on_delete=models.CASCADE)
  etapa= models.ForeignKey(Etapa,on_delete=models.CASCADE)
  Id= models.CharField(max_length=20,primary_key=True)
