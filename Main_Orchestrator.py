from modules.url_detector import URLDetector

def main():
    print("Welcome to the Multi-Platform Auto Job Applier Orchestrator")
    print("-----------------------------------------------------------")
    
    # This orchestrator will eventually ingest a list of generic job URLs 
    # scraped from an aggregator and route them to explicit platform apply-bots.
    
    sample_urls = [
        "https://www.linkedin.com/jobs/view/123456",
        "https://www.stepstone.de/jobs/data-scientist",
        "https://boards.greenhouse.io/openai/jobs/123",
        "https://jobs.lever.co/example/123"
    ]
    
    detector = URLDetector()
    for job in sample_urls:
        detector.route_application(job)

if __name__ == "__main__":
    main()
