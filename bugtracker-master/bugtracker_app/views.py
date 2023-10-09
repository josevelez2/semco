from django.shortcuts import render, reverse, HttpResponseRedirect
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import get_object_or_404, redirect
from bugtracker_app.forms import LoginForm, TicketForm, EditTicketForm, SignupForm
from bugtracker_app.models import TicketModel, CustomUser


def tu_vista(request):
    # Obtiene la lista de usuarios
    all_users = User.objects.all()
    return render(request, 'ticket.html', {'all_users': all_users})

@login_required
def index(request):
    data = TicketModel.objects.all().order_by("-datetime")
    Total_count = TicketModel.objects.count()
    N_count = 0
    InP_count = 0
    D_count = 0
    InV_count = 0
    for ticket in data:
        if ticket.status == "InP":
            InP_count += 1
        if ticket.status == "D":
            D_count += 1
        if ticket.status == "InV":
            InV_count += 1
        if ticket.status == "N":
            N_count += 1
    return render(request, 'index.html', {"data": data,
                                         "Total_count": Total_count,
                                         "InP_count": InP_count,
                                         "N_count": N_count,
                                         "D_count": D_count,
                                         "InV_count": InV_count})
def bug_tracker_form(request):
    if request.method == "POST":
        form = BugTrackerForm(request.POST)
        if form.is_valid():
            # Guarda el formulario
            form.save()

        else:
            # Muestra el formulario con los errores
            return render(request, "bug_tracker_form.html", {"form": form})

    else:
        form = BugTrackerForm()

    return render(request, "bug_tracker_form.html", {"form": form})

@login_required
def assign_ticket_to_self(request, ticketid):
    # Obtener el ticket
    ticket = TicketModel.objects.get(id=ticketid)

    if request.method == "POST":
        # Obtener el ID del usuario seleccionado desde el formulario
        user_id = request.POST.get("user_id")

        try:
            # Obtener el usuario seleccionado
            assigned_user = User.objects.get(id=user_id)
            
            # Asignar el ticket al usuario seleccionado
            ticket.assignedto = assigned_user
            ticket.save()

            messages.success(request, f"Ticket asignado a {assigned_user.username} con éxito.")
            return HttpResponseRedirect(reverse('ticketinfo', args=(ticketid,)))

        except User.DoesNotExist:
            messages.error(request, "El usuario seleccionado no existe.")

    # Obtener la lista de usuarios disponibles para asignar
    available_users = User.objects.exclude(id=request.user.id)  # Excluir al usuario actual
    return render(request, 'assign_ticket_to_self.html', {'ticket': ticket, 'available_users': available_users})
def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(
                request,
                username=data['username'],
                password=data['password'],
            )
            if user:
                login(request, user)
                messages.success(request, "Inicio de sesión exitoso.")  # Mensaje de éxito
                return HttpResponseRedirect(reverse('home'))
            else:
                messages.error(request, "Usuario o contraseña incorrectos.")  # Mensaje de error
    else:
        form = LoginForm()
    
    return render(request, 'login.html', {"form": form})
@staff_member_required
def signup_view(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = CustomUser.objects.create_user(
                username=data['username'],
                password=data['password'],
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('login'))
    form = SignupForm()
    return render(request, 'signup.html', {"form": form})


def logout_view(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return HttpResponseRedirect(reverse('home'))


@login_required
def ticketinfo(request, ticketid):
    ticketinfo = TicketModel.objects.get(id=ticketid)
    return render(request, "ticket.html", {"ticketinfo": ticketinfo})


@login_required
def userinfo(request, filerid):
    filer = CustomUser.objects.get(id=filerid)
    filerhistory = TicketModel.objects.filter(ticketfiler=filer)
    assigned = filerhistory.filter(status="InP")
    completed = filerhistory.filter(status="D")
    reported = filerhistory.filter(status="N")
    return render(request, 'userinfo.html', {'filerhistory': filerhistory,
                  'filer': filer, 'assigned': assigned, 'completed': completed,
                                             'reported': reported})


@login_required
def createticket(request):
    if request.method == "POST":
        form = TicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            filer = request.user
            priority = data['priority']
            TicketModel.objects.create(
                title=data['title'],
                description=data['description'],
                ticketfiler=filer,
                priority=priority
            )
            return HttpResponseRedirect(reverse('home'))
    form = TicketForm()
    return render(request, 'form.html', {"form": form})

@login_required
def assignticket(request, userid, ticketid):
    user = CustomUser.objects.get(id=userid)
    data = TicketModel.objects.get(id=ticketid)
    data.status = "InP"
    data.assignedticket = user
    data.assignedto = request.user
    data.save()
    return HttpResponseRedirect(reverse('ticketinfo', args=(ticketid,)))


@login_required
def completedticket(request, userid, ticketid):
    user = CustomUser.objects.get(id=userid)
    data = TicketModel.objects.get(id=ticketid)
    data.status = "D"
    # data.doneticket = user
    data.completedby = request.user
    data.fue_completado = timezone.now()
    data.save()
    return HttpResponseRedirect(reverse('ticketinfo', args=(ticketid,)))
@login_required
def invalidticket(request, userid, ticketid):
    user = CustomUser.objects.get(id=userid)
    data = TicketModel.objects.get(id=ticketid)
    data.invalidticket = user
    data.status = "InV"
    data.save()
    return HttpResponseRedirect(reverse('ticketinfo', args=(ticketid,)))


@login_required
def editticket(request, ticketid):
    ticket = TicketModel.objects.get(id=ticketid)
    if request.method == "POST":
        form = EditTicketForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            ticket.title = data['title']
            ticket.description = data['description']
            ticket.save()
            return HttpResponseRedirect(reverse('ticketinfo', args=(ticketid,)))
    form = EditTicketForm(initial={
        'title': ticket.title,
        'description': ticket.description,
    })
    return render(request, 'form.html', {"form": form})


def home(request):
    # Tu lógica para la página de inicio aquí
    return render(request, 'index.html')

def compras(request):
    # Lógica para la página de compras
    return render(request, 'compras.html')

def direccion_tecnica(request):
    # Lógica para la página de dirección técnica
    return render(request, 'direccion_tecnica.html')

def noticias(request):
    # Lógica para la página de noticias
    return render(request, 'noticias.html')

def crear_app(request):
    # Lógica para la página de crear la app
    return render(request, 'crear_app.html')
