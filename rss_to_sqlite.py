import feedparser
import sqlite_utils

# RSS feed URL
FEED_URL = "https://nitter.net/LutfurRahmanTH/rss"

# SQLite database file
DATABASE_FILE = "data.db"

# Table name for storing RSS feed items
TABLE_NAME = "tweets"

# Connect to the SQLite database
db = sqlite_utils.Database(DATABASE_FILE)

# Create the table if it doesn't exist
db[table_name].create({"id": int, "title": str, "link": str}, pk="id", foreign_keys=[])

# Fetch the RSS feed
feed = feedparser.parse(FEED_URL)

# Upsert the latest records
for entry in feed.entries:
    record = {
        "id": int(entry.id),
        "title": entry.title,
        "link": entry.link
    }
    db[table_name].upsert(record, pk="id")

print("RSS feed upserted to SQLite successfully.")
