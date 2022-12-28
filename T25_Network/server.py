import socket


def run_server(host, port):
    s = socket.socket()
    s.bind((host, port))
    s.listen()
    print(f"Сервер запущено на {host if host else '127.0.0.1'}:{port}")
    conn, address = s.accept()
    print(f"Під`єднано {address}")

    while True:

        inp_b = conn.recv(1024)
        print(f"Отримано від клієнта: {inp_b}")
        if not inp_b:
            break
        inp_s = ([int(x) for x in inp_b.split()])
        out_s = f"{min(inp_s)} \t {max(inp_s) } \n"
        out_b = bytes(out_s, encoding="utf-8")
        conn.sendall(out_b)
        print(f"Відправлено клієнту: {out_b}")

    conn.close()
    s.close()
    print("Сервер завершив роботу")


HOST = ""
PORT = 10000


if __name__ == "__main__":
    run_server(HOST, PORT)
