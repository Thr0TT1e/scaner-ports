import socket

hosts = list()
ports = [20, 21, 22, 23, 25, 42, 43, 53, 67, 69, 80, 110, 115, 123, 137, 138,
         139, 143, 161, 179, 443, 445, 514, 515, 993, 995, 1080, 1194, 1433,
         1702, 1723, 3128, 3268, 3306, 3389, 5432, 5060, 5900, 5938, 8080,
         10000, 20000]

answer = input('Указать адрес сайта (site) или путь к файлу (file): ')

if answer == 'site':
    hosts.append(input('Введи имя сайта без http/https или IP-адрес: '))
else:
    pathFile = input('Введите полный путь к файлу: ')
    with open(pathFile, 'r', encoding='UTF-8') as f:
        for str in f:
            hosts.append(str.strip())

print(f'Хосты: {hosts}')
print('\nОжидайте идёт сканирование!\n')

for host in hosts:
    for port in ports:
        s = socket.socket()
        s.settimeout(1)

        try:
            s.connect((host, port))
        except socket.error:
            pass
        else:
            print(f'{host}: {port} порт активен')

        s.close()

print('\nСканирование завершено!\n')
