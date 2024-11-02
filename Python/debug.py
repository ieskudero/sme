# ---------------------------------for debugging only. remove on production---------------------------------
import debugpy

debugpy.listen(("0.0.0.0", 5678))  # Start the debug server on port 5678
print("Waiting for debugger attach...")
debugpy.wait_for_client()  # Pause the execution until the debugger is attached
# ---------------------------------for debugging only. remove on production---------------------------------


# import module to debug
import discretize_test