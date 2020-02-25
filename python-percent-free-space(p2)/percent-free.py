import os
def disk_stat(path):
    disk = os.statvfs(path)
    percent = 100 - ((disk.f_blocks - disk.f_bfree) * 100 / (disk.f_blocks -disk.f_bfree + disk.f_bavail) + 1)
    return percent

return disk_stat('/')
#print disk_stat('/')
