import os
import logging
import src
from src.core.base_worker import BaseWorker



class LogWorker(BaseWorker):
    
    def func_set_log_level(self, level:str):
        try:
            level = level.upper()
            
            if not hasattr(logging, level):
                raise ValueError(f"Invalid log level: {level}") # DEBUG, INFO, WARNING, ERROR, CRITICAL
            
            logger = logging.getLogger(src.APP_NAME)
            logger.setLevel(getattr(logging, level))
            
            return {
                "level": level,
                "message": "Log level has been updated"
            }
            
        except Exception as e:
            raise RuntimeError(str(e))
        
    
    def func_get_logs(self, level:str | None = None):
        try:
            log_file = src.LOG_FILE
            
            if not os.path.exists(log_file):
                return []

            level = level.upper() if level else None
            logs = []
            
            with open(log_file, "r", encoding="utf-8") as file:
                for line in file:
                    if level is None or f"| {level} |" in line:
                        logs.append(line.rstrip())            
            return logs
            
        except Exception as e:
            raise RuntimeError(str(e))