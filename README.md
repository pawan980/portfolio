# Django Portfolio Website

A modern, responsive portfolio website built with Django, Django Cotton, Alpine.js, and Tailwind CSS.

## ✨ Features

- 🎨 Modern, responsive design with dark mode
- 📱 Mobile-first approach
- ⚡ Component-based architecture with Django Cotton
- 🎯 SEO optimized
- 📊 Admin panel for easy content management
- 💼 Project showcase with detailed pages
- 📝 Contact form with email notifications
- 🎓 Education & certification sections
- 💪 Skills with proficiency levels
- 🏢 Work experience timeline

## 🚀 Tech Stack

- **Backend**: Django 5.1+
- **Components**: Django Cotton 2.5+
- **Styling**: Tailwind CSS 3.4+
- **Interactivity**: Alpine.js 3.14+
- **Database**: SQLite (dev) / PostgreSQL (prod)

## 📦 Installation

### Prerequisites

- Python 3.11+
- Node.js 18+
- Git

### Setup

1. **Clone the repository:**
```bash
git clone <your-repo-url>
cd portfolio
```

2. **Create virtual environment:**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

3. **Install Python dependencies:**
```bash
pip install -r requirements/dev.txt
```

4. **Install Node dependencies:**
```bash
npm install
```

5. **Setup environment variables:**
```bash
cp .env.example .env
# Edit .env with your settings
```

6. **Run migrations:**
```bash
python manage.py migrate
```

7. **Create superuser:**
```bash
python manage.py createsuperuser
```

8. **Build CSS:**
```bash
npm run build:css
```

9. **Run development server:**

Terminal 1:
```bash
python manage.py runserver
```

Terminal 2:
```bash
npm run watch:css
```

10. **Visit:**
- Website: http://127.0.0.1:8000/
- Admin: http://127.0.0.1:8000/admin/

## 📝 Adding Content

1. Login to admin panel
2. Configure **Site Settings** with your information
3. Add **Skills** with categories and proficiency
4. Create **Projects** with images and details
5. Add **Work Experience**
6. Add **Education & Certifications**

## 🎨 Customization

### Change Colors

Edit `tailwind.config.js`:
```javascript
colors: {
  primary: {
    600: '#YOUR_COLOR',
  },
}
```

Then rebuild CSS:
```bash
npm run build:css
```

### Change Fonts

Update Google Fonts link in `templates/base.html` and font family in `tailwind.config.js`.
