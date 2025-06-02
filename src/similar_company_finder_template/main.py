#!/usr/bin/env python
import sys
import os
import logging
from dotenv import load_dotenv

from similar_company_finder_template.crew import SimilarCompanyFinderTemplateCrew

# Load environment variables
load_dotenv()

# Configure logging
logging.basicConfig(
    level=getattr(logging, os.getenv('LOG_LEVEL', 'INFO')),
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# This main file is intended to be a way for your to run your
# crew locally, so refrain from adding necessary logic into this file.
# Replace with inputs you want to test with, it will automatically
# interpolate any tasks and agents information


def run():
    """
    Run the crew with production-ready error handling.
    """
    try:
        # Validate required environment variables
        if not os.getenv('ANTHROPIC_API_KEY'):
            raise ValueError("ANTHROPIC_API_KEY environment variable is required")
        
        # Get inputs from environment variables or use defaults
        target_company = os.getenv('TARGET_COMPANY', '<Placeholder Company>')
        our_product = os.getenv('OUR_PRODUCT', '<Placeholder Product>')
        
        inputs = {
            "target_company": target_company,
            "our_product": our_product,
        }
        
        logger.info(f"Starting crew execution with target_company: {target_company}")
        logger.info(f"Our product: {our_product}")
        
        result = SimilarCompanyFinderTemplateCrew().crew().kickoff(inputs=inputs)
        
        logger.info("Crew execution completed successfully")
        return result
        
    except Exception as e:
        logger.error(f"An error occurred while running the crew: {e}")
        raise


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        SimilarCompanyFinderTemplateCrew().crew().train(
            n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        SimilarCompanyFinderTemplateCrew().crew().replay(task_id=sys.argv[1])

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {"topic": "AI LLMs"}
    try:
        SimilarCompanyFinderTemplateCrew().crew().test(
            n_iterations=int(sys.argv[1]), openai_model_name=sys.argv[2], inputs=inputs
        )

    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")
