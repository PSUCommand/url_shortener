create table if not exists links (
  id integer primary key autoincrement,
  short_link string not null,
  long_link string not null
);