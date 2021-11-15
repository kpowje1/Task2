import time
import dirsync
import logging
import sys
source_path = sys.argv[1] # путь к каталогу-источнику
target_path = sys.argv[2] # путь к каталогу-реплике
interval = sys.argv[3] # интервал синхронизации
path = sys.argv[4] # путь к каталогу записи логов
try:
    interval = int(interval)
    FORMAT = '%(asctime)s - %(name)s - %(levelname)s -%(message)s'
    logging.basicConfig(filename=path + "Task 2 logs.txt", level=logging.DEBUG, format=FORMAT)
    my_log = logging.getLogger('dirsync')
    sh = logging.StreamHandler()
    sh.setFormatter(logging.Formatter(FORMAT))
    while True:
        my_log.addHandler(sh)
        dirsync.sync(source_path, target_path, 'sync', logger=my_log, purge=True, verbose=True)
        time.sleep(interval)
except:
    print('Ошибка, попробуйте снова. Обратитесь в файлу README для получения инфорации о параметрах запуска')