from db_manage import db_init, sql_read_metrics
from functions import get_urls_metrics

# Create db, table and conection
con = db_init()
# Get metrics from Google Pages Speed API
get_urls_metrics(con)

print('SQL Read')
# Print SQLite table with results
sql_read_metrics(con)