"""
Simple Debugger: Logs chain/agent steps, inputs, outputs, and errors for debugging.
"""
import logging

class Debugger:
    def __init__(self, log_file="debug.log"):
        self.logger = logging.getLogger("LLMChainDebugger")
        self.logger.setLevel(logging.DEBUG)
        fh = logging.FileHandler(log_file)
        fh.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        if not self.logger.handlers:
            self.logger.addHandler(fh)

    def log_step(self, step_name, input_data, output_data=None, error=None):
        msg = f"Step: {step_name} | Input: {input_data}"
        if output_data is not None:
            msg += f" | Output: {output_data}"
        if error is not None:
            msg += f" | Error: {error}"
        self.logger.info(msg)
