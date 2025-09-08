
<img width="1536" height="1024" alt="ChatGPT Image Sep 8, 2025, 12_13_20 PM" src="https://github.com/user-attachments/assets/8e6cab6e-0213-4d1a-aca8-f25c032cd4d2" />





CodeDrop is a Django-based RESTful web application that enables users to store, track, and receive useful code snippets automatically via email. The system is designed to improve developer productivity by sending curated code examples regularly or after snippet creation.

💡 Key Features:
🔐 User Authentication: Only authenticated users can manage snippets.

📥 Code Snippet Storage: Users can create, view, and delete code snippets via API.

🧠 Progress Tracking: The system remembers the last snippet sent using a SnippetTracker model.

📧 Automated Emailing: After creating a snippet, the next snippet is automatically emailed using Celery and Redis for background task processing.

🔄 Scheduled Emailing: Supports future scheduling (e.g., daily tips) using celery-beat.


🗂️ Core Components:
Snippet Model: Stores the actual code content and metadata.

SnippetTracker Model: Tracks what the user last received.

Celery Task: Queues and sends the next snippet asynchronously to prevent blocking.

Redis Queue: Acts as a broker for Celery to manage task queuing.

DRF Views: CRUD API endpoints for snippet management.


technolgy :
Django REST Framework (DRF)

PostgreSQL

Celery

Redis

Celery Beat

Docker

Docker Compose

SMTP (Email Service)

Git & GitHub
