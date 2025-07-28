# 🌱 EcoWaste ♻️
## 📖 Overview 
EcoWaste is a sustainability-focused menu based application that helps users git rid of their waste at no cost. This CLI app is intended to stimulate a real-world recycling marketplace for educational/demo purposes. By promoting responsible waste management, EcoWaste supports the fight against climate change and promise a better more sustainable planet.
<br></br>


## 🚀 Features 
- **User Authentication**: Prompt for users to log in or create an new account.
- **Provider Menu**: A menu that allows the user to list recyclable waste items they want to get rid of.
- **Buyer Menu**: A menu that allows the user as a buyer (companies) to see exsisting list of items they want to buy.
<br></br>

## ⚙️ Technologies used 
- Python Programming
- SQLAlchemy for database management
- MySQL as a database engine
<br></br>


## 📏 Installation 
To set up the EcoWaste project on your local machine you need to follow these steps:
 
 i. Clone the project repository locally using your desired terminal. 
 
 ```sh
      git clone https://github.com/Eelaf-Adam/Group26_EcoWaste_PLP2
      cd Group26_EcoWaste_PLP2
```

ii. Create and activate a virtual environment

 ```sh
      #On windows
      python -m venv .venv
     .venv\Scripts\activate

      #On MacOS/Linux
      python3 -m venv .venv
      source .venv/bin/activate
```
iii. Install Dependencies

 ```sh
      pip install -r requirements.txt
```
iv. Set Up Environment Variables

 ```sh
      #If you are not using .env file you can skip this step
      DATABASE_URL=mysql+myconnector://your-db-url
```
v. Run the Application

 ```sh
      python main.py
```
<br>

## 💻 User Journey
After installing and running the app using 'python main.py', you will interact with it directly in your terminal.

### 1. 📧 Email Prompt
  You'll be asked to enter your email:
  - If the email exists, you'll be prompted to log in.
  - If the email is not found, you can create a new account.

---

### 2. 🔐 Sign Up Options
  - Choose your role:
     **Buyer**: A company or organization interested in purchasing waste.
     **Provider**: An individual or organization listing waste items.
    
  - Depending on your role, you'll be prompted to enter:
      - Name / Company Name
      - Location
      - Password   
---

### 3. 📋 Logged-In Menus

### 👤 Buyer Menu:
  - View available waste listings
  - Purchase listed items
  - View your purchase history

### 👤 Provider Menu:
  - Add new recyclable waste listings
  - View your active listings

---

### 4. 🧭 Navigation
  - All actions are selected through simple number or text-based input in the terminal
  - You can exit the application at any time using the quit option
---

# Project Structure 

```plaintext
📁Group26_EcoWaste_PLP2/
├── 📄main.py               #Contains logic to run the program
├── 📄requirements.txt      #Contains the requirements to run the file
├── 📄.env                  #Contains the database URL
├── 📄reset_db.py           #File run once to reset / clear the database tables
├── 📄table_creation.py     #File run once to populate database with respective tables
│
├── 📁controllers/          #Contains the logic for all user prompts
│   └── 📄auth.py           #Contains the logic for user account creation
|   └── 📄buyer_home.py     #Contains the logic for buyer prompts
|   └── 📄provider_home.py  #Contains the logic for provider prompts
│
├── 📁models/
│   ├── 📄database.py       #Connects the code to the database
│   └── 📄listings.py       #Creation and specification of requirements for listing table
|   └── 📄purchases.py      #Creation and specification of requirements for purchases table
|   └── 📄user.py           #Creation and specification of requirements for user table
│
├── 📁utils/
│   └── 📄security.py       #Connects the functions to hash user passwords on the database
│
└── 📄README.md
```

# 🛠️ DataBase setup 

### 1. Install MySQL Server
- **Windows:** Download and install from [MySQL Downloads]
- **macOS:** Use Homebrew:
  ```sh
  brew install mysql
- Linux
  ``` sh
  sudo apt update
  sudo apt install mysql-server

### 2. Create the Database
``` sql
CREATE DATABASE ecowaste_db;
```
OR
``` sh
mysql -u root -p
```

### 3. Configure Environment Variables
``` env
DATABASE_URL=mysql+mysqlconnector://{your_username}:{your_password}@localhost:3306/ecowaste_db?ssl-mode=DISABLED
```

### 4. Initialize the Database Schema
``` sh
python main.py
```
---
# 👩‍💻 Authors
- **Leon Nsamba**
- **Eelaf Adam**
<br></br>
---
### 💡Inspiration
This project was part of the Peer Learning Project Group 26 Summative at ALU. The project tasked us to develop a command-line-based, minimal menu-driven application that is Python-based and uses database technology. The software was designed to address a GCGO (Climate Change) that aligns with the group's mission and interests.
<br></br>


    
