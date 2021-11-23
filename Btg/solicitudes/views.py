from django.shortcuts import render, redirect
from .models import Usuario, Peticion, Queja, ReclamoP, ReclamoQ
from datetime import datetime
from django.contrib import messages

# Create your views here.

def home(request):
    return render(request, "gestionPQR.html")


def gestion_peticiones(request): 
    peticiones = Peticion.objects.all()
    return render(request, "gestionPeticiones.html", {"peticiones": peticiones})


def gestion_quejas(request):
    quejas = Queja.objects.all()
    return render(request, "gestionQuejas.html", {"quejas": quejas})


def crear_peticion(request):
    return render(request, "crearPeticion.html")


def crear_queja(request):
    return render(request, "crearQueja.html")


def registrar_peticion(request):
    id_usuario = 1
    descripcion = request.POST['descripcion']
    fecha_creacion = datetime.today()
    respuesta_admin = False
    desc_respuesta = ""
    fecha_respuesta = "2000-01-01"
    usuario_agrado = False
    hay_reclamo = False
    reclamo = -1
    
    peticion = Peticion.objects.create(id_usuario=id_usuario, descripcion=descripcion, fecha_creacion=fecha_creacion, respuesta_admin=respuesta_admin, desc_respuesta=desc_respuesta, fecha_respuesta=fecha_respuesta, usuario_agrado=usuario_agrado, hay_reclamo=hay_reclamo, reclamo=reclamo)
    return redirect('/gestionPeticiones/')


def registrar_queja(request):
    id_usuario = 1
    descripcion = request.POST['descripcion']
    fecha_creacion = datetime.today()
    respuesta_admin = False
    desc_respuesta = ""
    fecha_respuesta = "2000-01-01"
    usuario_agrado = False
    hay_reclamo = False
    reclamo = -1
    
    queja = Queja.objects.create(id_usuario=id_usuario, descripcion=descripcion, fecha_creacion=fecha_creacion, respuesta_admin=respuesta_admin, desc_respuesta=desc_respuesta, fecha_respuesta=fecha_respuesta, usuario_agrado=usuario_agrado, hay_reclamo=hay_reclamo, reclamo=reclamo)
    return redirect('/gestionQuejas/')


def eliminar_peticion(request, num_radicado):
    peticion = Peticion.objects.get(num_radicado=num_radicado)
    peticion.delete()
    return redirect('/gestionPeticiones/')


def eliminar_queja(request, num_radicado):
    queja = Queja.objects.get(num_radicado=num_radicado)
    queja.delete()
    return redirect('/gestionQuejas/')


def agrado_usuarioP(request, num_radicado):
    peticion = Peticion.objects.get(num_radicado=num_radicado)
    if (peticion.respuesta_admin == False or peticion.hay_reclamo == True):
        messages.warning(request, "No puede realizar esta accion si no hay respuesta por parte del area administrativa o si ya realizaste un reclamo")
        return redirect('/gestionPeticiones/')
    
    else:
        peticion.usuario_agrado = True
        peticion.save()
        return redirect('/gestionPeticiones/')


def agrado_usuarioQ(request, num_radicado):
    queja = Queja.objects.get(num_radicado=num_radicado)
    if (queja.respuesta_admin == False or queja.hay_reclamo == True):
        messages.warning(request, "No puede realizar esta accion si no hay respuesta por parte del area administrativa o si ya realizaste un reclamo")
        return redirect('/gestionQuejas/')
    
    else:
        queja.usuario_agrado = True
        queja.save()
        return redirect('/gestionQuejas/')


def hacer_reclamo_p(request, num_radicado):
    peticion = Peticion.objects.get(num_radicado=num_radicado)
    day = abs((datetime.today().date() - peticion.fecha_creacion).days)
    respuesta = peticion.respuesta_admin
    agrado = peticion.usuario_agrado
    reclamo = peticion.hay_reclamo
    if(((day > 5) or (respuesta == True and agrado == False)) and reclamo == False ):
        return render(request, "crearReclamoP.html", {"peticion": peticion})
    
    else:
        messages.warning(request, "No se cumplen las condiciones para hacer un reclamo")
        return redirect('/gestionPeticiones/')


def hacer_reclamo_q(request, num_radicado):
    queja = Queja.objects.get(num_radicado=num_radicado)
    day = abs((datetime.today().date() - queja.fecha_creacion).days)
    respuesta = queja.respuesta_admin
    agrado = queja.usuario_agrado
    reclamo = queja.hay_reclamo
    if(((day > 5) or (respuesta == True and agrado == False)) and reclamo == False ):
        return render(request, "crearReclamoQ.html", {"queja": queja})
    
    else:
        messages.warning(request, "No se cumplen las condiciones para hacer un reclamo")
        return redirect('/gestionQuejas/')


def registrar_reclamo_p(request):
    num_peticion = request.POST['num_peticion']
    descripcion = request.POST['descripcion']
    fecha_creacion = datetime.today()
    reclamo = ReclamoP.objects.create(num_peticion=num_peticion, descripcion=descripcion, fecha_creacion=fecha_creacion)
    
    peticion = Peticion.objects.get(num_radicado=num_peticion)
    peticion.reclamo = reclamo.num_radicado
    peticion.hay_reclamo = True
    peticion.save()
    
    return redirect('/gestionPeticiones/')


def registrar_reclamo_q(request):
    num_queja = request.POST['num_queja']
    descripcion = request.POST['descripcion']
    fecha_creacion = datetime.today()
    reclamo = ReclamoQ.objects.create(num_queja=num_queja, descripcion=descripcion, fecha_creacion=fecha_creacion)
    
    queja = Queja.objects.get(num_radicado=num_queja)
    queja.reclamo = reclamo.num_radicado
    queja.hay_reclamo = True
    queja.save()
    
    return redirect('/gestionQuejas/')


def ver_peticion(request, num_radicado):
    peticion = Peticion.objects.get(num_radicado=num_radicado)
    reclamo = {"descripcion" :"", "fecha_creacion": ""}
    if(peticion.hay_reclamo == True):
        reclamo = ReclamoP.objects.get(num_radicado=peticion.reclamo)
    return render(request, "verPeticion.html", {"peticion": peticion, "reclamo": reclamo})


def ver_queja(request, num_radicado):
    queja = Queja.objects.get(num_radicado=num_radicado)
    reclamo = {"descripcion" :"", "fecha_creacion": ""}
    if(queja.hay_reclamo == True):
        reclamo = ReclamoQ.objects.get(num_radicado=queja.reclamo)
    return render(request, "verQueja.html", {"queja": queja, "reclamo": reclamo})

