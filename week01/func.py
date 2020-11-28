import logging
import datetime
from pathlib import Path
from functools import wraps


def log_file(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        today = datetime.date.today().strftime('%y%y%m%d')
        log_catalog = Path(f'/var/log/python_{today}')

        if not (log_catalog.exists() and log_catalog.is_dir()):
            try:
                log_catalog.mkdir(exist_ok=True, parents=True)
            except PermissionError:
                print('请确定当前用户有该路径的读写权限！')

        logging.basicConfig(filename=log_catalog / 'print_time.log', format='%(asctime)s - %(levelname)s - %(message)s',
                            level=logging.INFO)
        logging.info(f'调用函数 {f} {f.__name__}')

        return f(*args, **kwargs)

    return wrapper


@log_file
def func():
    print('done')


if __name__ == '__main__':
    func()
