-- 운영 프로 테이블을 생성합니다.
CREATE TABLE admin_pro (
  id integer primary key,
  name text,
  phone_num text,
  campus_region integer,
  class integer,
  team integer
);

-- 교육생 테이블을 생성합니다.
CREATE TABLE student (
  id integer primary key,
  name text,
  phone_num text,
  campus_region integer,
  borrowed_book integer,
  project integer
);

-- 교보재 테이블을 생성합니다.
CREATE TABLE book (
  id integer primary key,
  student_id integer,
  title text,
  buy_at date,
  borrow date,
  return date,
  FOREIGN KEY(student_id) REFERENCES student(id)
);

-- 캠퍼스 지역 테이블을 생성합니다.
CREATE TABLE campus_region (
  id integer primary key,
  name text,
  admin_pro_id integer REFERENCES admin_pro(id),
  student_id integer REFERENCES student(id)
);

-- 프로젝트 테이블을 생성합니다.
CREATE TABLE project (
  id int primary key,
  title text,
  student integer REFERENCES student(id) ,
  admin_pro integer REFERENCES student(id)
);

-- 운영프로 테이블에 요소를 추가합니다.
insert into admin_pro (name, phone_num, campus_region, class, team)
values ('장재영', '010-1234-1234', 1, 1, 1);

-- 캠퍼스 지역 테이블에 요소를 추가합니다.
INSERT INTO campus_region (name)
VALUES ('서울');

-- 학생 테이블에 요소를 추가합니다.
insert into student (name, phone_num, campus_region)
values ('김우석', '010-1234-1234', 1);

-- 교보재 테이블에 요소를 추가합니다.
insert into book (title, buy_at, borrow, return, student_id)
values ('싸피7기', '2016-03-31', '2022-03-01', '2022-04-01', 1);