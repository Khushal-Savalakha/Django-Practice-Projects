# Shopping App

An interactive Django application that allows users to add items with quantities and view them temporarily via cookies, with data persistence lasting for 60 seconds.

---

## 📑 Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Demo Video](#demo-video)
- [Application Workflow](#application-workflow)
- [Screenshots](#screenshots)
- [Flowchart](#flowchart)
- [Additional Resources](#additional-resources)

---

## Overview
This Django app demonstrates a basic item management system, focusing on adding and displaying items with temporary storage in cookies.

### ⚙️ Technology Stack
- **Backend**: Django
- **Frontend**: HTML/CSS
- **Storage**: Cookies

## Features
- **Add Items**: Enter item names and quantities, stored temporarily.
- **View Items**: Display items stored in cookies.
- **Cookie Persistence**: Items are stored for 60 seconds.
---

## Demo Video


https://github.com/user-attachments/assets/6ebc0ed0-5aef-4a3d-a6ad-7810ecd51ff8
---

## Application Workflow

1. **Home Page**  
   The `index_view` function renders the home page, providing an entry point for users.

2. **Add Item Page**  
   - **View**: The `additems_view` function displays an `AddItemForm` for item input.
   - **Data Handling**: If the form is submitted via POST, item data (name and quantity) is validated and stored in a cookie, available for 60 seconds.
   - **Template**: `add_item.html` renders the form and displays a message upon successful addition.

3. **Display Items Page**  
   - The `displayitems_view` renders `display_items.html`, listing items retrieved from cookies.

---

## Screenshots

### 🏠 Home Page
![Home page](https://github.com/user-attachments/assets/c78fbaaf-5bc9-4298-910c-f5d5ecce9e85)

### ➕ Add Item Page
![Add item page](https://github.com/user-attachments/assets/7e1515e7-2da4-4b2f-93b9-dd1f101422a9)

### 📋 Display Items Page
![Display item page](https://github.com/user-attachments/assets/114c0859-395a-4370-80f3-54140ce94a66)

---

## Flowchart

```mermaid
graph TD
    A[Home Page] -->|Click on Add Item| B[Add Item Page]
    B -->|Submit Form| C{Form Valid?}
    C -- Yes --> D[Store in Cookie]
    D --> E[Redirect to Home Page]
    C -- No --> F[Display Form Errors]
    E --> G[Display Item Page]
    F --> B
    G -->|Show Items| E
```

This flowchart visually represents the interaction between pages and data flow, including form handling and item storage in cookies.




---

## Additional Resources

- 📖 [Django Documentation](https://docs.djangoproject.com/)
- 🍪 [Managing Cookies in Django](https://docs.djangoproject.com/en/stable/topics/http/sessions/#using-cookies-directly)

--- 
