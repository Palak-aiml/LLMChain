import unittest
import os
from llmchain.monitoring.experiment.experiment_tracker import ExperimentTracker
from llmchain.monitoring.experiment.debugger import Debugger

class TestExperimentTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = ExperimentTracker(log_dir="test_experiments")
        if not os.path.exists("test_experiments"):
            os.makedirs("test_experiments")

    def tearDown(self):
        for f in os.listdir("test_experiments"):
            os.remove(os.path.join("test_experiments", f))
        os.rmdir("test_experiments")

    def test_run_lifecycle(self):
        run_id = self.tracker.start_run(run_name="testrun", params={"lr":0.01})
        self.tracker.log_metric("accuracy", 0.95)
        self.tracker.log_artifact("model.pt")
        self.tracker.end_run()
        files = os.listdir("test_experiments")
        self.assertTrue(any("testrun.json" in f for f in files))

class TestDebugger(unittest.TestCase):
    def setUp(self):
        self.log_file = "test_debug.log"
        if os.path.exists(self.log_file):
            os.remove(self.log_file)
        self.debugger = Debugger(log_file=self.log_file)

    def tearDown(self):
        if os.path.exists(self.log_file):
            os.remove(self.log_file)

    def test_log_step(self):
        self.debugger.log_step("step1", {"input":1}, {"output":2})
        self.debugger.log_step("step2", {"input":2}, error="fail")
        with open(self.log_file) as f:
            logs = f.read()
        self.assertIn("step1", logs)
        self.assertIn("step2", logs)
        self.assertIn("fail", logs)

if __name__ == "__main__":
    unittest.main()
