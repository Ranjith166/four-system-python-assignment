import json, os, tempfile, sqlite3
from pathlib import Path

def atomic_json(path, data):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, tmp = tempfile.mkstemp(prefix=path.name, dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
            f.flush()
            os.fsync(f.fileno())
        os.replace(tmp, path)
    finally:
        if os.path.exists(tmp):
            os.unlink(tmp)

def initialize_warm_db(path):
    with sqlite3.connect(path) as db:
        db.execute("CREATE TABLE IF NOT EXISTS defects (defect_id TEXT PRIMARY KEY, timestamp TEXT, severity TEXT, description TEXT, defect_hash TEXT)")
        db.execute("CREATE INDEX IF NOT EXISTS idx_defects_timestamp ON defects(timestamp)")

def defects_since(path, cutoff):
    with sqlite3.connect(path) as db:
        return db.execute("SELECT * FROM defects WHERE timestamp >= ? ORDER BY timestamp", (cutoff,)).fetchall()
