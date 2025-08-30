import logger

def lambda_handler(event, context):
    log = logger.get_logger()
    log.info("共通Loggerが効いてます")
    log.debug("DEBUGレベルのログ")
    return {"statusCode": 200}
