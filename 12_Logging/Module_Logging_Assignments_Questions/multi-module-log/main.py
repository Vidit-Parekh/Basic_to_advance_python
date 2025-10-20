import logging.config
from mod_a import mod_a
from mod_b import mod_b

def mul_mod_log():
    log_config = {
        'version' : 1,
        'formatters' : {
            'default' : {
                'format' : '%(asctime)s-%(name)s-%(levelname)s-%(message)s'
            }
        },
        'handlers' : {
            'file' : {
                'class' : 'logging.FileHandler',
                'filename' : 'multi_module_log.log',
                'formatter':'detailed',
                'level' : 'DEBUG' 
            },
            'console' : {
                'class' : 'logging.StreamHandler',
                'formatter' : 'default',
                'level' : 'DEBUG'
            }
        },
        'root' : {
            'handlers' : ['file','console'],
            'level' : 'DEBUG'
        }
    }

    logging.config.dictConfig(log_config)

    if __name__ == '__main__':
        mul_mod_log()
        logger = logging.getLogger(__name__)
        logger.info('The process starts!!!')
        mod_a()
        mod_b()
        logger.info('The process finishes!!!')