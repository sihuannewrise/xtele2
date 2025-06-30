from time import sleep
from tqdm import tqdm

if __name__ == '__main__':
    for i in tqdm(range(2000), desc='запись в БД'):
        sleep(0.003)
    for i in tqdm(range(1000), desc='Downloading'):
        sleep(0.001)
