disk_capacity_mb = 1.44
pages = 100
lines = 50
chars = 25
bytes_per_char = 4

book_size_bytes = pages * lines * chars * bytes_per_char
disk_capacity_bytes = disk_capacity_mb * 1024 * 1024
num_books_on_diskette = disk_capacity_bytes // book_size_bytes

print("Количество книг, помещающихся на дискету:", int(num_books_on_diskette))
