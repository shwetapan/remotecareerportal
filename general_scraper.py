import os
import requests
import feedparser
from bs4 import BeautifulSoup
from datetime import date
import uuid

def fetch_rss_jobs():
    """
    Scrapes the public RSS feed from WeWorkRemotely.
    This is completely legal/free, easy to parse, and rich in remote tech jobs.
    """
    
    rss_urls = [
        "https://weworkremotely.com/categories/remote-programming-jobs.rss",
        "https://weworkremotely.com/categories/remote-design-jobs.rss",
        "https://weworkremotely.com/categories/remote-customer-support-jobs.rss",
        "https://remoteok.com/rss"
    ]
    
    # We load models dynamically to ensure the django context allows this Script to run
    from jobs.models import Jobs, Company, Category
    from django.utils import timezone
    from django.template.defaultfilters import slugify
    
    try:
        # Fetching directly from Remotive API first to get real company logos!
        remotive_url = "https://remotive.com/api/remote-jobs?limit=250"
        print(f"[{timezone.now()}] Fetching real logo jobs from {remotive_url}...")
        response = requests.get(remotive_url).json()
        
        added_count = 0
        for job_data in response.get('jobs', []):
            company_name = job_data.get('company_name', 'Remote Company')
            job_title = job_data.get('title', '')
            link = job_data.get('url', '')
            real_logo_url = job_data.get('company_logo_url') or job_data.get('company_logo')
            location = job_data.get('candidate_required_location', '')
            
            # Fetch or create the specific company dynamically
            company_slug = slugify(company_name)[:50]
            unique_company_id = f"remotive_{company_slug}"
            
            the_company, created = Company.objects.get_or_create(
                title=company_name,
                defaults={'uniqueId': unique_company_id, 'description': f'Jobs at {company_name}'}
            )
            
            # If newly created and we have a REAL logo
            if created and real_logo_url:
                the_company.companyLogoUrl = real_logo_url
                the_company.save()
                    
            # Basic category routing
            the_category, _ = Category.objects.get_or_create(title='Developer')
            if 'engineer' in job_title.lower() or 'developer' in job_title.lower():
                the_category, _ = Category.objects.get_or_create(title='Engineer')
            elif 'design' in job_title.lower():
                the_category, _ = Category.objects.get_or_create(title='Designer')
            elif 'support' in job_title.lower() or 'customer' in job_title.lower():
                the_category, _ = Category.objects.get_or_create(title='Support')
            elif 'data' in job_title.lower():
                the_category, _ = Category.objects.get_or_create(title='Databases')
            elif 'manager' in job_title.lower():
                the_category, _ = Category.objects.get_or_create(title='Manager')

            raw_html = job_data.get('description', '')
            soup = BeautifulSoup(raw_html, "html.parser")
            clean_summary = soup.get_text(separator="\n", strip=True) 

            if not Jobs.objects.filter(urlLink=link).exists():
                uid = str(uuid.uuid4()).split('-')[0]
                new_job = Jobs.objects.create(
                    title=job_title,
                    urlLink=link,
                    date_posted=date.today(),
                    description=clean_summary,
                    summary=clean_summary[:200] + "...", 
                    company=the_company, 
                    category=the_category,
                    job_type=Jobs.FULL_TIME,
                    uniqueId=uid,
                    location=location,
                    slug=slugify(f"{job_title} {uid}")
                )
                added_count += 1
                
        print(f"[{timezone.now()}] Successfully added {added_count} NEW jobs (with REAL logos) from Remotive.")
        
    except Exception as e:
        print(f"Error fetching from Remotive: {e}")

# Automatically execute when called
fetch_rss_jobs()
