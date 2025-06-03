# 🗨️ Real-Time Chat App with Django Channels

A real-time chat application built using **Django**, **Django Channels**, **WebSockets**, and **Bootstrap 4**. Authenticated users can join chat rooms, send and receive messages instantly without page reload, and enjoy a modern, responsive UI.

---

## 🚀 Features

- 🔒 **User Authentication** (Login / Logout)
- 💬 **Real-Time Messaging** using Django Channels & WebSockets
- 🏠 **Chat Rooms** – Users can join different rooms using dynamic URLs
- 👤 **User-Specific Messages** – Sent and received messages are styled based on the sender
- 🧩 **Responsive UI** with Bootstrap 4 for a smooth experience
- ⚡ **Live Message Updates** without refreshing the page
- 🔁 Messages automatically scroll to the latest on arrival

---

## 🛠️ Tech Stack

- **Backend:** Django, Django Channels
- **Frontend:** HTML, CSS, Bootstrap 4, JavaScript
- **WebSockets:** Django Channels & Redis
- **Database:** SQLite (default) – easy to switch to PostgreSQL
- **Deployment-ready:** Easily extendable for production with Daphne + Redis

---
---

## ⚙️ Setup Instructions

1. **Clone the repository:**
   ```bash
   git clone https://github.com/your-username/django-realtime-chat.git
   cd django-realtime-chat
2. **create and activate a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

3. **install dependencies**
   ```bash
   pip install -r requirements.txt

4. **Apply migrations & create superuser (optional)**
   ```bash
   python manage.py migrate
   python manage.py createsuperuser

5. **Run Redis server(ensure redis is installed)**
   ```bash
   redis-server

6. **Run the Django development server**
   ```bash
   python manage.py runserver

7. **Access the app**
   ```bash
   Open http://localhost:8000 in your browser.

🧪 Testing
Login with a user account.

Enter a chat room using the URL /room-name.

Send messages and open another browser to see real-time updates.


🤝 Contribution
Pull requests are welcome. For major changes, please open an issue first.

 


