
# Notes Application - Django Backend

![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)

A RESTful API backend for a Notes application built with Django and Django REST Framework.

## Features

- User authentication (JWT)
- CRUD operations for notes
- Note categorization with tags
- Search functionality


## Requirements

- Python 3.8+
- pip

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/notes-app-backend.git
cd notes-app-backend
```

2. Create and activate virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
.\venv\Scripts\activate  # Windows
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run migrations:
```bash
python manage.py migrate
```

5. Create superuser:
```bash
python manage.py createsuperuser
```

6. Run development server:
```bash
python manage.py runserver
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/notes/` | GET | GET NOTES|
| `/notes` | POST | POST NOTE |
| `/notes-search/` | GET | Search notes |
| `/notes/<slug:slug>` | GET, PUT, DELETE | Retrieve/Update/Delete note |
| `/categories/` | GET | List Categories |
| `/categories/add-category/` | POST | Add Categories |
| `/categories/delete/<int:id>/` | POST | Delete Category |


## Project Structure

```
notes_app/
├── notes/                # Notes app
│   ├── migrations/       # Database migrations
│   ├── models.py         # Data models
│   ├── serializers.py    # API serializers
│   └── views.py          # API views            
├── manage.py             # Django CLI
└── requirements.txt      # Dependencies
```

## Contributing

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

MIT
```

### Key Features of this README:
1. **Badges** - Visual indicators for technologies used
2. **Clear Installation** - Step-by-step setup instructions
3. **API Documentation** - Easy reference for endpoints
4. **Deployment Guide** - Ready for Render.com
5. **Project Structure** - Helps new developers navigate
6. **Contributing Section** - Encourages open-source collaboration


