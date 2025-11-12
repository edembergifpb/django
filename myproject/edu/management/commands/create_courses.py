from django.core.management.base import BaseCommand
from edu.models import Curso
from faker import Faker


class Command(BaseCommand):
    help = 'Comando para gerar vários registros de cursos'

    def add_arguments(self, parser):
        parser.add_argument('--count', type=int, default=50, help='Número de cursos a criar')

    def handle(self, *args, **options):
        count = options.get('count') or 50
        fake = Faker()

        created = 0
        for i in range(count):
            nome = fake.job()
            Curso.objects.create(nome=nome)
            created += 1

        self.stdout.write(self.style.SUCCESS(f'Criados {created} cursos.'))
