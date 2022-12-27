import socket


def run_client(host, port, inp, out):
    s = socket.socket()
    s.connect((host, port))
    print(f"Під`єднано до {host}:{port}")

    finp = open(inp, encoding="utf-8")
    fout = open(out, "w", encoding="utf-8")

    for line in finp:
        out_b = bytes(line, encoding="utf-8")
        s.sendall(out_b)
        print(f"Відправлено серверу: {out_b}")
        inp_b = s.recv(1024)
        print(f"Отримано від сервера: {inp_b}")
        inp_s = str(inp_b, encoding="utf-8")
        fout.write(inp_s)

    s.sendall(b"")

    finp.close()
    fout.close()

    s.close()
    print("Клієнт завершив роботу")


HOST = "127.0.0.1"
PORT = 10000

if __name__ == "__main__":
    run_client(HOST, PORT, "input.txt", "output.txt")