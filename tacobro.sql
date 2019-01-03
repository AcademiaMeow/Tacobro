CREATE TABLE Board (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name text,
    description text
);
CREATE TABLE User (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    picture text,
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
    profile text
);
CREATE TABLE Post (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    content text,
    publish_date datetime default current_timestamp,
    last_modify datetime default current_timestamp,
    like_count INTEGER,
    dislike_count INTEGER,
    author INTEGER,
    board INTEGER,
    FOREIGN KEY (author)  REFERENCES User(id),
    FOREIGN KEY (board)  REFERENCES Board(id)
);
CREATE TABLE Comment (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author INTEGER,
    post INTEGER,
    last_modify datetime default current_timestamp,
    publish_date datetime default current_timestamp,
    content text,
    FOREIGN KEY (author)  REFERENCES User(id),
    FOREIGN KEY (post)  REFERENCES Post(id)
);
CREATE TABLE Follower (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_no INTEGER,
    follower_no INTEGER,
    FOREIGN KEY (user_no)  REFERENCES User(id),
    FOREIGN KEY (follower_no)  REFERENCES User(id)
);
CREATE TABLE Following (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_no INTEGER,
    following_no INTEGER,
    FOREIGN KEY (user_no)  REFERENCES User(id),
    FOREIGN KEY (following_no)  REFERENCES User(id)
);
CREATE TABLE Bucket_list (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    board_no INTEGER,
    user_no INTEGER,
    FOREIGN KEY (board_no)  REFERENCES Board(id),
    FOREIGN KEY (user_no)  REFERENCES User(id)
);
CREATE TABLE Who_likes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_no INTEGER,
    like_no INTEGER,
    FOREIGN KEY (user_no)  REFERENCES User(id),
    FOREIGN KEY (like_no)  REFERENCES User(id)
);
CREATE TABLE Who_dislikes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_no INTEGER,
    dislike_no INTEGER,
    FOREIGN KEY (user_no)  REFERENCES User(id),
    FOREIGN KEY (dislike_no)  REFERENCES User(id)
);
CREATE TABLE AdBoard (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    position text,
    width INTEGER,
    height INTEGER,
    price INTEGER
);
CREATE TABLE Ad (
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
