import json
with open("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/4 lab/JSON/sample-data.json", "r") as f:
    data = json.load(f)

for item in data["imdata"]:
    attr = item["l1PhysIf"]["attributes"]
    dn = attr.get("dn")
    descr = attr.get("descr")
    speed = attr.get("speed")
    mtu = attr.get("mtu")
    print(f"{dn:50} {descr:3} {speed:7} {mtu}")
























#     Этот код на Python выполняет следующие действия:

# 1. Открывает и загружает JSON-файл

# import json
# with open("/Users/diastursynbek/Downloads/KBTU/PP2/PYTHON/4 lab/JSON/sample-data.json", "r") as f:
#     data = json.load(f)

# 	•	Открывает файл sample-data.json (если путь указан правильно).
# 	•	Загружает содержимое JSON-файла в переменную data как словарь (dict).

# 2. Выводит заголовки

# print("Inherit status")
# print("="*50)
# print("DN")
# print("-"*50)

# 	•	Выводит заголовок “Inherit status”.
# 	•	Рисует разделительные линии.

# 3. Проходит по каждому интерфейсу в JSON

# for item in data["imdata"]:
#     attr = item["l1PhysIf"]["attributes"]

# 	•	data["imdata"] – это список объектов, каждый из которых представляет собой информацию о сетевом интерфейсе.
# 	•	attr = item["l1PhysIf"]["attributes"] – извлекает атрибуты интерфейса.

# 4. Извлекает и форматирует данные

# dn = attr.get("dn")
# descr = attr.get("descr")
# speed = attr.get("speed")
# mtu = attr.get("mtu")
# print(f"{dn:50} {descr:11} {speed:7} {mtu}")

# 	•	dn (Distinguished Name) – путь к интерфейсу в сети.
# 	•	descr (Description) – описание (может быть пустым).
# 	•	speed – скорость интерфейса.
# 	•	mtu – Maximum Transmission Unit (максимальный размер пакета).

# 📌 Форматирование f"{dn:50} {descr:11} {speed:7} {mtu}":
# 	•	dn:50 – ширина 50 символов (для выравнивания).
# 	•	descr:11 – ширина 11 символов.
# 	•	speed:7 – ширина 7 символов.

# 🔹 Что будет в выводе?

# Допустим, в JSON есть такие данные:

# {
#     "imdata": [
#         {
#             "l1PhysIf": {
#                 "attributes": {
#                     "dn": "topology/pod-1/node-201/sys/phys-[eth1/1]",
#                     "descr": "Uplink",
#                     "speed": "10G",
#                     "mtu": "9000"
#                 }
#             }
#         },
#         {
#             "l1PhysIf": {
#                 "attributes": {
#                     "dn": "topology/pod-1/node-201/sys/phys-[eth1/2]",
#                     "descr": "",
#                     "speed": "inherit",
#                     "mtu": "9150"
#                 }
#             }
#         }
#     ]
# }

# 📌 Вывод в терминале:

# Inherit status
# ==================================================
# DN
# --------------------------------------------------
# topology/pod-1/node-201/sys/phys-[eth1/1]       Uplink       10G   9000
# topology/pod-1/node-201/sys/phys-[eth1/2]                   inherit   9150

# 📌 Итог

# Этот код читает JSON-файл с данными о сетевых интерфейсах и выводит информацию о каждом интерфейсе в формате таблицы.

# ✅ Если файл не найден, будет ошибка FileNotFoundError.
# ✅ Если descr пустое, просто оставит пробел.
# ✅ Используется get(), чтобы избежать KeyError, если ключа нет.

# 🔹 Если нужно что-то исправить или добавить (например, фильтрацию интерфейсов), скажите! 🚀