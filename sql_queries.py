# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS songplays;"
user_table_drop = "DROP TABLE IF EXISTS users;"
song_table_drop = "DROP TABLE IF EXISTS songs;"
artist_table_drop = "DROP TABLE IF EXISTS artists;"
time_table_drop = "DROP TABLE IF EXISTS time;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE songplays (
    songplay_id serial primary key, 
    start_time timestamp, 
    user_id int, 
    level varchar(10), 
    song_id varchar, 
    artist_id varchar, 
    session_id int, 
    location varchar(50), 
    user_agent varchar
);
""")

user_table_create = ("""
CREATE TABLE users (
    user_id int,
    first_name varchar(50), 
    last_name varchar(50), 
    gender varchar(1), 
    level varchar(10)
);
""")

song_table_create = ("""
CREATE TABLE songs (
    song_id varchar, 
    title varchar, 
    artist_id varchar, 
    year int, 
    duration numeric
);
""")

artist_table_create = ("""
CREATE TABLE artists (
    artist_id varchar, 
    name varchar, 
    location varchar(50), 
    latitude numeric, 
    longitude numeric
);
""")

time_table_create = ("""
CREATE TABLE time (
    start_time timestamp, 
    hour int, 
    day int, 
    week int, 
    month int, 
    year int, 
    weekday int
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
INSERT INTO songplays(start_time, user_id, level, song_id, artist_id, session_id, location, user_agent) 
VALUES(%s, %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
INSERT INTO users VALUES(%s, %s, %s, %s, %s);
""")

song_table_insert = ("""
INSERT INTO songs VALUES(%s, %s, %s, %s, %s);
""")

artist_table_insert = ("""
INSERT INTO artists VALUES(%s, %s, %s, %s, %s);
""")


time_table_insert = ("""
INSERT INTO time VALUES(%s, %s, %s, %s, %s, %s, %s);
""")

# FIND SONGS

song_select = ("""
SELECT 
    l.song_id,
    l.artist_id
FROM 
    songs l
JOIN
    artists r 
ON
    l.artist_id = r.artist_id
WHERE
    l.title = %s
    AND
    l.duration = %s
    AND
    r.name = %s
;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]