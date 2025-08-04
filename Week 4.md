# Week 4 - Data flow of app
## Data flow
| **Data**       | **Details**                                                                 |
|-----------------|---------------------------------------------------------------------------------|
| **Inputs**      | - name<br>- email<br>- password<br>- reCAPTCHA (human verification)            |
| **Data Flow**   | 1. user fills in form fields<br>2. clicks submit<br>3. reCAPTCHA is verified    |
|                 | 4. if reCAPTCHA fails -> redirect to error message (reCAPTCHA)                             |
|                 | 5. if email is invalid -> redirect to error message (email)                                          |
|                 | 6. if all valid -> save name/email/password to online database                  |
|                 | 7. redirect to clock page                                                      |
|                 | 8. show confirmation of account details via a popup                              |
| **Output**      | if successful: `"Account created!"` (shown as popup on clock page)<br> if failed: appropriate error message (eg. `invalid email or failed reCAPTCHA`) |

## Test case
| **Test case** | #1 |
|------------------|--------|
| **component/data**    | user registration form |
| **purpose**      | to check for a sucessful account creation when passing  |
| **inputs**       | -  ame: Jing<br>- Email: jingwen.cheng@education.nsw.gov.au<br>- Password: ihateanne!<br>- reCAPTCHA: passed |
| **expected out** | - redirects to clock<br>- popup message: `Account created!`<br>- user data then is saved to database |
| **written output**   | matched expected output (which is basically a pass)|
| **pass or fail?**       | pass |
