insert into Board (name, description) values ('C_Chat', '姆咪');
insert into Board (name, description) values ('Sex', 'ii');
insert into Board (name, description) values ('Tobacco', '雲端抽煙');

insert into AdBoard (position, price) values ('left', 128);
insert into AdBoard (position, price) values ('middle', 256);
insert into AdBoard (position, price) values ('right', 512);

insert into User (picture,username, password, first_name, last_name, birthday, join_date, last_login, login_count, is_admin, is_active, profile) values (
    'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/apple/155/smiling-face-with-smiling-eyes-and-three-hearts_1f970.png','mango', '3345678', '姆咪', '陳', '2007-01-01 10:00:00', '2007-01-01 10:00:00', '2007-01-01 10:00:00', 0, 0, 1, "並沒有");
insert into User (picture, username, password, first_name, last_name, birthday, join_date, last_login, login_count, is_admin, is_active, profile) values (
    'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/mozilla/36/smiling-face-with-smiling-eyes_1f60a.png', 'splitline', '949487', '星爆', '李', '2008-01-01 10:00:00', '2008-01-01 10:00:00', '2008-01-01 10:00:00', 0, 0, 1, "我的名字不好唸 叫做康帕內魯拉");
insert into User (picture, username, password, first_name, last_name, birthday, join_date, last_login, login_count, is_admin, is_active, profile) values (
    'https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/emojione/151/smiling-face-with-smiling-eyes-and-three-hearts_1f970.png', 'Nanoda', 'japari', 'noda', 'Na', '2008-01-01 10:00:00', '2008-01-01 10:00:00', '2008-01-01 10:00:00', 1, 1, 1,"平成最後的nanoda");
insert into User (picture,tacobit,username, password, first_name, last_name, birthday, join_date, last_login, login_count, is_admin, is_active, profile) values (
    'https://pbs.twimg.com/profile_images/2370446440/6e2jwf7ztbr5t1yjq4c5_400x400.jpeg',10000,'hank5566', '2e8db3aceb4b0eb09d42bd545be707ece82981a09e728aa4616d4bdd0e3e11cc', 'Hank', 'Lu', '2008-01-01 10:00:00', '2008-01-01 10:00:00', '2008-01-01 10:00:00', 1, 1, 1,"喵喵叫每一天");
insert into User (picture,tacobit,username, password, first_name, last_name, birthday, join_date, last_login, login_count, is_admin, is_active, profile) values (
    'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQffpKD__eKLPR2piV-j1g7jochChQ2geX1KU63RDDgT1A1p3v6',10000,'mumi5566', '2e8db3aceb4b0eb09d42bd545be707ece82981a09e728aa4616d4bdd0e3e11cc', '姆咪騎士', 'Lu', '2008-01-01 10:00:00', '2008-01-01 10:00:00', '2008-01-01 10:00:00', 1, 1, 1,"我自己改就好");


insert into Post (content, author, board, like_count, dislike_count) values (
    '我喜歡喵喵', 4, 1, 1024, 16
);
insert into Post (content, author, board, like_count, dislike_count) values (
    '我不喜歡喵喵', 4, 1, 16, 1024
);

insert into Post (content, author, board, like_count, dislike_count) values ('艾喵喵', 2, 2, 11, 3);
insert into Post (content, author, board, like_count, dislike_count) values ('討厭喵喵', 2, 2, 12, 3);

insert into Comment (author, post, content) values (
    1, 1, 'ouo!!!'
);

insert into Comment (author, post, content) values (
    2, 1, 'qwq!!!'
);


insert into Following(user_no, following_no) values (4, 1);
insert into Following(user_no, following_no) values (4, 2);

insert into Following(user_no, following_no) values (2,4);
insert into Following(user_no, following_no) values (3,4);


insert into User (picture,username, password, first_name, last_name, birthday, join_date, last_login, login_count, is_admin, is_active, profile) values ('https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/emojione/151/thinking-face_1f914.png','apple1', '123456', 'apple', '1', '2007-01-01 10:00:00', '2007-01-01 10:00:00', '2007-01-01 10:00:00', 0, 0, 1, 'apple1');
insert into User (username, password, first_name, last_name, birthday, join_date, last_login, login_count, is_admin, is_active, profile) values ('apple2', '123456', 'apple', '2', '2007-01-01 10:00:00', '2007-01-01 10:00:00', '2007-01-01 10:00:00', 0, 0, 1, 'apple2');
insert into User (username, password, first_name, last_name, birthday, join_date, last_login, login_count, is_admin, is_active, profile) values ('apple3', '123456', 'apple', '3', '2007-01-01 10:00:00', '2007-01-01 10:00:00', '2007-01-01 10:00:00', 0, 0, 1, 'apple3');
insert into User (username, password, first_name, last_name, birthday, join_date, last_login, login_count, is_admin, is_active, profile) values ('apple4', '123456', 'apple', '4', '2007-01-01 10:00:00', '2007-01-01 10:00:00', '2007-01-01 10:00:00', 0, 0, 1, 'apple4');
insert into User (picture,username, password, first_name, last_name, birthday, join_date, last_login, login_count, is_admin, is_active, profile) values ('https://emojipedia-us.s3.dualstack.us-west-1.amazonaws.com/thumbs/240/samsung/148/face-with-stuck-out-tongue_1f61b.png','apple5', '123456', 'apple', '5', '2007-01-01 10:00:00', '2007-01-01 10:00:00', '2007-01-01 10:00:00', 0, 0, 1, 'apple5');

insert into Friendship(user_A, user_B, strength) values (4,2,222);
insert into Friendship(user_A, user_B, strength) values (4,3,40);
insert into Friendship(user_A, user_B, strength) values (4,1,170);
insert into Friendship(user_A, user_B, strength) values (4,5,5);
insert into Friendship(user_A, user_B, strength) values (4,9,120);