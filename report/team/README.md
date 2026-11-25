# Báo cáo nhóm

| File | Nhiệm vụ | Ai điền | Ghi chú |
|---|---|---|---|
| `bang_chi_phi.md` | A, B | Người viết code, người kiểm số | A1–A4, B1–B4; ghi nhãn `simulated` cho số dùng cột `_simulated`. Mỗi câu trả lời tối đa 3 dòng và có số. |
| `bang_loi.md` | C | Hai người gắn nhãn | Hai bộ nhãn độc lập cho 20 ca, đồng thuận ít nhất 16/20, quy tắc xử lý ca bất đồng và bảng khắc phục đủ 5 loại lỗi. |
| `pilot_plan.yaml` | D | Nhóm trưởng hoặc vai trò được phân công | Hoàn tất D1/D2 và mọi trường YAML; không còn `?` ngoài chú thích, tối thiểu 3 luật dừng đủ vế NẾU–TRONG–THÌ–KHÔNG THÌ; tải được bằng `yaml.safe_load`. |
| `chi_so.md` | E | Người phụ trách chỉ số | Chỉ số chính, dùng, an toàn; ít nhất 6 event có `trace_id`; nối từng chỉ số với event tính ra nó; ít nhất 2 rủi ro kinh tế có số và người phụ trách. |
| `ho_so_launch_v0.md` | E | Người giữ hồ sơ | Một trang, đủ 7 mục; mỗi mục có số chính, trạng thái và người phụ trách là một vai trò; dòng cuối cùng là đề xuất Go, Go có điều kiện hoặc No-go. |
| `phieu_cham.md` | Duyệt chéo | Nhóm được phân công làm hội đồng | Điền phiếu đánh giá nhóm kế tiếp theo vòng (nhóm cuối đánh giá nhóm đầu), có bằng chứng và nhận xét theo rubric. |
| `group_report.md` | Tổng kết | Cả nhóm | Báo cáo ngắn nêu cách làm, kết quả chính, đề xuất, khó khăn, đóng góp và hạn chế; dẫn tới các hồ sơ chi tiết. |
| `MSSV_HoTen.md` | Báo cáo cá nhân | Từng thành viên | Mỗi người tạo file riêng từ mẫu, ghi phần việc, đóng góp, bằng chứng, công cụ AI và cách tự kiểm tra. |

Giữ nguyên tên các file trên để trợ giảng đối chiếu được.

## Quy tắc hoàn thiện hồ sơ

- Mọi câu trả lời trong hồ sơ cần ngắn gọn, có số liệu và nêu rõ nguồn khi phù hợp. Mọi kết quả tính từ cột `_simulated` phải được đánh dấu `simulated`.
- Ghi người phụ trách theo vai trò cụ thể; không ghi “cả đội”. Không mô tả pilot như đã được phê duyệt vận hành chính thức; Gate 2a chỉ duyệt kế hoạch pilot.
- Hồ sơ launch phải giữ đúng 7 mục trong mẫu; trạng thái chỉ dùng **Xong, có bằng chứng**, **Chưa** hoặc **Giả lập**.
- Báo cáo cá nhân đặt tên đúng định dạng `report/team/MSSV_HoTen.md`, ví dụ `report/team/20241234_NguyenVanAn.md`. Không đổi tên hoặc xoá file mẫu.

Thông tin, vai trò, đóng góp và bằng chứng của từng thành viên cũng phải được khai báo trong `TEAM.md` ở thư mục gốc.
