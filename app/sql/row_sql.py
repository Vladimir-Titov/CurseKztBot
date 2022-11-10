create_table = '''
    CREATE TABLE IF NOT EXISTS curs_by_date(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    curs real,
    сurs_date TEXT DEFAULT (datetime('now'))
);
'''

insert_query = '''
insert into curs_by_date(curs) values (?);
'''

select_5 = '''
select * from curs_by_date order by сurs_date desc limit 5;
'''

select_all = '''
select * from curs_by_date order by сurs_date desc;
'''