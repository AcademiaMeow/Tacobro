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


insert into Board (name, description) values ('C_Chat', '姆咪');
insert into Board (name, description) values ('Sex', 'ii');
insert into Board (name, description) values ('Tobacco', '雲端抽煙');


insert into User (username, password, first_name, last_name, birthday, join_date, last_login, login_count, is_admin, is_active, profile) values (
    '陳姆咪', '3345678', '姆咪', '陳', '2007-01-01 10:00:00', '2007-01-01 10:00:00', '2007-01-01 10:00:00', 0, 0, 1, "並沒有");
insert into User (username, password, first_name, last_name, birthday, join_date, last_login, login_count, is_admin, is_active, profile) values (
    '李星爆', '949487', '星爆', '李', '2008-01-01 10:00:00', '2008-01-01 10:00:00', '2008-01-01 10:00:00', 0, 0, 1, "我的名字不好唸 叫做康帕內魯拉");
insert into User (username, password, first_name, last_name, birthday, join_date, last_login, login_count, is_admin, is_active, profile) values (
    'Nanoda', 'japari', 'noda', 'Na', '2008-01-01 10:00:00', '2008-01-01 10:00:00', '2008-01-01 10:00:00', 1, 1, 1,"平成最後的nanoda");
insert into User (username, password, first_name, last_name, birthday, join_date, last_login, login_count, is_admin, is_active, profile) values (
    'hank5566', 'japari', 'Hank', 'Lu', '2008-01-01 10:00:00', '2008-01-01 10:00:00', '2008-01-01 10:00:00', 1, 1, 1,"喵喵叫每一天");

insert into Post (content, author, board) values ('我喜歡喵喵', 4, 1);
insert into Post (content, author, board) values ('我不喜歡喵喵', 4, 1);

insert into Post (content, author, board) values ('艾喵喵', 2, 2);
insert into Post (content, author, board) values ('討厭喵喵', 2, 2);

insert into Following(user_no, following_no) values (4, 1);
insert into Following(user_no, following_no) values (4, 2);

insert into Following(user_no, following_no) values (2,4);
insert into Following(user_no, following_no) values (3,4);