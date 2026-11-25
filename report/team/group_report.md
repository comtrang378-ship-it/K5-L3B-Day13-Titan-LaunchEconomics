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
- **C — Lỗi:** hai phiếu cho 20 ca/5 loại khớp 20/20, nhưng một người đã tiếp cận nhãn tham khảo qua AI trước khi đối chiếu; vì vậy chưa tính đây là đồng thuận độc lập hợp lệ. Cần xin bộ ca mới hoặc phương án thay thế từ giảng viên. Xem [bang_loi.md](./bang_loi.md).
- **D — Pilot:** chọn chia ngẫu nhiên theo nhân viên, 20 nhân viên mỗi nhánh. MDE 6 điểm cần 859 yêu cầu hiệu dụng, tương ứng 5.980 yêu cầu thô mỗi nhánh (299/người; DE 6,96); nếu tác động thật chỉ 5 điểm, power ước tính khoảng 0,64. Bậc 50% kiểm mẫu sau tuần đầu, có thể kéo dài tối đa 15 ngày làm việc; quyết định chỉ sau khi khóa mẫu và đủ 7 ngày theo dõi. Xem [pilot_plan.yaml](./pilot_plan.yaml).
- **E — Chỉ số:** trong mẫu, chỉ số chính là 82,83% (994/1.200), tỉ lệ bỏ qua gợi ý 27,12% (48/177), tỉ lệ mở lại trong 7 ngày 4,25% (51/1.200). Hồ sơ đề xuất 11 event có `trace_id` và ba rủi ro kinh tế. Xem [chi_so.md](./chi_so.md).

## 4. Kết quả và đề xuất

Đề xuất **Go có điều kiện** cho pilot giới hạn ở `noi_dia` và `hang_nang`; loại `quoc_te` và `doi_tac` khỏi phạm vi ban đầu. Trước khi bắt đầu cần sửa lỗi hoàn trùng và đối soát sổ cái, được Giám đốc vận hành chấp thuận MDE 6 điểm (859 hiệu dụng/5.980 thô mỗi nhánh), bật đủ event và đo thời gian thật. Bậc 50% có thể thu mẫu tối đa 15 ngày làm việc; chỉ giảm xem lại khi chi phí hệ thống dưới 12.000 đ/yêu cầu và ba lần rà đạt ngưỡng an toàn. Quyết định dựa trên KTC 95% có điều chỉnh cụm, sau khi đủ mẫu và 7 ngày theo dõi.

Nhóm Titan là nhóm số 1; phiếu chấm chéo đối chiếu Titan với Ghidorah. Phản hồi bằng văn bản của Ghidorah giúp đối chiếu các điều kiện pilot, nhưng chưa có hồ sơ kết quả đầy đủ của Ghidorah nên chưa chốt điểm rubric hoặc đề xuất launch. Xem [phiếu chấm chéo](./phieu_cham.md).

## 5. Khó khăn và cách xử lý

Thời gian xem lại và làm lại trong trace là `simulated`, nên nhóm gắn nhãn rõ và đưa việc đo thời gian thật vào điều kiện pilot. Mẫu hiện tại không có nhóm đối chứng, nên báo cáo chỉ mô tả kết quả quan sát. Cỡ mẫu 859 là hiệu dụng; kế hoạch yêu cầu 5.980 quan sát thô mỗi nhánh sau điều chỉnh cụm. Nhãn CP3 bị ảnh hưởng do một người đã thấy nhãn tham khảo; cần bộ ca mới để xác nhận đồng thuận độc lập.

## 6. Tổng hợp đóng góp

Thông tin thành viên và vai trò chính thức xem [TEAM.md](../../TEAM.md). Nguyễn Anh Tú phụ trách kiểm số, tổng hợp và phối hợp hoàn thiện phần lớn hồ sơ A–E; chi tiết ở [2A202604088_NguyenAnhTu.md](./2A202604088_NguyenAnhTu.md). Thông tin, đóng góp và bằng chứng của ba thành viên còn lại chưa được cung cấp, đã được đánh dấu chờ bổ sung trong `TEAM.md`.

## 7. Hạn chế và hướng cải thiện

Các kết quả kinh tế phụ thuộc giả định `simulated`; mẫu không chứng minh trợ lý gây ra thay đổi chỉ số. Cỡ mẫu theo cụm không đủ để phát hiện mức tăng 5 điểm với 40 nhân viên. Cần chạy pilot có nhóm đối chứng ngẫu nhiên, đo thời gian lao động thật, kiểm toán mẫu định kỳ, xin bộ ca mới để gắn nhãn độc lập và hoàn tất phiếu chấm chéo đúng nhóm.

## 8. Tài liệu tham khảo

- [Hướng dẫn chi tiết Lab 13](../../docs/Lab13_Huong_dan_chi_tiet_buoi_chieu.md)
- [Dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md)
- [Rubric](../../RUBRIC.md)
- `src/logix_runs.csv` và `src/logix_requests.csv` (dữ liệu giả lập của lab)
