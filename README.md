# account-manager

## About this Project

A simple command-line account manager to generate, save and manage passwords locally.

This is my small Python Project I worked on as a exercise.

> ⚠️ **Disclaimer**: Do not use real passwords with this script. It is for educational purposes only.

## Installation

To ensure a clean environment, it is recommended to use a virtual environment (**venv**).

1. **Clone the repository:**

   ```bash
   git clone <your-repo-url>
   cd account-manager
   ```

2. Create & active a virtual environment

Windows:

    ```bash
    python -m venv venv
    .\venv\Scripts\activate
    ```

Mac/Linux:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Install dependencies

   ```bash
   pip install keyring
   ```

4. Run the application;
   ```bash
   python main.py
   ```

## Features

- Generate Random Password
- Robust Error Handling
- Save your Account with IDs
- Show & Delete Accounts
- Object Oriented Syntax

## How to Use

- For Menu navigation type in the number which menu to select
- for "yes", type in "y" or "yes"

## Built With

- Python

## What I Learned

- OOP with Python
- Error Handling
- Reading Json files
- Random module
- Lists and Dicts
- Writing clean and organized code
