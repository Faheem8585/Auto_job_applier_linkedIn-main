import re
from urllib.parse import urlparse

class URLDetector:
    """
    Detects the recruitment platform or Application Tracking System (ATS)
    based on the provided job URL.
    """
    
    @staticmethod
    def identify_platform(url: str) -> str:
        parsed_url = urlparse(url)
        domain = parsed_url.netloc.lower()
        
        if "linkedin.com" in domain:
            return "linkedin"
        elif "stepstone." in domain:
            return "stepstone"
        elif "glassdoor." in domain:
            return "glassdoor"
        elif "boards.greenhouse.io" in domain:
            return "greenhouse"
        elif "jobs.lever.co" in domain:
            return "lever"
        elif "myworkdayjobs.com" in domain:
            return "workday"
        else:
            return "unknown_direct"

    @staticmethod
    def route_application(url: str):
        platform = URLDetector.identify_platform(url)
        print(f"[Orchestrator] Detected platform: {platform.upper()} for URL: {url}")
        
        # Routing logic placeholder for when specific adapters are built
        if platform == "linkedin":
            print("=> Routing to specialized LinkedIn Adapter...")
            # run_linkedin_bot(url)
        elif platform == "stepstone":
            print("=> Routing to specialized Stepstone Adapter...")
            # run_stepstone_bot(url)
        elif platform == "glassdoor":
            print("=> Routing to specialized Glassdoor Adapter...")
            # run_glassdoor_bot(url)
        elif platform == "greenhouse" or platform == "lever":
            print("=> Routing to direct ATS Adapter...")
            # run_ats_bot(url)
        else:
            print(f"=> Unsupported platform domain: {domain}")

# Example Integration:
# detector = URLDetector()
# detector.route_application("https://www.stepstone.de/jobs/machine-learning-engineer")
