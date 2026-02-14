# Django Portfolio Website
A cyberpunk-themed digital showcase of my work and professional journey with modern UI/UX.

## ✨ Features

### 🎯 Projects Showcase
- **Category Filtering**: Filter projects by Web Apps, Backend, AI Agents, Open Source, Data Engineering
- **Multiple Categories**: Projects can belong to multiple categories simultaneously
- **Featured Projects**: Highlight important projects with full-width cards
- **Status Badges**: Live, In Development, or Archived status with animated indicators
- **Rich Metadata**: Display GitHub stars, dates, technologies, and categories
- **Multiple Links**: Support for Live Demo, GitHub, Case Study, and Documentation links
- **Drag & Drop Ordering**: Reorder projects in admin with django-admin-sortable2

### 📝 Blog
- **Modern Card Layout**: Clean grid design with responsive columns
- **External Links**: Support for cross-posted articles with source indicators
- **Tag System**: Categorize posts with tags
- **Read Time**: Automatic read time calculation

### 💬 Testimonials
- **Client Testimonials**: Responsive carousel with star ratings
- **LinkedIn Integration**: Direct links to testimonial authors
- **Public Submission**: Allow clients to submit testimonials via form
- **Smart Display**: Shows 1-3 testimonials per page based on screen size

### 📊 Analytics
- **Page View Tracking**: Monitor visitor engagement
- **Project Click Analytics**: Track project interest
- **Contact Form Submissions**: Log inquiry patterns

### 🎨 Design System
- **Cyberpunk Theme**: Gradient animations, neon effects, glass morphism
- **Responsive**: Mobile-first design with Tailwind CSS
- **Smooth Animations**: Fade-in effects with stagger delays
- **Sticky Navigation**: Fixed category filters with backdrop blur

## 🚀 Tech Stack

- **Backend**: Django 4.2.27
- **Components**: django-cotton 2.5.0 for reusable template components
- **Styling**: Tailwind CSS 3.4.1 with @tailwindcss/typography
- **Interactivity**: Alpine.js 3.14.1
- **Static Files**: WhiteNoise 6.8.2
- **Storage**: django-storages with AWS S3 support (boto3)
- **Database**: SQLite (dev) / PostgreSQL (prod)
- **Admin**: django-admin-sortable2 for drag & drop ordering

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
# Create .env file in project root
touch .env
```

Add the following to your `.env` file:
```env
DEBUG=True
SECRET_KEY=your-secret-key-here
ALLOWED_HOSTS=localhost,127.0.0.1
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

### Site Settings
1. Login to admin panel at `/admin/`
2. Configure **Site Settings** with your personal information
3. Upload profile picture and favicon

### Projects
1. Navigate to **Projects** in admin
2. Click **Add Project**
3. Fill in required fields:
   - **Title**: Project name
   - **Short Description**: Brief summary (shown on cards)
   - **Description**: Detailed description (shown on featured projects)
   - **Categories**: Select multiple categories (Web Apps, Backend, AI Agents, etc.)
   - **Technologies**: Comma-separated list (e.g., "Django, React, PostgreSQL")
   - **Thumbnail**: Main project image
4. Optional fields:
   - **Featured Image**: Additional hero image
   - **Status**: Completed, In Progress, or Planned
   - **Live URL**: Link to live demo
   - **GitHub URL**: Link to repository
   - **Case Study URL**: Link to detailed article
   - **Documentation URL**: Link to docs
   - **Stars**: GitHub stars count
   - **Dates**: Start and end dates
5. Toggle **Is Featured** to display as full-width card
6. Toggle **Is Published** to make visible
7. Use drag handles to reorder projects

### Blog Posts
1. Navigate to **Blog** → **Posts**
2. Add posts with title, content, cover image
3. Set **Published Date** to make visible
4. Add tags (comma-separated)
5. Optional **External URL** for cross-posted articles

### Skills & Experience
1. Add **Skills** with categories and proficiency levels
2. Create **Work Experience** entries
3. Add **Education & Certifications**
4. Use drag handles to reorder items

## 🧩 Component System

This project uses **django-cotton** for reusable template components with a clean, prop-based API.

### Available Components

