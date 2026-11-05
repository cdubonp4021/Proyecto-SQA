from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.shortcuts import render

from owners.models import Owner
from maintenance.models import MaintenanceSchedule
from reminders.models import Reminder
from service_orders.models import ServiceOrder
from vehicles.models import Vehicle


@login_required
def home(request):
    order_metrics = ServiceOrder.objects.aggregate(
        received=Count("id", filter=Q(estado=ServiceOrder.Status.RECIBIDO)),
        in_progress=Count(
            "id",
            filter=Q(estado=ServiceOrder.Status.EN_PROCESO),
        ),
        stopped=Count(
            "id",
            filter=Q(estado=ServiceOrder.Status.DETENIDO_REPUESTOS),
        ),
        finished=Count(
            "id",
            filter=Q(estado=ServiceOrder.Status.TERMINADO),
        ),
    )

    schedules = list(
        MaintenanceSchedule.objects.filter(activo=True).select_related(
            "vehicle",
            "vehicle__owner",
        )
    )

    status_priority = {
        MaintenanceSchedule.MaintenanceStatus.VENCIDO: 0,
        MaintenanceSchedule.MaintenanceStatus.PROXIMO: 1,
        MaintenanceSchedule.MaintenanceStatus.AL_DIA: 2,
    }

    for schedule in schedules:
        schedule.calculated_status = schedule.get_status()

    maintenance_metrics = dict.fromkeys(
        (status for status, _label in MaintenanceSchedule.MaintenanceStatus.choices),
        0,
    )
    for schedule in schedules:
        maintenance_metrics[schedule.calculated_status] += 1

    schedules = [
        schedule
        for schedule in schedules
        if schedule.calculated_status
        in {
            MaintenanceSchedule.MaintenanceStatus.VENCIDO,
            MaintenanceSchedule.MaintenanceStatus.PROXIMO,
        }
    ]

    schedules.sort(
        key=lambda item: status_priority[item.calculated_status]
    )

    context = {
        "total_owners": Owner.objects.count(),
        "total_vehicles": Vehicle.objects.count(),
        "order_metrics": order_metrics,
        "overdue_maintenance": sum(
            schedule.calculated_status
            == MaintenanceSchedule.MaintenanceStatus.VENCIDO
            for schedule in schedules
        ),
        "upcoming_maintenance": sum(
            schedule.calculated_status
            == MaintenanceSchedule.MaintenanceStatus.PROXIMO
            for schedule in schedules
        ),
        "priority_maintenance": schedules[:5],
        "pending_reminders": Reminder.objects.filter(
            estado=Reminder.Status.PENDIENTE
        ).count(),
        "order_chart_data": {
            "labels": [
                "Recibidas",
                "En proceso",
                "Detenidas por repuestos",
                "Terminadas",
            ],
            "values": [
                order_metrics["received"],
                order_metrics["in_progress"],
                order_metrics["stopped"],
                order_metrics["finished"],
            ],
            "colors": ["#d58a32", "#398b83", "#bd6247", "#4f9063"],
        },
        "order_chart_total": sum(order_metrics.values()),
        "maintenance_chart_data": {
            "labels": ["Vencidos", "Próximos", "Al día"],
            "values": [
                maintenance_metrics[MaintenanceSchedule.MaintenanceStatus.VENCIDO],
                maintenance_metrics[MaintenanceSchedule.MaintenanceStatus.PROXIMO],
                maintenance_metrics[MaintenanceSchedule.MaintenanceStatus.AL_DIA],
            ],
            "colors": ["#bd5649", "#d58a32", "#4f9063"],
        },
        "maintenance_chart_total": sum(maintenance_metrics.values()),
    }

    return render(request, "home.html", context)