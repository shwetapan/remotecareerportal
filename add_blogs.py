import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "workremotely.settings")
django.setup()

from blog.models import Post

blogs = [
    {
        "title": "The Exhausted Developer's Guide to a Winning Job Search Strategy",
        "desc": "Look, I get it. You just spent 8 hours debugging a weird race condition, and now you have to 'network' on LinkedIn? No thanks. But here’s the truth: shotgunning 100 applications a day into the void using Quick Apply doesn't work anymore.\n\nI recently changed how I approach the job hunt. Instead of applying everywhere, I picked 5 companies I actually liked. I read their engineering blogs, found the hiring managers on Twitter, and sent them a quick message about something they built. It felt awkward, but it got me 3 interviews in a week. Your strategy shouldn't be about volume; it should be about precision. Treat your job search like a targeted debugging session. Find the right stack trace, isolate the component, and strike."
    },
    {
        "title": "Throw Away Your Fancy Resume Template (Yes, Right Now)",
        "desc": "If your resume has two columns, a progress bar for your JavaScript skills (what does 75% JavaScript even mean?), and a photo of you looking pensively into the distance, you're doing it wrong.\n\nATS (Applicant Tracking Systems) hate multi-column layouts. Recruiters hate reading paragraphs. Do yourself a favor: open a plain Google Doc. Put your name, contact info, and GitHub at the top. For your experience, use bullet points that follow the 'Action + Context + Result' format. For example: 'Reduced API response time by 40% (Result) by implementing Redis caching on the main endpoint (Action/Context).' Keep it to one page if you have less than 10 years of experience. Simple, boring, single-column resumes get interviews. Save the fancy design for your portfolio site."
    },
    {
        "title": "How to Actually Find the Best Remote Jobs Before Everyone Else",
        "desc": "Everyone knows about the big remote job boards. By the time a 'Remote React Developer' role is posted on LinkedIn, it already has 500 applicants.\n\nIf you want to find the good remote jobs, you have to look where the crowd isn't. First, check out niche communities. Slack and Discord groups for your specific framework (like Next.js or Vue) often have #jobs channels where founders post roles directly. Second, look at Open Source projects you use. Many commercial open-source companies hire remotely and heavily recruit from their own contributors or community members. Lastly, use advanced search on X/Twitter: 'hiring remote frontend -link' to filter out the automated job board bots and find actual humans tweeting about open roles on their teams."
    },
    {
        "title": "Using AI in Your Job Search: Don't Be a Robot",
        "desc": "We've all seen them: the cover letters that start with 'As an AI language model, I would be a great fit for your Senior Frontend role...' Or the painfully obvious ChatGPT-generated messages filled with words like 'delve' and 'testament.'\n\nAI is a massive cheat code for the job hunt, but only if you use it right. Don't use it to generate your entire resume or cover letter. Instead, use it as a sparring partner. Paste a job description and your resume into Claude or ChatGPT and ask, 'What are the biggest gaps between my experience and this role, and how can I frame my existing skills to bridge them?' Or ask it to generate tricky interview questions based on the company's tech stack. Use AI to prepare and strategize, but write the final communication yourself. Being authentically human is actually a competitive advantage right now."
    }
]

for b in blogs:
    Post.objects.create(title=b["title"], desc=b["desc"])
    print(f"Added: {b['title']}")

print("All blogs added successfully!")
