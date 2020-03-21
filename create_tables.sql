create table if not exists twitter.corona (
	id bigint primary key,
	created_at timestamp,
	lang varchar(5),
	raw_json json
);

CREATE INDEX ON twitter.corona (id);

create table if not exists twitter.nyc (
	id bigint primary key,
	created_at timestamp,
	lang varchar(5),
	raw_json json
);

CREATE INDEX ON twitter.nyc (id);