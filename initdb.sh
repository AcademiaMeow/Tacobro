rm tacobro.db
(sqlite3 tacobro.db < create_table.sql
    && sqlite3 tacobro.db < test_data.sql)
