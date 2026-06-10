CREATE TABLE IF NOT EXISTS expenses(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date TEXT,
    merchant TEXT,
    amount REAL,
    category TEXT,
    source TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS goals(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    goal_name TEXT,
    target_amount REAL,
    saved_amount REAL,
    deadline TEXT
);

CREATE TABLE IF NOT EXISTS user_profile(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT,
    email TEXT,
    age INTEGER,
    occupation TEXT,
    monthly_income REAL,
    risk_level TEXT,
    primary_goal TEXT
);