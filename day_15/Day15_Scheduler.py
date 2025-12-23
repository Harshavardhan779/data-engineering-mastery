import random 
import logging
import time

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(message)s')
def mock_etl_job():
    """Simulates an ETL job that sometimes fails."""
    logging.info("🚀 Starting ETL Job...")
    time.sleep(1) # Simulate work
    
    # Simulate a random 20% chance of failure
    if random.random() < 0.2:
        raise Exception("Database Connection Timeout!")
    
    logging.info("✅ ETL Job Completed Successfully.")
def run_scheduler(iterations=5):
    """Runs the job periodically and handles retries."""
    print("🕰️ Scheduler Started (Simulating Airflow)...")
    
    for i in range(1, iterations + 1):
        print(f"\n--- Cycle {i} ---")
        try:
            mock_etl_job()
        except Exception as e:
            logging.error(f"❌ Job Failed: {e}")
            logging.info("🔄 Retrying immediately...")
            # Simple Retry Logic
            try:
                mock_etl_job()
            except:
                logging.critical("💀 Retry Failed. Sending Alert to Engineer.")
        
        # Wait for 3 seconds before next run
        time.sleep(3)

if __name__ == "__main__":
    run_scheduler()    