- **`<c-section>`**: Page sections with title and subtitle
  ```html
  <c-section title="My Section" subtitle="Description">
    <!-- content -->
  </c-section>
  ```

- **`<c-card>`**: Styled content cards with cyberpunk theme
  ```html
  <c-card>
    <!-- card content -->
  </c-card>
  ```

- **`<c-social-icon>`**: Social media icons with hover effects
  ```html
  <c-social-icon platform="github" url="https://github.com/username" size="w-8 h-8" />
  ```

- **`<c-lazy-image>`**: Lazy-loaded images with loading states
- **`<c-share-buttons>`**: Social sharing buttons for blog posts

### Creating Custom Components

1. Create a new file in `templates/cotton/`
2. Add `<c-vars>` to declare props:
   ```html
   <c-vars 
     title="{{ title|default:'' }}"
     subtitle="{{ subtitle|default:'' }}"
   />
   ```
3. Use props in your template
4. Access with `<c-component-name>` syntax

## 🎨 Customization

### Change Theme Colors

Edit `tailwind.config.js` to modify the color scheme:
```javascript
colors: {
  cyan: { /* Primary accent */ },
  purple: { /* Secondary accent */ },
  green: { /* Success/Live status */ },
  // Add your custom colors
}
```

Then rebuild CSS:
```bash
npm run build:css
```

### Change Fonts

Current fonts (from Google Fonts):
- **Headings**: 'Sora' (modern, bold)
- **Body**: System fonts
- **Code**: 'JetBrains Mono' (monospace)

To change:
1. Update font links in `templates/base.html`
2. Modify `font-family` in templates or add to `tailwind.config.js`

### Project Categories

Project categories are stored in the database. To modify:

1. Login to admin panel
2. Navigate to **Projects**
3. Edit the **categories** field (comma-separated values)
4. Available categories: `web_apps`, `backend`, `ai_agents`, `open_source`, `data_engineering`

To add new categories, update the filtering logic in `apps/projects/views.py`.

## 📁 Project Structure

```
portfolio/
├── apps/
│   ├── core/          # Base models & site settings
│   ├── projects/      # Project showcase (with categories, filtering)
│   ├── blog/          # Blog posts and articles
│   ├── experience/    # Work experience
│   ├── education/     # Education & certifications
│   ├── contact/       # Contact form
│   ├── testimonials/  # Client testimonials
│   └── analytics/     # Page view tracking
├── config/            # Django settings (split: base, dev, prod)
├── static/            # CSS, JS, images
│   ├── src/          # Tailwind source files
│   └── css/          # Compiled CSS
├── templates/         # HTML templates
│   ├── base.html     # Base template
│   ├── cotton/       # Django-cotton components
│   └── pages/        # Page templates
└── requirements/      # Python dependencies (base, dev, prod)
```

## 🔧 Development

### Running with Live Reload (Recommended)

Terminal 1 - Django server:
```bash
python manage.py runserver
```

Terminal 2 - Tailwind watch mode:
```bash
npm run watch:css
```

### Running without Auto-reload (Performance)

If experiencing slow server performance:
```bash
python manage.py runserver --noreload
```

**Note**: Requires manual server restart after code changes.

### Building for Production

```bash
# Build optimized CSS
npm run build:css

# Collect static files
python manage.py collectstatic --noinput

# Run with production settings
python manage.py runserver --settings=config.settings.production
```

## 🐛 Troubleshooting

### Admin Pages Blank
1. Check if server is running
2. Hard refresh browser (Cmd+Shift+R / Ctrl+Shift+R)
3. Clear browser cache

### CSS Changes Not Showing
1. Rebuild CSS: `npm run build:css`
2. Hard refresh browser
3. Check if `static/css/output.css` was updated

### Multiple Server Instances
If server is slow:
```bash
# Kill all Django processes
pkill -9 -f "manage.py runserver"

# Restart server
python manage.py runserver --noreload
```

### Category Filtering Not Working
1. Check project has categories assigned in admin
2. Verify categories field format: comma-separated keys (e.g., "web_apps,backend")
3. Ensure migrations are applied: `python manage.py migrate`

## 📄 License

[Your License Here]

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

## 👤 Author

**Your Name**
- Website: [your-site.com](https://your-site.com)
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)
