CREATE DATABASE IF NOT EXISTS url_shortener;

CREATE TABLE IF NOT EXISTS url_shortener.links (
	id INT UNSIGNED auto_increment NOT NULL,
	original TEXT NOT NULL,
	shortened VARCHAR(100) NOT NULL,
	CONSTRAINT links_PK PRIMARY KEY (ID),
	CONSTRAINT links_UN UNIQUE KEY (shortened)
)
ENGINE=InnoDB
DEFAULT CHARSET=utf8
COLLATE=utf8_general_ci
COMMENT='Table to store original and shortened links';
