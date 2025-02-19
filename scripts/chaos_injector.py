  #!/usr/bin/env python3
"""
chaos_injector.py
-----------------
Script to simulate failures in the HPC and ICS systems.
Used for stress testing and resilience verification.
"""

import random
import time
from src.utils.logger import get_logger

logger = get_logger(__name__)

def simulate_ics_outage(duration=5):
    logger.warning("Simulating ICS outage...")
    time.sleep(duration)
    logger.info("ICS outage simulation complete.")

def simulate_hpc_failure():
    failure_modes = ["overheating", "network disconnect", "GPU fault"]
    mode = random.choice(failure_modes)
    logger.error(f"Simulated HPC failure mode: {mode}")
    return mode

if __name__ == "__main__":
    simulate_ics_outage()
    simulate_hpc_failure()
