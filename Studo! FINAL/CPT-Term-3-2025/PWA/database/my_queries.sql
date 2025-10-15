
CREATE TABLE users (
  user_id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  email TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL
);

INSERT INTO users (first_name, email, password) 
VALUES ('Jing', 'jing@email.com', 'mypassword123');

SELECT * FROM users WHERE userID = '1';

SELECT * FROM users WHERE email = 'jing@gmail.com';

SELECT * FROM users 
WHERE username = 'jing123' AND password = 'mypassword123';

SELECT user_id, username, email FROM users WHERE username = 'jing123';


CREATE TABLE pomodoro_sessions (
    sessionID INTEGER PRIMARY KEY AUTOINCREMENT,
    userID INTEGER NOT NULL,
    start_time DATETIME NOT NULL,
    end_time DATETIME,
    session_type TEXT NOT NULL,
    completed BOOLEAN DEFAULT 0,
    FOREIGN KEY (userID) REFERENCES users(userID)
);
INSERT INTO pomodoro_sessions (userID, start_time, session_type) 
VALUES (1, CURRENT_TIMESTAMP, 'focus');
UPDATE pomodoro_sessions
SET end_time = CURRENT_TIMESTAMP, completed = 1
WHERE sessionID = 1;
SELECT * FROM pomodoro_sessions
WHERE userID = 1
ORDER BY start_time DESC;
SELECT COUNT(*) AS total_focus_sessions
FROM pomodoro_sessions
WHERE userID = 1 AND session_type = 'focus' AND completed = 1;
SELECT SUM(strftime('%s', end_time) - strftime('%s', start_time)) / 60 AS total_minutes
FROM pomodoro_sessions
WHERE userID = 1 AND session_type = 'focus' AND completed = 1;


