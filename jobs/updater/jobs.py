import os
import subprocess

def run_all_scrapers():
    """
    Function to execute the run_scrapers management command using subprocess.
    This ensures that the scraping job is safely executed inside the Django context.
    """
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    manage_py = os.path.join(base_dir, 'manage.py')
    
    print("APScheduler starting automated job scraping run...")
    try:
        subprocess.run(['python', manage_py, 'run_scrapers'], check=True, cwd=base_dir)
        print("Automated job scraping successful.")
    except subprocess.CalledProcessError as e:
        print(f"Automated job scraping failed: {e}")
