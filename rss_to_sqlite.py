from feed_to_sqlite import ingest_feed

ingest_feed(db="data.db", url="https://nitter.net/lutfurrahmanth/rss", table_name="lutfur_tweets")

print("RSS feed upserted to SQLite successfully.")
