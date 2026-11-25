# Báo cáo nhóm

Báo cáo tóm tắt kết quả của nhóm Titan, L3B. Chi tiết và nguồn số liệu nằm trong các hồ sơ liên kết bên dưới. Dữ liệu trace của lab có các trường giả lập và không có nhóm đối chứng, vì vậy kết quả mô tả đợt chạy thử, không khẳng định tác động nhân quả.

## 1. Thông tin nhóm

- Tên nhóm: Titan
- Lớp: L3B
- Thành viên: xem [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Đánh giá chi phí trợ lý hoàn phí LogiX-VN, loại yêu cầu phù hợp, rủi ro khi lỗi và cách thiết kế pilot để có thể ra quyết định. Nhóm đối chiếu dữ liệu 1.200 yêu cầu với trace chạy, hướng dẫn lab và rubric; các thời gian nhân viên được đánh dấu `simulated`.

## 3. Giải pháp

- **A — Chi phí:** ba phép thử đáp án biết trước đạt. Với 1.200 yêu cầu, tổng chi phí là 4.373.585 đ, có 978 việc thành công và 4.472 đ/việc thành công [simulated]. `noi_dia` đạt 2.696 đ [simulated], `hang_nang` 8.221 đ [simulated], `quoc_te` 22.515 đ [simulated]. Chi tiết ở [bang_chi_phi.md](./bang_chi_phi.md).
- **B — Độ nhạy:** làm lại là yếu tố tác động lớn nhất; nếu số ca làm lại tăng gấp đôi, chi phí tăng 51,8% lên 6.787 đ/việc [simulated]. Giới hạn 2 lần chạy cho tổng chi phí hệ thống thấp nhất trong ba phương án, 6.901.220 đ [simulated]. Chi tiết ở [bang_chi_phi.md](./bang_chi_phi.md).
- **C — Lỗi:** hai thành viên theo vai kiểm thử và lập trình web đã gắn nhãn độc lập 20 ca vào 5 loại Google PAIR; đồng thuận 20/20 (100%). Bảng có cách phát hiện đo được và vai trò phụ trách; tên hai thành viên cần bổ sung vào TEAM. Xem [bang_loi.md](./bang_loi.md).
- **D — Pilot:** chọn chia ngẫu nhiên theo nhân viên, 20 nhân viên mỗi nhánh. MDE 6 điểm cần 859 yêu cầu hiệu dụng, tương ứng 5.980 yêu cầu thô mỗi nhánh (299/người; DE 6,96); nếu tác động thật chỉ 5 điểm, power ước tính khoảng 0,64. Kế hoạch có đối chứng cùng thời gian và ba luật dừng. Xem [pilot_plan.yaml](./pilot_plan.yaml).
- **E — Chỉ số:** trong mẫu, chỉ số chính là 82,83% (994/1.200), tỉ lệ bỏ qua gợi ý 27,12% (48/177), tỉ lệ mở lại trong 7 ngày 4,25% (51/1.200). Hồ sơ đề xuất 11 event có `trace_id` và ba rủi ro kinh tế. Xem [chi_so.md](./chi_so.md).

## 4. Kết quả và đề xuất

Đề xuất **Go có điều kiện** cho pilot giới hạn ở `noi_dia` và `hang_nang`; loại `quoc_te` và `doi_tac` khỏi phạm vi ban đầu. Trước khi bắt đầu cần sửa lỗi hoàn trùng và đối soát sổ cái, được Giám đốc vận hành chấp thuận đánh đổi MDE 6 điểm (power khoảng 0,64 nếu tác động chỉ 5 điểm), bật đủ event có `trace_id`, thay thời gian `simulated` bằng thời gian đo thật sau tuần đầu, và giảm xem lại theo từng bước khi dữ liệu an toàn cho phép.

Kết quả chấm chéo chưa có: chưa biết số thứ tự nhóm Titan để xác định nhóm kế tiếp; URL hiện có là repo của Titan, không phải hồ sơ peer. Phiếu [phieu_cham.md](./phieu_cham.md) giữ trạng thái chờ, không tự gán điểm khi thiếu bằng chứng.

## 5. Khó khăn và cách xử lý

Thời gian xem lại và làm lại trong trace là `simulated`, nên nhóm gắn nhãn rõ và đưa việc đo thời gian thật vào điều kiện pilot. Mẫu hiện tại không có nhóm đối chứng, nên báo cáo chỉ mô tả kết quả quan sát. Cỡ mẫu 859 là hiệu dụng; kế hoạch yêu cầu 5.980 quan sát thô mỗi nhánh sau điều chỉnh cụm. Tên người gắn nhãn và hồ sơ peer vẫn cần bổ sung.

## 6. Tổng hợp đóng góp

Thông tin thành viên và vai trò chính thức xem [TEAM.md](../../TEAM.md). Nguyễn Anh Tú phụ trách kiểm số, tổng hợp và phối hợp hoàn thiện phần lớn hồ sơ A–E; chi tiết ở [2A202604088_NguyenAnhTu.md](./2A202604088_NguyenAnhTu.md). Thông tin, đóng góp và bằng chứng của ba thành viên còn lại chưa được cung cấp, đã được đánh dấu chờ bổ sung trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

Các kết quả kinh tế phụ thuộc giả định `simulated`; mẫu không chứng minh trợ lý gây ra thay đổi chỉ số. Cỡ mẫu theo cụm không đủ để phát hiện mức tăng 5 điểm với 40 nhân viên. Cần chạy pilot có nhóm đối chứng ngẫu nhiên, đo thời gian lao động thật, kiểm toán mẫu định kỳ, bổ sung danh tính người gắn nhãn và chấm chéo sau khi nhận hồ sơ nhóm được phân công.

## 8. Tài liệu tham khảo

- [Hướng dẫn chi tiết Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md)
- [Dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md)
- [Rubric](../../RUBRIC.md)
- `src/logix_runs.csv` và `src/logix_requests.csv` (dữ liệu giả lập của lab)
