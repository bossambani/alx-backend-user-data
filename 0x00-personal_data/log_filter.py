import logging
import re

#Define a log filter to mask PII fields
class PIIObfuscationFilter(logging.Filter):
    def filter(self, record):
        #Mask sensitive data like emails, SSNs, and credit card numbers
        record.msg = self.mask_pii(record.msg)
        return True
    
    def mask_pii(self, msg):
        # Mask email addresses
        msg = re.sub(r'([a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,})', '[EMAIL MASKED]', msg)
        # Mask Social Security Numbers
        msg = re.sub(r'\d{3}-\d{2}-\d{4}', '[SSN MASKED]', msg)
        # Mask credit card numbers
        msg = re.sub(r'\d{4} \d{4} \d{4} \d{4}', '[CREDIT CARD MASKED]', msg)
        return msg

# Set up the logger with the custom filter
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

# Add a StreamHandler to output logs to the console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)

# Add the PII obfuscation filter to the console handler
log_filter = PIIObfuscationFilter()
console_handler.addFilter(log_filter)

# Add the handler to the logger
logger.addHandler(console_handler)

# Log test messages
logger.info("User John Doe with email john.doe@example.com logged in")
logger.info("SSN: 123-45-6789, Credit Card 4111 1111 1111 1111")