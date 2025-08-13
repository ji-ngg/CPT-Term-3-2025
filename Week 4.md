# Week 4 - Data flow of app
## Algorithm Flowchart
<img width="1278" height="1235" alt="CPT3 Y10 Flowchart" src="https://github.com/user-attachments/assets/65871404-b8cb-452e-9907-67d37e42fa36" />


## Data flow
| **Data**       | **Details**                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| **Inputs**      | - name<br>- email<br>- password<br>- reCAPTCHA (human verification)            |
| **Data Flow**   | 1. prompt user to fill in form fields<br>2. clicks submit<br>3. all variables are verified    |
|                 | 4. IF reCAPTCHA FAILS -> redirect to error message (reCAPTCHA) <br> Error message: `Invalid reCAPTCHA! Try again`, prompt user to re-enter the data <br> 5. if email is invalid -> redirect to error message (email)  <br> Error message: `Invalid email! Try again`, prompt user to re-enter the data.  <br>6. if all valid -> save name/email/password to online database                  |
|                 | 7. redirect to clock page                                                      |
|                 | 8. show confirmation of account details via a popup                              |
| **Output**      | if successful: `"Account created!"` (shown as popup on clock page)<br> if failed: appropriate error message |

## Test case ID - ACCOUNT CREATION
| **Functionality** | testing |
|------------------|--------|
| Test case ID| #001|
| **Pre-conditions** | ALL boxes (ie. email, password, first name, reCAPTCHA) filled |
| **Purpose**      | to check for a sucessful account creation when passing  |
| **Test Steps** | 1. Open application <br> 2. Enter full name, email and make a password <br> 3. Fill in the reCAPTCHA <br> 4. Click `Create Account` button |
| **Expected Result** | 1. redirects to clock<br> 2. popup message: `Account created!`<br> 3.user data then is saved to database |
| **Priority** | Medium-High |

## Test case 2 - LOG IN
| **Functionality** | testing |
|------------------|--------|
| Test case ID| #002|
| **Pre-conditions** | ALL boxes (ie. email, password, reCAPTCHA) filled |
| **Purpose**      | to be able to log into the application with minimal bugs and with a clear layout  |
| **Test Steps** | 1. Open application <br> 2. Enter email and password <br> 3. Fill in the reCAPTCHA <br> 4. Click `Log in` button |
| **Expected Result** | 1. credentials entered is matched to the database <br> 2. redirects to clock<br> 3. popup message: `Successfully logged in!!`<br>|
| **Priority** | Medium-High |

## Test case - FORGOT PASSWORD
| **Functionality** | testing |
|------------------|--------|
| Test case ID| #003|
| **Preconditions** | User has an account and remembers the email they signed up with |
| **Purpose** | To allow users to change their password credentials in case they forget |
| **Test Steps** | 1. User writes in their email <br>2. Presses the `Send an email` button <br>3. Get an email to change their password sent to the inbox of the email they entered |
| **Expected Results** |1. User opens application <br> 2. Presses forgot password on the Log in page <br> 3. Redirected to page and enters email they have an account with <br> 4. Email sent to their inbox <br> 5. User changes their email with the link sent and successfully logs in |
|**Priority**| Low-Medium
