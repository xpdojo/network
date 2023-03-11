import psutil
from psutil._common import snicstats, snicaddr

# 현재 시스템에서 사용 가능한 모든 네트워크 인터페이스를 가져오기
net_if_addrs: dict[str, list[snicaddr]] = psutil.net_if_addrs()
net_if_stats: dict[str, snicstats] = psutil.net_if_stats()

for interface_name in net_if_addrs.keys():
    print('===============================')
    print(net_if_addrs.get(interface_name))
    print(net_if_stats.get(interface_name))
