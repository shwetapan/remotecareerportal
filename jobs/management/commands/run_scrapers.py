from django.core.management.base import BaseCommand
import subprocess
import os

class Command(BaseCommand):
    help = 'Runs all job scraping scripts'

    def handle(self, *args, **options):
        # List of all your scraper scripts
        scripts = [
            '11sigma.py',
            'anka.py',
            'argyle.py',
            'automattic.py',
            'theorem.py',
            'vodacom.py',
            'general_scraper.py'
        ]

        base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))

        for script in scripts:
            script_path = os.path.join(base_dir, script)
            if os.path.exists(script_path):
                self.stdout.write(self.style.SUCCESS(f'Running {script}...'))
                try:
                    # Run the script using the current python environment
                    # We pass the content directly to manage.py shell exactly how we did manually
                    command = f'python manage.py shell -c "exec(open(\'{script_path}\').read())"'
                    subprocess.run(command, shell=True, check=True, cwd=base_dir)
                    self.stdout.write(self.style.SUCCESS(f'Successfully ran {script}'))
                except subprocess.CalledProcessError as e:
                    self.stdout.write(self.style.ERROR(f'Error running {script}: {e}'))
            else:
                self.stdout.write(self.style.WARNING(f'Script not found: {script}'))

        self.stdout.write(self.style.SUCCESS('Finished running all scrapers!'))
