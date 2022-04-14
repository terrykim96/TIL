CREATE TABLE "posts_comment" (
  "id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, 
  "content" text NOT NULL, 
  "post_id" integer NOT NULL REFERENCES 
  "posts_post" ("id") DEFERRABLE INITIALLY DEFERRED
);

