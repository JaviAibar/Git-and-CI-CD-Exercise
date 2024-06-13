import sys

def clean_buffer(clients_len):
    for _ in range(clients_len):
        next(sys.stdin)

def reduce_by_min(array):
    min_value = obtener_numero_mas_bajo(array)
    empties = []
    for i in range(len(array)):
        if array[i] == min_value:
            array[i] = 0
            empties.append(i)
        else:
            array[i] -= min_value
    return empties

def obtener_numero_mas_bajo(lista_enteros):
    return min(lista_enteros)

def main():
    with open('input.txt', 'r') as file:
        data = file.read().split()
    idx = 0
    
    while idx < len(data):
        checkout_len = int(data[idx])
        idx += 1
        clients_len = int(data[idx])
        idx += 1

        if checkout_len > clients_len:
            idx += clients_len
            print(clients_len + 1)
            continue

        if checkout_len == 1:
            idx += clients_len
            print(1)
            continue

        checkouts = [0] * checkout_len
        clients = [0] * (clients_len - checkout_len)

        for c in range(clients_len):
            if c < checkout_len:
                checkouts[c] = int(data[idx])
            else:
                clients[c - checkout_len] = int(data[idx])
            idx += 1

        clients_len -= checkout_len
        client_index = 0
        found = False

        while not found:
            empties = reduce_by_min(checkouts)
            for e in empties:
                if client_index >= clients_len:
                    print(e + 1)
                    found = True
                    break
                checkouts[e] = clients[client_index]
                client_index += 1

if __name__ == "__main__":
    main()
