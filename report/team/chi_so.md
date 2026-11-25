# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | **82,83% (994/1.200)** |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | **27,12% (48/177)** |
| An toàn | Tỉ lệ yêu cầu bị mở lại trong 7 ngày (proxy lỗi lọt đến khách) | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | **4,25% (51/1.200)** |
| Dùng (tự đề xuất) | Tỉ lệ dùng trợ lý trong nhóm được phân vào treatment | Số yêu cầu treatment có `assistant_panel_opened`, chia yêu cầu được phân vào treatment | Chưa có event mở trợ lý trong trace hiện tại; đo trong pilot |
| An toàn (tự đề xuất) | Tỉ lệ đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần | Số đơn sai tiền trong `audit_sample_checked`, chia tổng đơn được kiểm tra | Chưa có dữ liệu kiểm toán mẫu; bắt đầu đo hằng tuần trong pilot |

Các tỉ lệ trên mô tả đợt chạy thử; không kết luận trợ lý đã làm tăng hoặc giảm chỉ số vì dữ liệu này không có nhóm đối chứng.

## Danh sách event

Mỗi event có `trace_id` để nối với trace của agent và `request_id` khi cần nối các lần chạy của cùng yêu cầu.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | App khách | `request_id`, `created_at`, `loai`, `so_tien`, `arm`, `trace_id` | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | `attempt`, `tokens_in`, `tokens_out`, `tool_calls`, `status`, `trace_id` | Sau mỗi lần chạy, kể cả lỗi |
| `assistant_panel_opened` | Giao diện nhân viên | `request_id`, `staff_id`, `trace_id` | Khi nhân viên mở trợ lý |
| `agent_suggestion_shown` | Giao diện nhân viên | `request_id`, `staff_id`, `so_tien_de_xuat`, `trace_id` | Khi gợi ý hiện ra |
| `staff_review_decision` | Nhân viên | `request_id`, `giu/sua/bo`, `phut_xem_lai`, `trace_id` | Khi bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | `phut_lam_lai`, `ly_do`, `trace_id` | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | `idempotency_key`, `so_tien`, `ket_qua`, `trace_id` | Khi ghi sổ hoàn tiền |
| `handoff_to_staff` | Agent | `reason`, `tom_tat`, `trace_id` | Khi chuyển cho nhân viên |
| `ticket_closed` | Hệ thống ticket | `request_id`, `closed_at`, `trace_id` | Khi đóng yêu cầu |
| `ticket_reopened` | Khách / hệ thống ticket | `request_id`, `reopened_at`, `reason`, `trace_id` | Khi yêu cầu được mở lại |
| `audit_sample_checked` | Kế toán | `so_tien_da_hoan`, `so_tien_dung`, `ket_qua`, `trace_id` | Khi kiểm tra mẫu hằng tuần |

**Kiểm tra chéo:** với mỗi chỉ số ở bảng E1, ghi event dùng để tính. Chỉ số nào không tính được từ danh sách event thì chưa đo được.

- Chỉ số chính: `refund_request_created.created_at` là mốc bắt đầu; nối `ticket_closed.closed_at` để xác nhận đóng trong 24 giờ, rồi kiểm tra không có `ticket_reopened` trong 7 ngày; đếm yêu cầu duy nhất.
- Tỉ lệ bỏ qua gợi ý: `staff_review_decision`; tử số là yêu cầu duy nhất có quyết định `sua` hoặc `bo`, mẫu số là yêu cầu duy nhất được xem lại.
- Tỉ lệ mở lại: số `request_id` duy nhất có `ticket_reopened` trong 7 ngày chia số yêu cầu từ `refund_request_created`.
- Mức sử dụng: số `request_id` treatment duy nhất có `assistant_panel_opened` chia tổng `request_id` duy nhất được phân vào treatment trong `refund_request_created`.
- Tỉ lệ hoàn sai tiền: `audit_sample_checked`; chưa tính được cho trace hiện tại vì chưa có mẫu kiểm toán.

## E2 · Rủi ro kinh tế

Ít nhất hai dòng, số lấy từ bảng độ nhạy (`bang_chi_phi.md`).

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | Chi phí mỗi việc thành công tăng **51,8% lên 6.787 đ** [simulated]. | Tỉ lệ làm lại theo tuần vượt 7%; mức hiện tại trong phạm vi pilot là 4,9% [simulated]. | Thu hẹp về `noi_dia`, rà 20 trace làm lại và ghi nguyên nhân. | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | **11.743 đ = 0,98×** baseline; tăng lên **12.415 đ = 1,03×** nếu làm lại trung bình 15,3 phút [simulated]. | Tỉ lệ yêu cầu phải xem lại vẫn trên 50% ở cuối bước rollout 0,25. | Giảm tỉ lệ xem lại theo từng bước khi tỉ lệ sửa + bỏ dưới 15%; theo dõi lỗi lọt trước khi giảm tiếp. | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu đ/tháng tương đương **1.185 đ/việc** ở 45.000 yêu cầu/tháng và **2.370 đ/việc** nếu khối lượng còn một nửa [simulated]. | Số việc thành công mỗi tuần thấp hơn 50% kế hoạch. | Không mở rộng rollout; rà lại giả định khối lượng và điều khoản chi phí cố định. | PM trợ lý hoàn phí |
