from django.contrib.auth import get_user_model
from django.test import TestCase

from maintenance.models import MaintenanceSchedule
from owners.models import Owner
from service_orders.models import ServiceOrder
from vehicles.models import Vehicle


class AuthenticationTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username="usuario_prueba",
            password="contrasena-segura",
        )

    def test_anonymous_user_is_redirected_from_home(self):
        response = self.client.get("/")

        self.assertRedirects(response, "/login/?next=/")

    def test_login_page_renders(self):
        response = self.client.get("/login/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Iniciar sesión")
        self.assertContains(response, 'autocomplete="username"')
        self.assertContains(response, 'autocomplete="current-password"')

    def test_login_preserves_requested_destination(self):
        response = self.client.get("/login/?next=/admin/")

        self.assertContains(response, 'name="next" value="/admin/"')

    def test_admin_login_redirects_to_public_login(self):
        response = self.client.get("/admin/login/?next=/admin/")

        self.assertRedirects(response, "/login/?next=%2Fadmin%2F")

    def test_authenticated_user_can_access_home(self):
        self.client.force_login(self.user)

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Dashboard")

    def test_valid_login_works(self):
        response = self.client.post(
            "/login/",
            {"username": "usuario_prueba", "password": "contrasena-segura"},
        )

        self.assertRedirects(response, "/")
        self.assertTrue(response.wsgi_request.user.is_authenticated)

    def test_logout_works(self):
        self.client.force_login(self.user)

        response = self.client.post("/logout/")

        self.assertRedirects(response, "/login/")
        home_response = self.client.get("/")
        self.assertRedirects(home_response, "/login/?next=/")


class DashboardChartTests(TestCase):
    def setUp(self):
        user = get_user_model().objects.create_user(
            username="dashboard_chart_user",
            password="contrasena-segura",
        )
        self.client.force_login(user)
        owner = Owner.objects.create(
            tipo=Owner.OwnerType.PERSONA,
            nombre="Propietario de prueba",
            telefono="3001234567",
        )
        self.vehicle = Vehicle.objects.create(
            owner=owner,
            tipo="AUTOMOVIL",
            marca="Toyota",
            modelo="Corolla",
            anio=2022,
            placa="DASH01",
            kilometraje_actual=5000,
            estado="ACTIVO",
            perfil_uso=Vehicle.UsageProfile.NORMAL,
        )

    def test_dashboard_chart_context_counts_orders_and_maintenance_states(self):
        ServiceOrder.objects.create(
            vehicle=self.vehicle,
            kilometraje_ingreso=self.vehicle.kilometraje_actual,
            motivo_ingreso="Revisión de prueba",
        )
        for name, interval, last_mileage in [
            ("Vencido", 500, 4000),
            ("Próximo", 1000, 4500),
            ("Al día", 3000, 3000),
        ]:
            MaintenanceSchedule.objects.create(
                vehicle=self.vehicle,
                nombre_servicio=name,
                intervalo_km=interval,
                ultimo_kilometraje=last_mileage,
            )

        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(
            response.context["order_chart_data"]["values"],
            [1, 0, 0, 0],
        )
        self.assertEqual(
            response.context["maintenance_chart_data"]["values"],
            [1, 1, 1],
        )
        self.assertContains(response, "orders-chart")
        self.assertContains(response, "maintenance-chart")