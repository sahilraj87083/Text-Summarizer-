import os
from Textsummarizer.logging import logger
from Textsummarizer.entity import DataValidationConfig


class DataValidation:
    def __init__(self, config:DataValidationConfig):
        self.config = config

    def validate_all_files_exist(self)->bool:
        try:
            logger.info("Starting all files validation")
            validation_status = None

            all_files = os.listdir(os.path.join("artifacts","data","samsum_dataset"))

            for file in all_files:
                if file in self.config.ALL_REQUIRED_FILES:
                    logger.info(f"Required file {file} is present")
                    validation_status = True
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"validation_status : {validation_status}")
                else:
                    logger.info(f"Required file {file} is missing")
                    validation_status = False
                    with open(self.config.STATUS_FILE, 'w') as f:
                        f.write(f"validation_status : {validation_status}")
            
            return validation_status

        except Exception as e:
            raise e