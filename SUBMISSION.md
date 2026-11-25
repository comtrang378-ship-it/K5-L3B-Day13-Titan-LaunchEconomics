# Submission

## Loại bài

**Nhóm** (4 người). Nhóm push bài lên GitHub; mỗi thành viên tự nộp cùng link repo nhóm trên LMS bằng tài khoản cá nhân. Ai không nộp link thì không có điểm, dù nhóm đã nộp.

## Tên repo và biến tên

- `Kn`: số khóa. Khóa này dùng `K5`.
- Level/lớp: `L3A` hoặc `L3B`.

### Repo bài nộp nhóm

```text
K5-L3A-DAY13-TenNhom-LaunchEconomics
```

Lớp L3B thay `L3A` bằng `L3B`. `TenNhom` viết không dấu, không khoảng trắng. Repo phải public, hoặc đã mời giảng viên vào.

### Tạo repo nhóm

Nhóm trưởng Fork repo đề bài rồi đổi tên theo mẫu trên. Nếu không Fork được, clone repo đề bài, đổi `origin` sang repo nhóm rỗng và push `main`:

```bash
git clone https://github.com/VinUni-AI20k/K5-L34-Day13-Lab.git <TEN_REPO_NHOM>
cd <TEN_REPO_NHOM>
git remote rename origin upstream
git remote add origin <URL_REPO_NHOM>
git push -u origin main
```

## Cấu trúc và deliverable phải nộp (đặt tên và cấu trúc)

### Code (trong `src/`)

| File | Nội dung | Nhiệm vụ |
|---|---|---|
| `src/lab13.py` | Code chạy được từ đầu đến cuối trong `src/`, in ra các bảng | A, B, D1 |

### Hồ sơ nhóm (trong `report/team/`, giữ nguyên tên file)

| File | Nội dung | Nhiệm vụ |
|---|---|---|
| `report/team/bang_chi_phi.md` | Bảng A2, A3, bảng độ nhạy, câu trả lời B3 và B4 | A, B |
| `report/team/bang_loi.md` | Hai bộ nhãn, tỉ lệ đồng thuận, bảng khắc phục 5 ca | C |
| `report/team/pilot_plan.yaml` | Kế hoạch pilot, không còn dấu `?` | D |
| `report/team/chi_so.md` | Đặc tả chỉ số, danh sách event, các dòng rủi ro kinh tế | E |
| `report/team/ho_so_launch_v0.md` | Một trang, bảy mục; dòng cuối khuyến nghị Gate 2a có bắt đầu pilot hay không: Go / Go có điều kiện / No-go | E |
| `report/team/phieu_cham.md` | Phiếu nhóm mình chấm nhóm khác khi làm hội đồng | Duyệt chéo |

### Thông tin nhóm và báo cáo

| File | Nội dung |
|---|---|
| `TEAM.md` (root) | Thông tin nhóm, thành viên, vai và đóng góp |
| `report/team/group_report.md` | Báo cáo nhóm ngắn |
| `report/team/MSSV_HoTen.md` | Mỗi thành viên một file, copy từ mẫu và đổi tên, ví dụ `report/team/20241234_NguyenVanAn.md` |

Demo xem nhanh các kết quả A–E: [demo-lab13-titan.html](demo-lab13-titan.html). Slide giải thích riêng về cỡ mẫu và rollout: [slide-d1-ba-cach-chia.html](slide-d1-ba-cach-chia.html). Đây là các trang trình bày bổ trợ, không thay thế code hoặc hồ sơ phải nộp.

Không commit `.venv/` hay `.env`.

## Mốc tại lớp

- **17:00:** `report/team/ho_so_launch_v0.md` đã đủ bảy mục để gửi cho nhóm hội đồng.
- **17:45–18:00:** commit và push bản làm tại lớp.

Các mốc giờ trong [CHECKPOINTS.md](CHECKPOINTS.md) là checkpoint tại lớp, không phải deadline.

## Deadline (GMT+7)

