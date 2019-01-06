CREATE TABLE IF NOT EXISTS Board (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text,
    description text
);
CREATE TABLE IF NOT EXISTS User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    picture text default 'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/lg/57/thinking-face_1f914.png',
    username text,
    password text,
    first_name text,
    last_name text,
    birthday datetime,
    join_date datetime default current_timestamp,
    last_login datetime default current_timestamp,
    login_count INTEGER,
    is_admin BOOLEAN,
    is_active BOOLEAN,
    profile text,
    tacobit INTEGER default 0
);
CREATE TABLE IF NOT EXISTS Post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content text,
    publish_date datetime default current_timestamp,
    last_modify datetime default current_timestamp,
    like_count INTEGER default 0,
    dislike_count INTEGER default 0,
    author INTEGER,
    board INTEGER,
    FOREIGN KEY (author)  REFERENCES User(id),
    FOREIGN KEY (board)  REFERENCES Board(id)
);
CREATE TABLE IF NOT EXISTS Comment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author INTEGER,
    post INTEGER,
    last_modify datetime default current_timestamp,
    publish_date datetime default current_timestamp,
    content text,
    FOREIGN KEY (author)  REFERENCES User(id),
    FOREIGN KEY (post)  REFERENCES Post(id)
);
CREATE TABLE IF NOT EXISTS Following (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_no INTEGER,
    following_no INTEGER,
    FOREIGN KEY (user_no)  REFERENCES User(id),
    FOREIGN KEY (following_no)  REFERENCES User(id)
);
CREATE TABLE IF NOT EXISTS Friendship (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_A INTEGER,
    user_B INTEGER,
    strength INTEGER default 0,
    FOREIGN KEY (user_A)  REFERENCES User(id),
    FOREIGN KEY (user_B)  REFERENCES User(id)
);
CREATE TABLE IF NOT EXISTS Bucket_list (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    board_no INTEGER,
    user_no INTEGER,
    FOREIGN KEY (board_no)  REFERENCES Board(id),
    FOREIGN KEY (user_no)  REFERENCES User(id)
);
CREATE TABLE IF NOT EXISTS Who_likes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_no INTEGER,
    like_no INTEGER,
    FOREIGN KEY (user_no)  REFERENCES User(id),
    FOREIGN KEY (like_no)  REFERENCES User(id)
);
CREATE TABLE IF NOT EXISTS Who_dislikes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_no INTEGER,
    dislike_no INTEGER,
    FOREIGN KEY (user_no)  REFERENCES User(id),
    FOREIGN KEY (dislike_no)  REFERENCES User(id)
);
CREATE TABLE IF NOT EXISTS AdBoard (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    position text,
    width INTEGER default 0,
    height INTEGER default 0,
    price INTEGER default 0
);
CREATE TABLE IF NOT EXISTS Ad (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad text,
    URL text,
    start_date datetime,
    end_date datetime,
    poster INTEGER,
    board INTEGER,
    FOREIGN KEY (poster)  REFERENCES User(id),
    FOREIGN KEY (board)  REFERENCES AdBoard(id)
);

CREATE TABLE IF NOT EXISTS Notifications (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    notified_date datetime default current_timestamp,
    link text,
    content text,
    has_read BOOLEAN default 0,
    user INTEGER,
    FOREIGN KEY (user) REFERENCES User(id)
);
