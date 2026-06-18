# **📧 Email Spam Detection System – Final Semester Project**

### **Full Stack Machine Learning Web Application**

---

## **📌 Project Objective**

Develop a full stack web application that automatically classifies email messages as **Spam** or **Not Spam** using machine learning techniques. The system operates entirely offline using a locally trained model and a local SQLite database.

This project is an enhanced version of the **HAL Internship Project**, redesigned and extended as a final semester project with additional features such as user authentication, role-based access control, prediction history tracking, and an admin dashboard.

---

## 📁 Dataset

The dataset used in this project is a spam email dataset stored locally.

### **File:** `dataset/spam.csv`

### Key Columns

- **Message / Text – Email content**
- **Label** – Spam or Ham**

The dataset is used to train the machine learning model for accurate email classification.

---

## **🛠 Technology Stack**

### **Backend**
- Python
- Flask
- SQLite
- Scikit-learn
- Pandas
  
### **Frontend**
- HTML
- CSS

---

## **⚙ Features**
- User Registration and Login System
- Email Spam Detection (Manual Input)
- Machine Learning Model Integration
- Prediction History Storage
- Admin Dashboard
- Role-Based Access Control
- Responsive User Interface
- Offline Functionality (No Cloud / XAMPP)

---

## **🧠 Machine Learning Model**
- Algorithm: Multinomial Naive Bayes
- Text Processing: Vectorization
- Dataset: Local spam email dataset (dataset/spam.csv)

The trained model is stored locally using:
- spam_model.pkl
- vectorizer.pkl

---

## **📊 System Modules**

- ### **User Authentication Module**

Handles user registration, login, session management, and role-based access.

- ### **User Interface Module**

Provides interactive web pages for user registration, login, and email classification.

- ### **Model Training Module**

Trains the Multinomial Naive Bayes model using the spam dataset.

- ### **Feature Extraction Module**

Converts email text into numerical features using vectorization.

- ### **Spam Detection Module**

Classifies email messages using the trained machine learning model.

- ### **Admin Module**

Displays registered users and overall spam detection statistics.

- ### **Database Module**

Stores user information and prediction history using SQLite.

---

## **📂 Project Structure**
Email Spam Detection Project/

├── app.py
├── train_model.py
├── spam_model.pkl
├── vectorizer.pkl
├── users.db
│
├── dataset/
│   └── spam.csv
│
├── static/
│   ├── style.css
│   ├── welcomeimage.jpg
│   ├── loginimage.jpg
│   ├── registerimg.jpg
│   ├── indeximg.jpg
│   └── predictimg.jpg
│
├── templates/
│   ├── admin.html
│   ├── home.html
│   ├── index.html
│   ├── login.html
│   ├── register.html
│   ├── spam_checker.html
│   └── welcome.html
│
└── Output/
    └── screenshots

---

## **▶ How to Run**

### **1. Install Dependencies**
pip install flask pandas scikit-learn pickle

### **2. Train the Model**
python train_model.py

### **3. Run the Application**
python app.py

### **4. Open in Browser**
http://127.0.0.1:5000/

---

## **📊 Output**

- Welcome Page
- User Registration and Login
- Email Spam Detection Interface
- Spam / Not Spam Result Display
- Admin Dashboard
- Prediction History Storage

---

## **📈 Conclusion**

This project demonstrates the integration of machine learning and web technologies to build an efficient email spam detection system. The application provides accurate classification, secure user management, and an intuitive interface while functioning completely offline.

---

## **🚀 Future Enhancements**

- Real-Time Email Integration
- Advanced Machine Learning Models
- Multi-Language Support
- Cloud Deployment
- Password Encryption
- User Feedback Learning System

---

## **✨ Author**

**Sanjana S M**

**Final Semester Project**
