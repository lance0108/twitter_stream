create table if not exists twitter.corona (
	id bigint primary key,
	created_at timestamp,
	lang varchar(5),
	raw_json json
);

CREATE INDEX ON twitter.corona (id);
CREATE INDEX ON twitter.corona (created_at);
CREATE INDEX ON twitter.corona (lang);

create table if not exists twitter.nyc (
	id bigint primary key,
	created_at timestamp,
	lang varchar(5),
	raw_json json
);

CREATE INDEX ON twitter.nyc (id);
CREATE INDEX ON twitter.nyc (created_at);
CREATE INDEX ON twitter.nyc (lang);

create table if not exists twitter.chicago (
	id bigint primary key,
	created_at timestamp,
	lang varchar(5),
	raw_json json
);

CREATE INDEX ON twitter.chicago (id);
CREATE INDEX ON twitter.chicago (created_at);
CREATE INDEX ON twitter.chicago (lang);