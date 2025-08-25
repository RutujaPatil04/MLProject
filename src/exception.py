import sys #any exception handling sys will come inot picture

from logger import logging
# How message will look like
def error_message_detail(error,error_detail:sys):
    _,_,exc_tb = error_detail.exc_info()
    file_name = exc_tb.tb_frame.f_code.co_filename
    error_message = "Error occured in python script name [{0}] line number [{1}] error message [{2}]".format(
    file_name,exc_tb.tb_lineno,str(error)
    
    )
    return error_message
# Provides detailed and uniform error messages.
class CustomException(Exception):
    def __init__(self, error_message,error_detail:sys):
        super().__init__(error_message)
        self.error_message = error_message_detail(error_message,error_detail=error_detail)

#__str__ is needed because it customizes the print/logging representation of your custom exception, 
# making sure the detailed error info is shown whenever the exception is printed or logged.
    def __str__(self):
        return self.error_message
    
if __name__=="__main__":
    try:
        a=1/0
    except Exception as e:
        logging.info("Division by zero")
        raise CustomException(e,sys)
        