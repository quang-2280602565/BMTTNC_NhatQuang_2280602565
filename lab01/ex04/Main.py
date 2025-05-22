from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()

while True:
    print("\nChuong trinh quan ly sinh vien")
    print("**********************MENU*********************")
    print("*** 1.Them sinh vien                       ****")
    print("*** 2.Cap nhat thong tin sinh vien         ****")
    print("*** 3.Xoa sinh vien theo id                ****")
    print("*** 4.Tim sinh vien theo ten               ****")
    print("*** 5.Sap xep sinh vien theo diem TB       ****")
    print("*** 6.Sap xep sinh vien theo ten           ****")
    print("*** 7.Hien thi danh sach sinh vien         ****")
    print("*** 0.Thoat                                ****")
    print("***********************************************")

    key = int(input("Nhap tuy chon: "))

    # Check if there are students in the list
    if qlsv.soLuongSinhVien() == 0:
        print("\nDanh sach sinh vien rong")
    
    elif key == 1:
        print("\n1.Them sinh vien ")
        qlsv.nhapSinhVien()
        print("\nThem sinh vien thanh cong")

    elif key == 2:
        if qlsv.soLuongSinhVien() > 0:
            print("\n2.Cap nhat thong tin sinh vien  ")
            print("\nNhap ID: ")
            ID = int(input())
            qlsv.updateSinhVien(ID)  # Call method with parentheses
            print("\nCap nhat thong tin thanh cong")
        else:
            print("\nDanh sach sinh vien rong")

    elif key == 3:
        if qlsv.soLuongSinhVien() > 0:
            print("\n3.Xoa sinh vien theo id  ")
            print("\nNhap ID: ")
            ID = int(input())
            if qlsv.deleteById(ID) > 0:
                print(f"\nSinh Vien co id = {ID} da bi xoa")
            else:
                print(f"\nSinh Vien co id = {ID} khong ton tai")
        else:
            print("\nDanh sach sinh vien rong")

    elif key == 4:
        if qlsv.soLuongSinhVien() > 0:
            print("\n4.Tim sinh vien theo ten")
            print("\nNhap ten: ")
            name = input()
            searchResult = qlsv.findByName(name)
            qlsv.showSinhVien(searchResult)
        else:
            print("\nDanh sach sinh vien rong")

    elif key == 5:
        if qlsv.soLuongSinhVien() > 0:
            print("\n5.Sap xep sinh vien theo diem TB")
            qlsv.sortByDiemTB()
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien rong")

    elif key == 6:
        if qlsv.soLuongSinhVien() > 0:
            print("\n6.Sap xep sinh vien theo ten")
            qlsv.sortByName()  # Fixed method name
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien rong")

    elif key == 7:
        if qlsv.soLuongSinhVien() > 0:
            print("\n7.Hien thi danh sach sinh vien")
            qlsv.showSinhVien(qlsv.getListSinhVien())
        else:
            print("\nDanh sach sinh vien rong")

    elif key == 0:
        print("\nBan da thoat")
        break

    else:
        print("\nKhong co chuc nang nay")
        print("\nHay chon chuc nang trong menu")
