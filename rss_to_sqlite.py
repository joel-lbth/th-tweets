from feed_to_sqlite import ingest_feed
import ssl

ssl._create_default_https_context = ssl._create_unverified_context

ingest_feed(db="data.db", url="https://nitter.net/lutfurrahmanth/rss", table_name="lutfur_tweets")

print("RSS feed upserted to SQLite successfully.")
