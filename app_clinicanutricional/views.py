from django.shortcuts import render, redirect, get_object_or_404
from .models import Nutriologo, Paciente, Cita

# Página de inicio
def inicio_clinicanutricional(request):
    return render(request, 'inicio.html')

# --------------------------
# CRUD NUTRIÓLOGOS
# --------------------------
def agregar_nutriologo(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion')
        telefono = request.POST.get('telefono')
        experiencia = request.POST.get('experiencia')
        especialidad = request.POST.get('especialidad')

        Nutriologo.objects.create(
            nombre=nombre,
            apellido=apellido,
            correo=correo,
            direccion=direccion,
            telefono=telefono,
            experiencia=experiencia,
            especialidad=especialidad
        )
        return redirect('ver_nutriologos')

    return render(request, 'nutriologos/agregar_nutriologo.html')


def ver_nutriologos(request):
    nutris = Nutriologo.objects.all()
    return render(request, 'nutriologos/ver_nutriologos.html', {'nutris': nutris})


def actualizar_nutriologo(request, id):
    nutri = get_object_or_404(Nutriologo, pk=id)
    return render(request, 'nutriologos/actualizar_nutriologo.html', {'nutri': nutri})


def realizar_actualizacion_nutriologo(request, id):
    nutri = get_object_or_404(Nutriologo, pk=id)
    if request.method == 'POST':
        nutri.nombre = request.POST.get('nombre')
        nutri.apellido = request.POST.get('apellido')
        nutri.correo = request.POST.get('correo')
        nutri.direccion = request.POST.get('direccion')
        nutri.telefono = request.POST.get('telefono')
        nutri.experiencia = request.POST.get('experiencia')
        nutri.especialidad = request.POST.get('especialidad')
        nutri.save()
        return redirect('ver_nutriologos')
    return redirect('ver_nutriologos')


def borrar_nutriologo(request, id):
    nutri = get_object_or_404(Nutriologo, pk=id)
    if request.method == 'POST':
        nutri.delete()
        return redirect('ver_nutriologos')
    return render(request, 'nutriologos/borrar_nutriologo.html', {'nutri': nutri})

# --------------------------
# CRUD PACIENTES
# --------------------------
def agregar_paciente(request):
    nutriologos = Nutriologo.objects.all()
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        apellido = request.POST.get('apellido')
        telefono = request.POST.get('telefono')
        fechnacimiento = request.POST.get('fechnacimiento')
        correo = request.POST.get('correo')
        direccion = request.POST.get('direccion')
        sexo = request.POST.get('sexo')
        id_nut = request.POST.get('id_nut') or None

        Paciente.objects.create(
            nombre=nombre,
            apellido=apellido,
            telefono=telefono,
            fechnacimiento=fechnacimiento,
            correo=correo,
            direccion=direccion,
            sexo=sexo,
            id_nut_id=id_nut if id_nut else None
        )
        return redirect('ver_pacientes')

    return render(request, 'pacientes/agregar_pacientes.html', {'nutriologos': nutriologos})


def ver_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'pacientes/ver_pacientes.html', {'pacientes': pacientes})


def actualizar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    nutriologos = Nutriologo.objects.all()
    return render(request, 'pacientes/actualizar_pacientes.html', {'paciente': paciente, 'nutriologos': nutriologos})


def realizar_actualizacion_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        paciente.nombre = request.POST.get('nombre')
        paciente.apellido = request.POST.get('apellido')
        paciente.telefono = request.POST.get('telefono')
        paciente.fechnacimiento = request.POST.get('fechnacimiento')
        paciente.correo = request.POST.get('correo')
        paciente.direccion = request.POST.get('direccion')
        paciente.sexo = request.POST.get('sexo')
        id_nut = request.POST.get('id_nut') or None
        paciente.id_nut_id = id_nut if id_nut else None
        paciente.save()
        return redirect('ver_pacientes')
    return redirect('ver_pacientes')


def borrar_paciente(request, id):
    paciente = get_object_or_404(Paciente, id=id)
    if request.method == 'POST':
        paciente.delete()
        return redirect('ver_pacientes')
    return render(request, 'pacientes/borrar_pacientes.html', {'paciente': paciente})

# --------------------------
# CRUD CITAS
# --------------------------
def agregar_cita(request):
    pacientes = Paciente.objects.all()
    nutriologos = Nutriologo.objects.all()

    if request.method == 'POST':
        fecha = request.POST['fecha']
        horario = request.POST['horario']
        motivo = request.POST['motivo']
        estado = request.POST['estado']
        duracion = request.POST['duracion']
        observaciones = request.POST.get('observaciones', '')
        id_paciente = request.POST['id_paciente']
        id_nut = request.POST['id_nut']

        Cita.objects.create(
            fecha=fecha,
            horario=horario,
            motivo=motivo,
            estado=estado,
            duracion=duracion,
            observaciones=observaciones,
            id_paciente_id=id_paciente,
            id_nut_id=id_nut
        )

        return redirect('ver_citas')

    return render(request, 'citas/agregar_citas.html', {  # 👈 aquí va tu archivo HTML correcto
        'pacientes': pacientes,
        'nutriologos': nutriologos
    })

def ver_citas(request):
    citas = Cita.objects.select_related('id_paciente', 'id_nut').all()
    return render(request, 'citas/ver_citas.html', {'citas': citas})


def actualizar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    pacientes = Paciente.objects.all()
    nutriologos = Nutriologo.objects.all()
    return render(request, 'citas/actualizar_citas.html', {'cita': cita, 'pacientes': pacientes, 'nutriologos': nutriologos})


def realizar_actualizacion_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    if request.method == 'POST':
        # Campos simples
        cita.fecha = request.POST.get('fecha', cita.fecha)
        cita.horario = request.POST.get('horario', cita.horario)
        cita.motivo = request.POST.get('motivo', cita.motivo)
        cita.estado = request.POST.get('estado', cita.estado)
        cita.observaciones = request.POST.get('observaciones', cita.observaciones)
        # Duración (asegurar int)
        dur = request.POST.get('duracion')
        try:
            cita.duracion = int(dur) if dur not in (None, '') else cita.duracion
        except ValueError:
            # si no es número, mantener la duración actual
            pass

        # Paciente: si viene en POST lo asignamos, si no, mantenemos el actual
        id_paciente_post = request.POST.get('id_paciente')
        if id_paciente_post:
            cita.id_paciente_id = id_paciente_post  # asigna FK por id
        # Nutriólogo: idem — SIEMPRE asegurarnos que no quede NULL
        id_nut_post = request.POST.get('id_nut')
        if id_nut_post:
            cita.id_nut_id = id_nut_post

        # Guardar cambios
        cita.save()
        return redirect('ver_citas')

    return redirect('ver_citas')


def borrar_cita(request, id):
    cita = get_object_or_404(Cita, id=id)
    if request.method == 'POST':
        cita.delete()
        return redirect('ver_citas')
    return render(request, 'citas/borrar_citas.html', {'cita': cita})
