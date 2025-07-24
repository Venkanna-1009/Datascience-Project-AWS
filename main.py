from src.datascience import logger
from src.datascience.pipeline.Data_Ingestion_Pipeline import DataIngestionTrainingPipeline
from src.datascience.pipeline.Data_Validation_Pipeline import DataValidationTrainingPipeline
from src.datascience.pipeline.Data_Transformation_Pipeline import DataTransformationTrainingPipeline
from src.datascience.pipeline.Model_trainer_Pipeline import ModelTrainerTrainingPipeline
from src.datascience.pipeline.model_evaluation_Pipeline import ModelEvaluationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>>> stage {STAGE_NAME} started <<<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.initiate_data_ingestion()
    logger.info(f">>>>>>>>> stage {STAGE_NAME} completed <<<<<<<\n\nx========x")
except Exception as e:
    logger.exception(e)
    raise e



STAGE_NAME = "Data Validation Stage"

try:
    logger.info(f">>>>>>>>> stage {STAGE_NAME}  started <<<<<<<<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.initiate_data_validation()
    logger.info(f">>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<\n\nx=========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = " Data Transformation Stage"

try:
    logger.info(f">>>>>>>>>> stage {STAGE_NAME} started  <<<<<<<<<<<< ")
    data_transformation = DataTransformationTrainingPipeline()
    data_transformation.initiate_data_transformation()
    logger.info(f">>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\nx==========x") 
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Model trainer stage"

try:
    logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<<")
    model_trainer = ModelTrainerTrainingPipeline()
    model_trainer.initiate_model_trainer()
    logger.info(f">>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<\n\nx===========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "model evaluation stage"

try:
    logger.info(f">>>>>>>>>>>>>> stage {STAGE_NAME} started <<<<<<<<<<<<<")
    model_evaluation = ModelEvaluationTrainingPipeline()
    model_evaluation.initiate_model_evaluation()
    logger.info(f">>>>>>>>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<<<<<<<\n\nx================x")
except Exception as e:
    logger.exception(e)
    raise e 