# Covert date column with mixed date formats to a single date format
# Pandas 2.0.0+
data["date"] = pd.to_datetime(data["date"], format="mixed")
# Older versions of Pandas
data["date"] = pd.to_datetime(data["date"], errors="coerce")
