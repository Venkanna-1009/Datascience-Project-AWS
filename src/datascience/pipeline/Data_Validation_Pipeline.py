from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.Data_Validation import DataValidation
from src.datascience import logger

STAGE_NAME =  "Data Validation Stage"

class DataValidationTrainingPipeline:
    def __init__(self):
        pass

    def initiate_data_validation(self):
        config = ConfigurationManager()
        data_validation_config = config.get_data_validation_config()
        data_validation = DataValidation(config=data_validation_config)
        data_validation.validate_all_columns()


if __name__ == "__main__":
    try:
        logger.info(f">>>>>>>> stage {STAGE_NAME} started >>>>>")
        obj = DataValidationTrainingPipeline()
        obj.main()
        logger.info()
        logger.info(f">>>>>>>>>>>  stage {STAGE_NAME} completed <<<<<<<<<<< \n\nx=========x")
    except Exception as e:
        raise e