- Lab **sáng** và lab **chiều** (lịch mẫu 14:00–18:00): nộp trước **23h59 GMT+7** ngày lab.
- Coach có thể gia hạn ≤ 48h nếu có lý do chính đáng; nếu gia hạn thì theo thông báo của coach.
- Sửa sau deadline phải tạo commit mới; xem [RULES.md](RULES.md).

## Checklist

- [ ] Đổi tên repo theo đúng quy ước `K5-L3A-DAY13-…` (hoặc `K5-L3B-DAY13-…`).
- [ ] Điền `TEAM.md` ở root: thông tin nhóm, thành viên, vai, đóng góp.
- [ ] Mỗi thành viên có file báo cáo đã đổi tên đúng định dạng `report/team/MSSV_HoTen.md`.
- [ ] Chạy `lab13.py` hết trên máy khác trong nhóm (Windows PowerShell: `Set-Location src; python lab13.py`; macOS/Linux: `cd src && python3 lab13.py`); ba phép thử A1 in ĐẠT (1,20 · 1,25 · 1,25).
- [ ] Đủ sáu file hồ sơ trong `report/team/`, đúng tên.
- [ ] Mọi con số từ cột `_simulated` có nhãn `simulated`.
- [ ] `report/team/pilot_plan.yaml` đọc được bằng `yaml.safe_load` và không còn dấu `?`; ít nhất ba luật dừng đủ bốn vế NẾU – TRONG – THÌ – KHÔNG THÌ.
- [ ] D1 ghi tách cỡ mẫu hiệu dụng và số yêu cầu thô sau điều chỉnh cụm; với 20 nhân viên/nhánh, 859 hiệu dụng tương ứng khoảng 5.980 yêu cầu thô (299/người, DE 6,96).
- [ ] Mỗi mục hồ sơ có người phụ trách là một vai trò, không ghi "cả đội".
- [ ] Đề xuất Gate 2a chọn một trong ba quyết định về bắt đầu pilot: Go, Go có điều kiện hoặc No-go. Go có điều kiện phải nêu từng điều kiện, vai trò chịu trách nhiệm và ngày kiểm tra; No-go phải nêu bằng chứng và việc cần khắc phục trước khi trình lại. Đây là quyết định về pilot, không phải phê duyệt mở rộng vận hành chính thức.
- [ ] Không có từ "production" trong file hồ sơ.
- [ ] Không commit secret, password, file `.env`.
- [ ] Đã push lên GitHub; repo mở được cho người chấm.
- [ ] Mọi thành viên đã nộp cùng link repo trên LMS trước deadline.

### Ví dụ quyết định Gate 2a

> **Đề xuất: Go có điều kiện** — chỉ bắt đầu pilot trợ lý cho `noi_dia` và `hang_nang`; chưa mở rộng sang các loại yêu cầu khác.
>
> | Điều kiện trước khi bắt đầu | Người phụ trách | Hạn | Bằng chứng hoàn tất |
> |---|---|---|---|
> | Sửa lỗi báo hoàn thành khi sổ cái trả 503 và thêm khóa chống hoàn trùng (ca 7, 20). | Kỹ sư trưởng agent | 2027-01-05 | Kiểm thử lỗi 503 và gửi lặp; mỗi yêu cầu chỉ ghi sổ hoàn tiền một lần, có cùng `trace_id`. |
> | Chấp nhận đánh đổi cỡ mẫu: 20 nhân viên mỗi nhánh, MDE 6 điểm; nếu tác động thật là 5 điểm, power khoảng 0,64. | Giám đốc vận hành | 2027-01-05 | Quyết định pilot được ghi nhận trước khi phân nhóm. |
> | Bật event có `trace_id` và thay thời gian nhân viên `simulated` bằng số đo thật sau tuần đầu. | Người phụ trách chỉ số | Trước pilot; báo cáo sau tuần 1 | Kiểm tra đủ event và có bảng thời gian đo thật. |
>
> **Nếu một điều kiện chưa đạt:** chưa bật pilot; giữ quyết định No-go cho đến khi có bằng chứng và hội đồng xem xét lại.
