import logging
import datetime
from pathlib import Path


def log_file():
    today = datetime.date.today().strftime('%y%y%m%d')
    log_catalog = Path(f'/var/log/python_{today}')
    try:
        log_catalog.mkdir(exist_ok=True, parents=True)
    except PermissionError:
        print('请确定当前用户有该路径的读写权限！')
    return log_catalog / 'print_time.log'


logging.basicConfig(filename=log_file(), format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)


def func():
    logging.info('调用函数 func() ')
    print('done')


if __name__ == '__main__':
    func()
