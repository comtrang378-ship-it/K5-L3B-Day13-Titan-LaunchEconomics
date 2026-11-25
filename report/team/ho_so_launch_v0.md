# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm Titan · L3B. Kết quả mô tả trace hiện có; các ước tính dùng `_simulated` được ghi nhãn. Pilot chỉ đề xuất, chưa được xem là đã phê duyệt triển khai chính thức.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ; 978 thành công trên 1.200 yêu cầu [simulated] | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | Làm lại ×2: +51,8%; xem lại ×2: +40,7%; lương +25%: +23,1% [simulated] | Giả lập | PM trợ lý hoàn phí |
| 3 · So với nhân viên tự làm | 5.865 đ/yêu cầu = 0,49× mức 12.000 đ, đã cộng chi phí nhân viên xử lý 222 ca không thành công [simulated] | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, dùng, an toàn | 82,83% (994/1.200); bỏ qua gợi ý 27,12% (48/177); mở lại 7 ngày 4,25% (51/1.200) | Xong, có bằng chứng | Người phụ trách chỉ số |
| 5 · Bảng lỗi và cách khắc phục | Hai thành viên gắn nhãn độc lập 20 ca/5 loại; đồng thuận 20/20 (100%); tên cần bổ sung vào TEAM | Xong, có bằng chứng | Người gắn nhãn 1 và người gắn nhãn 2 |
| 6 · Pilot plan | Chia theo nhân viên, 20 người/nhánh; MDE 6 điểm cần 859 yêu cầu hiệu dụng = 5.980 thô/nhánh (299/người; DE 6,96); power khoảng 0,64 nếu tác động thật là 5 điểm | Giả lập | Giám đốc vận hành LogiX-VN |
| 7 · Rủi ro kinh tế | Làm lại ×2: 6.787 đ/việc; xem lại 100%: 11.743 đ, hoặc 12.415 đ nếu làm lại 15,3 phút; chi phí cố định tăng 1.185→2.370 đ/việc khi khối lượng giảm một nửa [simulated] | Giả lập | PM trợ lý hoàn phí |

**Điều kiện trước quyết định ngày 2027-01-05:**

- Kỹ sư trưởng agent sửa xử lý lỗi sổ cái và khoá chống hoàn trùng (ca 7, 20), kiểm tra đối soát theo `trace_id`.
- Giám đốc vận hành xác nhận bằng văn bản việc chấp nhận MDE 6 điểm, 5.980 yêu cầu thô mỗi nhánh (859 hiệu dụng) và power khoảng 0,64 nếu tác động thật chỉ 5 điểm.
- Người phụ trách chỉ số xác nhận các event cần thiết đều có `trace_id` trước 2027-01-05; thay thời gian nhân viên `simulated` bằng số đo thật sau tuần đầu và báo cáo tại mốc này.
- Tại quyết định ngày 2027-01-05, Trưởng nhóm CSKH chỉ giảm tỉ lệ xem lại theo từng bước nếu chỉ số an toàn đạt ngưỡng trong `pilot_plan.yaml`; không mở rollout kế tiếp nếu luật dừng bị kích hoạt.

**Đề xuất: Go có điều kiện** — Chỉ pilot `noi_dia` và `hang_nang`; giữ `quoc_te` và `doi_tac` ngoài phạm vi cho tới khi có bằng chứng mới.
