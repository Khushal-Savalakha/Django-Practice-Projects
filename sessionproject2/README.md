
# Django Session Project

Welcome to the **Django Session Project**! This project demonstrates cookie handling and session management using Django, providing a step-by-step flow from user input through to displaying personalized content. 

> ### 🔍 **Preview of the Application Workflow**
>
> The application allows users to enter their name and password, stores these values in cookies, and displays the stored name along with the current date and time on subsequent pages.

---

## 🚀 Project Overview

This project consists of a simple Django application that:
1. Takes user input (name and password).
2. Stores the inputs as cookies.
3. Displays the stored values along with the current date and time.
4. Updates the display with each page refresh.

---

## 🛠️ Code Flow and Structure

### **1. Home View (User Input Form)**
![Home page](https://github.com/user-attachments/assets/5bd29184-09da-410c-bec6-e6315272f03f)
- **Path**: `/`
- **Template**: `home.html`
- **Function**: Displays a form for the user to input their name and password.
- **Action**: Submits the data to the `second` page (`date_time_view`) via a GET request.

#### **Visualization**:
  https://github.com/user-attachments/assets/d6b3e444-d17a-4a27-8ad9-2f799fe9ee7c

### **2. Date Time View (Set Cookies and Display Name)**
- **Path**: `/second/`
- **Template**: `date_time.html`
- **Function**: 
  - Retrieves the name and password from the request.
  - Sets cookies for the name and password.
  - Displays the name and provides a link to get the updated time.
  
#### **Visualization**:
   ![date time page](https://github.com/user-attachments/assets/43c8abba-8367-46c8-9e7b-135f71c35bef)
![date time page 2](https://github.com/user-attachments/assets/c12f8775-9855-43cd-8fa9-078a729bc6a2)
![date time page3](https://github.com/user-attachments/assets/1f2f20a6-80b3-4580-99bc-bf9bab653859)
### **3. Result View (Display Name and Current Date/Time)**
- **Path**: `/result/`
- **Template**: `result.html`
- **Function**: 
  - Retrieves the `name` from cookies.
  - Fetches the current date and time.
  - Renders a personalized greeting along with the current date and time.

#### **Visualization**:
   ![result page](https://github.com/user-attachments/assets/1f2f20a6-80b3-4580-99bc-bf9bab653859)


---

## 🗂️ Project Structure

```plaintext
sessionproject2/
│
├── testapp/
│   ├── templates/testapp/
│   │   ├── home.html
│   │   ├── date_time.html
│   │   └── result.html
│   ├── views.py          # Contains main views for the app
│   ├── forms.py          # Contains the LoginForm class for user input
│   └── urls.py           # Maps URLs to respective views
│
├── manage.py
└── README.md
```

![Add age](https://github.com/user-attachments/assets/13cef0b2-0996-42fe-93e8-366603be1e97)
