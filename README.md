# Instructions for Writing Methods in `solutions.py` and Running Tests

## Prerequisites
Before proceeding, ensure you have completed the following:
- Installed Python 3.12 or higher.
- Installed Git and Pytest on your system.
- Forked and cloned the repository to your local machine.
- Installed all required dependencies (as outlined in the previous guide).

You should also ensure you are in the root directory of the cloned repository.

---

## Writing Methods in `solutions.py`
The `solutions.py` file contains method stubs with comments describing what each method should do. You need to:

1. **Open the `solutions.py` File:**
   Navigate to the `solutions.py` file in your code editor or IDE.

2. **Identify the Function to Work On:**
   Each method includes comments explaining its purpose. For example, the `add(a, b)` function includes the comment:
   ```python
   # Return the result of adding a and b.
   ```

3. **Implement the Method Logic:**
   Replace the `pass` statement in the method with the required logic. For example:
   ```python
   def subtract(a, b):
       return a - b
   ```

4. **Save Your Work:**
   After implementing a method, save the changes to the `solutions.py` file.

---

## Unskipping and Running Tests
Each test in `test_solution.py` is initially skipped using the `@pytest.mark.skip` decorator. You will unskip tests one by one as you complete each corresponding method.

### Steps to Unskip and Run Tests

1. **Open the `test_solution.py` File:**
   Navigate to the `test_solution.py` file in your code editor.

2. **Locate the Relevant Test:**
   Find the test corresponding to the method you implemented. For example, if you implemented the `subtract` method, locate:
   ```python
   @pytest.mark.skip
   def test_subtract_two_numbers(self):
       assert solution.subtract(5, 3) == 2
   ```

3. **Remove the Skip Marker:**
   Delete the `@pytest.mark.skip` decorator. The test should now look like this:
   ```python
   def test_subtract_two_numbers(self):
       assert solution.subtract(5, 3) == 2
   ```

4. **Save Your Changes:**
   Save the updated `test_solution.py` file.

5. **Run the Tests:**
   Open a terminal in the root directory of the project and run the following command:
   ```bash
   pytest exercises/exercises1/test_solution.py
   ```

6. **Check the Test Results:**
   - If the test passes, you’ve successfully implemented the method.
   - If the test fails, review the error message, update your implementation in `solutions.py`, and rerun the test.

7. **Repeat for Each Test:**
   - Implement the next method in `solutions.py`.
   - Unskip the corresponding test in `test_solution.py`.
   - Run the tests and verify your implementation.

---

## Important Notes

- **Test Incrementally:**
  Always work on one method and its corresponding test at a time. This ensures you can isolate and fix any issues quickly.

- **Stay in the Root Directory:**
  All commands should be run from the root directory of the cloned repository. If unsure, you can check your current directory by running:
  ```bash
  pwd
  ```

- **Use Clear Logic:**
  The comments in each method provide hints about the expected logic. Ensure your implementation adheres to these requirements.

- **Verify Results:**
  Each test will provide feedback on whether your implementation is correct. If a test fails, carefully read the output to identify the issue.

---

## Example Workflow

### Implementing and Testing the `subtract` Method
1. Open `solutions.py` and implement the `subtract` method:
   ```python
   def subtract(a, b):
       return a - b
   ```

2. Open `test_solution.py` and locate:
   ```python
   @pytest.mark.skip
   def test_subtract_two_numbers(self):
       assert solution.subtract(5, 3) == 2
   ```

3. Remove the `@pytest.mark.skip` decorator.

4. Save both files.

5. Run the tests:
   ```bash
   pytest exercises/exercises1/test_solution.py
   ```

6. Verify the output:
   - If the test passes, proceed to the next method.
   - If the test fails, debug and fix your implementation in `solutions.py`.

---

Following this approach will help you systematically implement and test each function while building your Python programming skills.

