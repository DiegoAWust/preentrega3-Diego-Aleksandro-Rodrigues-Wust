from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.core.mail import send_mail

from carrito.carro import Carro
from pedidos.models import LineaPedido, Pedido


@login_required
def procesar_pedido(request):
    pedido=Pedido.objects.create(user=request.user)
    carro=Carro(request)
    lineas_pedido=list()
    for key, value in carro.carro.items():
        lineas_pedido.append(LineaPedido(
    producto_id=key,
    cantidad=value["cantidad"],
    user=request.user,
    pedido=pedido
    ))
    
    LineaPedido.objects.bulk_create(lineas_pedido)

    enviar_mail(
        pedido=pedido,
        lineas_pedido=lineas_pedido,
        nombre_usuario = request.user.username,
        email_usuario=request.user.email,
    )

    messages.success(request, "El pedido se ha hecho correctamente")

    return redirect("../productos")

def enviar_mail(**kwargs):

    asunto="Pedido de MagnusSRL"
    mensaje=render_to_string("emails/pedidos.html",{
            "pedido": kwargs.get("pedido"),
            "lineas_pedido": kwargs.get("lineas_pedido"),
            "nombre_usuario": kwargs.get("nombre_usuario")
    
    })

    mensaje_texto=strip_tags(mensaje)
    from_email="diegoarwust@gmail.com"
    to=kwargs.get("email_usuario")

    send_mail(asunto, mensaje_texto, from_email, [to], html_message=mensaje)