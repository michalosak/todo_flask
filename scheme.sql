drop table if exists "todo_items";
CREATE TABLE "todo_items" (
	`ID`	INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
	`item_title`	TEXT,
	`status`	INTEGER
)