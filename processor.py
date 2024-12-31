# run_serial_parallel.py
import subprocess
import time
import threading

def run_script(script_name):
    """Run the script and capture the output."""
    start_time = time.time()
    process = subprocess.Popen(['python', script_name], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()  # Capture output and errors
    end_time = time.time()
    execution_time = end_time - start_time
    
    
    if process.returncode == 0:
        return stdout.decode()
    else:
        return stderr.decode()

# Serial Execution
def run_serial_execution(scripts):
    """Run scripts serially."""
    total_start_time = time.time()
    for script in scripts:
        
        print(run_script(script))
    total_end_time = time.time()
    return total_end_time - total_start_time

# Parallel Execution
def run_parallel_execution(scripts):
    """Run scripts in parallel using threads."""
    total_start_time = time.time()
    
    # Run each script in a separate thread
    threads = []
    for script in scripts:
        thread = threading.Thread(target=run_script, args=(script,))
        threads.append(thread)
        thread.start()
    
    # Wait for all threads to finish
    for thread in threads:
        thread.join()

    total_end_time = time.time()
    return total_end_time - total_start_time

# List of Python scripts to run
scripts_to_run = ['test2.py', 'translate.py']

if __name__ == "__main__":
    print("Starting Serial Execution...\n")
    serial_time = run_serial_execution(scripts_to_run)
    print(f"Serial execution total time: {serial_time:.2f} seconds")
    
    print("\nStarting Parallel Execution...\n")
    parallel_time = run_parallel_execution(scripts_to_run)
    print(f"Parallel execution total time: {parallel_time:.2f} seconds")
