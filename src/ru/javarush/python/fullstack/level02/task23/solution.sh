# Запустите контейнер с образом nginx, ограничив использование 512 MB оперативной памяти и 512 MB подкачки (swap).
docker run --name swap_limited_container --memory 512m --memory_swap 1024m -d nginx