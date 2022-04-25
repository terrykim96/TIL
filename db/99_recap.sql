/*

  (1) DB 목록을 확인하는 명령어
  => .databases

  (2) 테이블 목록을 확인하는 명령어
  => .tables

  (3) CSV 파일 불러오는 명령어
  => .mode csv
  => .import 파일명.csv 테이블명

  ex) .import users.csv users_user

  (4) help
  => .help

  (5) 터미널 지우는 명령어
  => .shell clear

*/

-- (1) 테이블 생성 (DDL)

CREATE TABLE 테이블명 (
  column1 datatype constraint,
  column2 datatype constraint,
);

CREATE TABLE Article (
  id INTEGER PRIMARY KEY,
  title TEXT NOT NULL,
  content TEXT NOT NULL
);

-- (2) 테이블 삭제 (DROP)
-- (주의) 한 번 삭제된 테이블은 되돌릴 수 없습니다.
DROP TABLE Article;

-- (3) 데이터 생성 (INSERT)
INSERT INTO 테이블명 (column1, column2, ...)
VALUES(value1, value2);

INSERT INTO Article (title, content)
VALUES('제목1', '내용1');

-- (4) 데이터 조회 (SELECT)

-- (4-1) 모든 컬럼 조회하기
SELECT *FROM Article;

-- (4-2) 특정 컬럼 조회하기
SELECT title FROM Article;

-- (4-3) 원하는 개수만큼 가져오기
SELECT * FROM Article LIMIT 1;

-- (4-4) 특정 위치에서부터 가져올 때
INSERT INTO Article (title, content)
VALUES
('제목2', '내용2'),
('제목3', '내용3'),
('제목4', '내용4'),
('제목5', '내용5');

SELECT *
FROM Article
LIMIT 1 OFFSET 1;