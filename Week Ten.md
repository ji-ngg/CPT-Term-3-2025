## Adding Interactivity (cont.)
Continuing from last week, I started adding buttons and other interactive elements into my website. However, I didn't get as far as what I had hoped because I went on vacation :(

I caught up on week ten work and when I tested my website it was all working fine - during the holidays I will refine my CSS and make sure everything is to design. Currently, my website is looking like the default one that was provided but different layout and not to my plan. 

To do during holidays:
Refine CSS
Change all the font colours to what was on layout
Add the images
Import sound and background music -> code into the website
Set up log in & sign up database and code

## **Work during the holidays**
During the holidays, I created the log in and sign up page as well as set up the SQL database. I then linked this to my `data_source.db` and `my_queries.sql` where examples of user's data is shown below:
<img width="852" height="148" alt="Screenshot 2025-10-14 at 4 10 02 pm" src="https://github.com/user-attachments/assets/5320950a-9429-43a2-a54d-7e194b3a5a9b" />

Studo will save the user's saved preferences for background sound and music, as well as their preferred background (which I have edited from the original plan to just different pastel colours since having high quality normal pictures will interfere with the readability of the text on page).

I've also finalised and shortened my code for my CSS styling of the website (shown below)
````
:root{
  --surround:#c0cfd8;
  --main-bg:#edf2f4;
  --accent:#2b2b2b;
  --card-bg:#ffffff;
  --muted:#6b7a86;
}
html,body{height:100%;margin:0;font-family: Inter, system-ui, -apple-system, 'Segoe UI', Roboto, Arial; background:var(--main-bg); color:var(--accent);}
.app{display:flex;min-height:100vh;}
.sidebar{width:220px;background:var(--surround);padding:18px;box-sizing:border-box;display:flex;flex-direction:column;justify-content:space-between;border-right:1px solid rgba(0,0,0,0.06)}
.logo img{width:48px;height:48px;border-radius:6px;display:block}
.brand{font-weight:700;margin-top:6px}
nav{margin-top:20px}
.navlink{display:block;padding:8px 10px;color:inherit;text-decoration:none;border-radius:6px;margin-bottom:8px}
.navlink:hover{background:rgba(0,0,0,0.06)}
.sidebar-bottom{width:100%}
.btn{background:#2f4858;color:#fff;padding:8px 12px;border-radius:10px;border:none;cursor:pointer}
.btn.small{background:#3b5666;padding:6px 8px;margin-top:8px}
.auth-card{width:380px;margin:60px auto;padding:22px;border-radius:12px;background:var(--card-bg);box-shadow:0 8px 20px rgba(0,0,0,0.12)}
.error{color:#a33;background:#ffecec;padding:8px;border-radius:8px;margin-bottom:10px}
label{display:block;margin-bottom:10px}
input[type="text"], input[type="email"], input[type="password"], textarea, select {width:100%;padding:10px;border-radius:8px;border:1px solid #ddd;box-sizing:border-box}
.show-pass{font-size:13px;color:var(--muted)}
.center-card{margin:40px auto;padding:30px;border-radius:12px;background:var(--card-bg);min-width:400px;max-width:760px;text-align:center;box-shadow:0 8px 24px rgba(0,0,0,0.12)}
.time-large{font-size:72px;font-weight:800;letter-spacing:1px}
.motivate{margin-top:12px;color:var(--muted);font-weight:600}
.quote{font-weight:700;color:var(--muted);margin-bottom:18px}
.popup{position:fixed;right:40px;bottom:40px;width:420px;padding:18px;background:#20232a;color:#fff;border-radius:12px;box-shadow:0 8px 40px rgba(0,0,0,0.5)}
.popup .close{position:absolute;right:10px;top:6px;background:transparent;border:0;color:#fff;font-size:22px}
.option-grid{display:flex;flex-wrap:wrap;gap:8px}
.option-grid button{padding:8px 12px;border-radius:8px;border:0;background:#333;color:#fff;cursor:pointer}
.option-grid .bg-option{width:80px;height:40px;border-radius:8px;border:2px solid rgba(255,255,255,0.06)}
.actions{margin-top:12px;text-align:right}
````
