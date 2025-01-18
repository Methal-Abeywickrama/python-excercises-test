# Instructions for Python Beginners

## Getting Started: Running Tests with Pytest

This guide will walk you through setting up your environment to run Python tests using Pytest, starting from creating a GitHub account to running the provided test suite. This is aimed at Windows users.

---

### Step 1: Create a GitHub Account

1. Go to [GitHub](https://github.com/).
2. Click on **Sign up**.
3. Enter your email address, create a username, and set a password.
4. Follow the on-screen instructions to complete the setup.

---

### Step 2: Install Git on Windows

1. Download Git from the [official Git website](https://git-scm.com/downloads).
2. Run the installer and:
   - Keep the default options unless you have specific preferences.
   - Make sure to select **"Add Git to PATH"** during installation.
3. Verify the installation by opening Windows PowerShell and running:
   ```powershell
   git --version
   ```

---

### Step 3: Install Python

1. Download Python from the [official Python website](https://www.python.org/downloads/).
2. Run the installer and ensure you:
   - Check the option to **Add Python to PATH**.
   - Install for all users if prompted.
3. Verify the installation by opening Windows PowerShell and running:
   ```powershell
   python --version
   ```

---

### Step 4: Install Visual Studio Code (VS Code)

1. Download VS Code from the [official Visual Studio Code website](https://code.visualstudio.com/).
2. Run the installer and:
   - Select **"Add to PATH"** during installation.
   - Choose to install the Python extension if prompted.
3. Launch VS Code and install the Python extension (if not already installed):
   - Click on the Extensions icon.
   - Search for "Python" and click **Install**.

---

### Step 5: Install Pytest

1. Open Windows PowerShell.
2. Install Pytest by running:
   ```powershell
   pip install pytest
   ```
3. Verify the installation by running:
   ```powershell
   pytest --version
   ```

---

### Step 6: Fork and Clone the Repository

1. **Fork the Repository:**

   - Navigate to the repository [python-exercises-test](https://github.com/Methal-Abeywickrama/python-excercises-test) in your web browser.
   - Click on **Fork** (top-right corner) to create a copy under your GitHub account.
   - Copy the forked repository's URL by clicking the green **Code** button and copying the HTTPS link.

2. **Open PowerShell:**

   - Search for "PowerShell" in the Start menu or press `Win + R`, type `powershell`, and hit Enter.

3. **Navigate to the Documents Folder:**

   ```powershell
   cd Documents
   ```

   If you're not in the default user profile directory, specify the full path:

   ```powershell
   cd C:\Users\YourUsername\Documents
   ```

   Replace `YourUsername` with your actual Windows username.

4. **Create a Folder Called ****************************************`pythontests`****************************************:**

   ```powershell
   New-Item -Name "pythontests" -ItemType Directory
   ```

5. **Navigate to the ****************************************`pythontests`**************************************** Folder:**

   ```powershell
   cd pythontests
   ```

6. **Clone the Forked Repository:**

   ```powershell
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the HTTPS link you copied earlier.

7. **Verify the Folder is Created:**

   ```powershell
   ls
   ```

   You should see a folder with the repository's name in the list.

**Example Session:**

```powershell
PS C:\Users\YourUsername> cd Documents  
PS C:\Users\YourUsername\Documents> New-Item -Name "pythontests" -ItemType Directory  
PS C:\Users\YourUsername\Documents> cd pythontests  
PS C:\Users\YourUsername\Documents\pythontests> git clone https://github.com/YourUsername/python-excercises-test.git  
PS C:\Users\YourUsername\Documents\pythontests> ls  
```

---

### Step 7: Navigate to the Repository

1. Change to the cloned repository’s directory:
   ```powershell
   cd <repository-folder>
   ```
   Replace `<repository-folder>` with the folder name of the repository.

---

### Step 8: Open the Directory in VS Code

1. Open the current directory in VS Code:

   ```powershell
   code .
   ```

   The `.` indicates the current directory.

2. **Ensure the ****************************************`code`**************************************** Command is Available:**

   - If the `code` command is not recognized:
     1. Open VS Code.
     2. Press `Ctrl+Shift+P` (or `Cmd+Shift+P` on Mac) to open the Command Palette.
     3. Search for and select **Shell Command: Install 'code' command in PATH**.
     4. Restart PowerShell and try the `code .` command again.

---

### Step 9: Run the Tests

1. Run the test suite with Pytest:
   ```powershell
   pytest -v exercises/exercises1/test_solution.py
   ```
### Step 10: Unlock Tests

Each test is currently skipped using the `@pytest.mark.skip` decorator. To unlock a test:

1. Open the test file (e.g., `test_solution.py`) in VS Code or any text editor.
2. Remove the `@pytest.mark.skip` decorator from the test you want to unlock.
3. Save the file.
4. Re-run the tests to check your progress.

---

### Notes for Beginners

- **Debugging Tests:** If a test fails, read the error message carefully to understand the issue.
- If you cannot figure out something, do not use ChatGPT under any circumstances. Share it in the group chat, and finally me.

