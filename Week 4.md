# Week 4 - Data flow of app
## Algorithm Flowchart
<img width="3705" height="2389" alt="CPT3 Y10 Flowchart (2)" src="https://github.com/user-attachments/assets/74878578-d24e-47f8-a148-7641989bb1b6" />

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
| **Test Steps** | Open application <br> Enter full name, email and make a password <br> Fill in the reCAPTCHA <br> Click `Create Account` button |
| **Expected Result** | - redirects to clock<br>- popup message: `Account created!`<br>- user data then is saved to database |
| **Priority** | Medium-High |

## Test case 2 - LOG IN
| **Functionality** | testing |
|------------------|--------|
| Test case ID| #002|
| **Pre-conditions** | ALL boxes (ie. email, password, reCAPTCHA) filled |
| **Purpose**      | to be able to log into the application with minimal bugs and with a clear layout  |
| **Test Steps** | Open application <br> Enter email and password <br> Fill in the reCAPTCHA <br> Click `Log in` button |
| **Expected Result** | credentials entered is matched to the database <br> redirects to clock<br>- popup message: `Successfully logged in!!`<br>|
| **Priority** | Medium-High |

## Test case - FORGOT PASSWORD
| **Functionality** | testing |
|------------------|--------|
| Test case ID| #003|
| **Preconditions** | User has an account and remembers the email they signed up with |
| **Purpose** | To allow users to change their password credentials in case they forget |
| **Test Steps** | User writes in their email, then presses the `Send an email` button, they'll get an email to change their password sent to the inbox of the email they entered |
| **Expected Results** | User opens application <br> Presses forgot password on the Log in page <br> Redirected to page and enters email they have an account with <br> Email sent to their inbox <br> User changes their email with the link sent and successfully logs in |
|**Priority**| Low-Medium
