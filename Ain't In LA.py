
import time

# ==============================
# WARNA TERMINAL
# ==============================

ORANGE = "\033[38;5;208m"
WHITE = "\033[97m"
RESET = "\033[0m"


# ==============================
# JUDUL LAGU
# ==============================

print()

print(" " * 10 + ORANGE + "== ADÉLA - AIN'T IN LA ==" + RESET)

print(" " * 16 + ORANGE + "Nama sendiri" + RESET)

print()

# JARAK SEBELUM LIRIK
print()
time.sleep(2)


# ==============================
# LIRIK DAN DURASI
# ==============================

lyrics = [
    ("Maybe tonight,", 2.0),
    ("we don't gotta run away", 2.0),
    ("It's all a lie,", 2.0),
    ("the baddest bitches ain't in LA", 2.0),
    ("Enjoy the ride,", 2.0),
    ("I know that you might wanna escape", 2.5),
    ("It's all a lie,", 1.5),
    ("the baddest bitches ain't in LA", 3.0)
]


# ==============================
# EFEK LIRIK PER HURUF
# ==============================

for teks, durasi in lyrics:

    for huruf in teks:

        print(
            WHITE + huruf + RESET,
            end="",
            flush=True
        )

        # SEDIKIT LEBIH LAMBAT
        time.sleep((durasi / len(teks)) * 1.2)

    # PINDAH BARIS
    print()

    # JEDA ANTAR LIRIK
    time.sleep(0.8)




print()
print()
