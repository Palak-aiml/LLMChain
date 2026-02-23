"""
Experiment Tracker: Logs runs, parameters, metrics, and artifacts for chains/agents.
"""
import os
import json
import uuid
from datetime import datetime

class ExperimentTracker:
    def __init__(self, log_dir="experiments"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

    def start_run(self, run_name=None, params=None):
        self.run_id = str(uuid.uuid4())
        self.run_name = run_name or f"run_{self.run_id}"
        self.start_time = datetime.utcnow().isoformat()
        self.params = params or {}
        self.metrics = {}
        self.artifacts = []
        self._log_metadata()
        return self.run_id

    def log_metric(self, key, value):
        self.metrics[key] = value
        self._log_metadata()

    def log_artifact(self, file_path):
        self.artifacts.append(file_path)
        self._log_metadata()

    def end_run(self):
        self.end_time = datetime.utcnow().isoformat()
        self._log_metadata(final=True)

    def _log_metadata(self, final=False):
        meta = {
            "run_id": self.run_id,
            "run_name": self.run_name,
            "start_time": self.start_time,
            "end_time": getattr(self, "end_time", None),
            "params": self.params,
            "metrics": self.metrics,
            "artifacts": self.artifacts,
        }
        fname = f"{self.run_name}.json"
        with open(os.path.join(self.log_dir, fname), "w") as f:
            json.dump(meta, f, indent=2)
