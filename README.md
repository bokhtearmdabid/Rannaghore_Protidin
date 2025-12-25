# Rannaghore Protidin

<div align="center">

[![Render Deployment](https://img.shields.io/badge/render-deployed-brightgreen?logo=render&style=for-the-badge)](https://rannaghore-protidin.onrender.com)
[![Django](https://img.shields.io/badge/Django-5.2.5-092E20?logo=django&style=for-the-badge)](https://www.djangoproject.com/)
[![Python](https://img.shields.io/badge/Python-3.13-3776AB?logo=python&style=for-the-badge&logoColor=white)](https://www.python.org/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Neon-4169E1?logo=postgresql&style=for-the-badge&logoColor=white)](https://neon.tech/)

**Your One-Stop Shop for Household & Baking Essentials**

[Live Demo](https://rannaghore-protidin.onrender.com) • [Report Bug](https://github.com/bokhtearmdabid/Rannaghore_Protidin/issues) • [Request Feature](https://github.com/bokhtearmdabid/Rannaghore_Protidin/issues)

</div>

---

## 📖 About The Project

**Rannaghore Protidin** (রান্নাঘর প্রতিদিন) is a modern e-commerce platform specializing in household items and professional cake baking supplies. Whether you're a home baker looking for the perfect cake decorating tools or searching for everyday household essentials, we've got you covered!

### ✨ Why Choose Rannaghore Protidin?

- 🎂 **Specialized Catalog**: Curated selection of premium baking supplies and household items
- 🔐 **Secure Authentication**: Google OAuth integration for hassle-free login
- 🛒 **Smart Shopping Cart**: Easy-to-use cart system with real-time updates
- 📦 **Order Tracking**: Complete order management system with status tracking
- 💬 **Customer Support**: Integrated support ticket system for quick assistance
- 📱 **Responsive Design**: Seamless experience across all devices

---

## 🚀 Features

### 🛍️ For Customers

- **Browse Products**: Explore our extensive catalog of baking and household items
- **Search & Filter**: Find exactly what you need with powerful search functionality
- **Secure Checkout**: Safe and easy payment process
- **Order History**: Track all your orders in one place
- **Profile Management**: Update your information anytime
- **Google Sign-In**: Quick authentication with your Google account

### 👨‍💼 For Administrators

- **Dashboard**: Comprehensive admin panel for managing the store
- **Product Management**: Add, edit, and organize products effortlessly
- **Order Processing**: Handle orders with multiple status stages (Pending → Confirmed → Processing → Shipped → Delivered)
- **Customer Support**: Manage support tickets and customer inquiries
- **FAQ Management**: Create and update frequently asked questions
- **Analytics**: Track sales and customer engagement

---

## 🛠️ Built With

### Backend
- **Django 5.2.5** - High-level Python web framework
- **Python 3.13** - Programming language
- **PostgreSQL** - Robust relational database via Neon
- **Gunicorn** - WSGI HTTP Server

### Frontend
- **HTML5 & CSS3** - Modern markup and styling
- **JavaScript** - Interactive user experience
- **Bootstrap** - Responsive design framework

### Authentication & Social
- **Django Social Auth** - Google OAuth2 integration
- **Python Social Auth** - Social authentication library

### Storage & Media
- **WhiteNoise** - Static file serving
- **Pillow** - Image processing

### Deployment
- **Render** - Cloud hosting platform
- **Neon** - Serverless PostgreSQL database

---

## 📦 Installation

### Prerequisites

- Python 3.11 or higher
- PostgreSQL database
- Git

## 📁 Project Structure

```
Rannaghore_Protidin/
├── RannaghoreProtidin/          # Main project directory
│   ├── settings.py              # Django settings
│   ├── urls.py                  # URL configuration
│   └── wsgi.py                  # WSGI configuration
├── rannaghoreprotidinapp/       # Main application
│   ├── models.py                # Database models
│   ├── views.py                 # View functions
│   ├── urls.py                  # App URLs
│   ├── admin.py                 # Admin configuration
│   └── migrations/              # Database migrations
├── templates/                   # HTML templates
│   ├── shop/                    # Shop templates
│   └── emails/                  # Email templates
├── static/                      # Static files (CSS, JS, Images)
├── staticfiles/                 # Collected static files
├── media/                       # User uploaded files
├── requirements.txt             # Python dependencies
├── build.sh                     # Build script for deployment
├── .gitignore                   # Git ignore file
└── README.md                    # Project documentation
```

---

## 🗄️ Database Models

### Core Models

- **UserInfo**: Extended user profile with contact information
- **Products**: Product catalog with images, pricing, and descriptions
- **Cart**: Shopping cart items for users
- **Order**: Order management with status tracking

### Support Models

- **SupportTicket**: Customer support ticket system
- **TicketReply**: Conversation threads for tickets
- **FAQ**: Frequently asked questions
- **ContactMessage**: General contact form submissions

---

## 🔐 Security Features

- ✅ CSRF Protection enabled
- ✅ Secure password hashing
- ✅ SQL injection prevention via Django ORM
- ✅ XSS protection with template escaping
- ✅ HTTPS enforcement in production
- ✅ Environment variable management
- ✅ Secure session handling

---

## 📧 Contact & Support
- **GitHub**: [@bokhtearmdabid](https://github.com/bokhtearmdabid)
- **Project Link**: [https://github.com/bokhtearmdabid/Rannaghore_Protidin](https://github.com/bokhtearmdabid/Rannaghore_Protidin)

---

## 🤝 Contributing

Contributions are what make the open source community amazing! Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 🙏 Acknowledgments

- [Django Documentation](https://docs.djangoproject.com/)
- [Render Documentation](https://render.com/docs)
- [Neon Database](https://neon.tech/)
- [Bootstrap](https://getbootstrap.com/)
- [Font Awesome](https://fontawesome.com/)

---

<div align="center">

**Made with ❤️ by [Abid Muhammad](https://github.com/bokhtearmdabid)**

⭐ Star this repo if you find it helpful!

</div>
