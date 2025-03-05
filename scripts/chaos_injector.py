"""
Simulates disruptions in the ICS environment or HPC to test the resilience of the overall system.
Use with caution in a staging or controlled environment.

Realistic assumptions:
- We have admin access to HPC device or ICS DMZ firewall
- We use shell commands or Azure CLI to degrade resources or block ports
"""

import subprocess
import time
import random

def degrade_hpc_resources(duration=60):
    """
    Example approach: artificially stress HPC device with a CPU or GPU stress tool.
    duration: how long in seconds to run the stress.
    """
    print(f"[Chaos] Degrading HPC resources for {duration}s using stress-ng...")
    # subprocess.run(["ssh", "jetson@192.168.1.10", "stress-ng --cpu 2 --timeout 60"])
    time.sleep(duration)
    print("[Chaos] HPC stress test ended.")

def block_dmz_port(duration=30):
    """
    Blocks ICS DMZ port (443 or 8443) for a certain duration to mimic a WAF or firewall meltdown.
    """
    port = 443
    print(f"[Chaos] Blocking ICS DMZ port {port} for {duration}s.")
    # Example iptables approach (on a test environment only)
    # subprocess.run(["sudo", "iptables", "-A", "INPUT", "-p", "tcp", "--dport", str(port), "-j", "DROP"])
    time.sleep(duration)
    # subprocess.run(["sudo", "iptables", "-D", "INPUT", "-p", "tcp", "--dport", str(port), "-j", "DROP"])
    print("[Chaos] Port block ended, restored normal traffic.")

def random_chaos_scenario():
    scenario = random.choice(["hpc_degrade", "dmz_block"])
    if scenario == "hpc_degrade":
        degrade_hpc_resources(duration=45)
    else:
        block_dmz_port(duration=30)

def main():
    print("[Chaos] Starting random chaos scenario...")
    random_chaos_scenario()
    print("[Chaos] Chaos scenario completed.")

if __name__ == "__main__":
    main()
