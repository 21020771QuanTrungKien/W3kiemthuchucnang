def tien_tro_cap(base, dependents, age_group):
    tro_cap = 0.0
    if age_group == 't':
        if dependents < 0:
            return -1  # Trả về -1 nếu dependents là số âm
        if dependents == 0:
            return tro_cap 
        elif dependents == 1:
            tro_cap = base + 0.3 * base
        else:
            tro_cap = base + 0.5 * base
            if dependents >= 3:
                tro_cap += 0.3 * base
    elif age_group == 'g':
        if dependents < 0:
            return -1  # Trả về -1 nếu dependents là số âm
        elif dependents == 0:
            tro_cap = base * 0.3
        elif dependents == 1:
            tro_cap = base + 0.5 * base
        else:
            tro_cap = base + 0.8 * base
            if dependents >= 3:
                tro_cap += 0.2 * base
    return int(tro_cap)

def main():
    while True:  # Lặp lại việc nhập thông tin nếu tro_cap = -1
        try:
            base = float(input("Nhap muc tien tro cap co so (dolar): "))
            dependents = int(input("Nhap so nguoi phu thuoc: "))
            age_group = input("Nhap nhom tuoi (t/g): ")[0]

            tro_cap = tien_tro_cap(base, dependents, age_group)

            if tro_cap == -1:
                print("Nhap lai thong tin. So nguoi phu thuoc khong the la so am.")
            else:
                break  # Thoát khỏi vòng lặp nếu tro_cap không bằng -1

        except ValueError:
            print("Nhap sai dinh dang. Vui long nhap lai.")

    if tro_cap == 0:
        print("Khong duoc tro cap (co lam thi moi co an)")
    else:
        print("Tien tro cap duoc tinh la: {} dolar".format(tro_cap))

if __name__ == "__main__":
    main()
