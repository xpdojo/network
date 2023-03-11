from datetime import datetime

import psutil

from util.table import print_table


def scan_processes():
    # 현재 실행 중인 모든 프로세스에서 target_port를 사용하는 연결 정보를 가져옴
    # psutil.process_iter(attrs=['pid', 'name', 'username', 'connections'])
    connections = [pconn for pconn in psutil.net_connections()]

    # 연결 정보를 포트 번호를 기준으로 정렬
    sorted_connections = sorted(connections, key=lambda pconn: pconn.laddr.port)

    # 정렬된 연결 정보를 반환
    processes = []
    for connection in sorted_connections:
        try:
            psutil_process = psutil.Process(connection.pid)
            process = list()
            process.append(connection.laddr.port)
            process.append(psutil_process.pid)
            process.append(psutil_process.name())
            process.append(psutil_process.status())
            process.append(psutil_process.exe())
            process.append(datetime.fromtimestamp(psutil_process.create_time()))
            processes.append(process)
        except Exception as e:
            print(e)

    return processes


print_table(scan_processes())
