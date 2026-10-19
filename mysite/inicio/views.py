from django.shortcuts import render


def inicio(request):
   contexto = {
    "titulo": "Software en la UNEMI",
    "mensaje": "estamos aprendiendo python y django en visual.",
}
   return render(request,  "inicio/inicio.html", contexto)