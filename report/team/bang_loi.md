# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn và giới hạn của kết quả đồng thuận

Hai thành viên đã lập nhãn riêng theo vai kiểm thử và lập trình web; tuy nhiên, theo phản hồi duyệt chéo của Ghidorah, Quốc đã tiếp cận nhãn tham khảo qua công cụ AI trước khi đối chiếu phiếu gốc của Dũng. Vì vậy, 20/20 là mức trùng quan sát được nhưng không phải bằng chứng đồng thuận độc lập đáng tin cậy. Tên đầy đủ và MSSV của hai thành viên cũng cần bổ sung vào `TEAM.md`.

Hai vai phân loại theo nguyên nhân gốc: kiểm thử tập trung vào biểu hiện và khả năng phát hiện lỗi; lập trình web tập trung vào nguồn lỗi trong luồng xử lý, dữ liệu và tích hợp.

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Mức trùng quan sát:** 20 / 20 = **100%**. Do có tiếp cận nhãn tham khảo trước khi so, không dùng con số này để kết luận CP3 đạt ngưỡng đồng thuận độc lập 80%.

**Việc cần làm:** xin giảng viên bộ ca mới hoặc phương án đánh giá thay thế; nếu được làm lại, hai người lưu riêng phiếu gắn nhãn trước khi đối chiếu. Chưa đánh dấu CP3 hoàn tất cho tới khi có bằng chứng hợp lệ.

## Quy tắc phân biệt cho các ca dễ lẫn

Hai phiếu hiện tại không có ca bất đồng; việc tiếp cận nhãn tham khảo có thể làm tăng mức trùng. Các quy tắc gốc dưới đây vẫn hữu ích khi gắn nhãn lại:

- Ca 6 và 9 là **Do người dùng** vì nguyên nhân gốc là khách chọn sai mục hoặc nhập sai mã; việc trợ lý không gợi ý là hướng khắc phục.
- Ca 13 là **Giới hạn hệ thống** vì yêu cầu ngoài phạm vi, dù trợ lý xử lý giới hạn chưa tốt.
- Ca 8 và 15 là **Hệ thống** vì lỗi đã lộ ra; **Ngầm** chỉ dùng khi không ai nhận ra cho tới lúc kiểm tra.
- Ca 18 là **Ngữ cảnh** vì số tiền đúng chính sách nhưng giả định khách tự hiểu cách tính không phù hợp.
- Ca 12 là **Ngầm** vì chi phí sai kéo dài mà không ai phát hiện; lỗi có thể nằm ở chi phí chứ không chỉ câu trả lời.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 9 | Do người dùng | Event `input_validation_failed`; cảnh báo nếu vượt 2% tổng yêu cầu trong ngày. | Nhận diện mã sàn thương mại điện tử và tra sang mã vận đơn; nếu không tra được, hướng dẫn khách kèm ảnh. | PM trợ lý hoàn phí |
| 7 | Hệ thống | Đối soát mỗi giờ: tin nhắn “đã hoàn” phải có bản ghi sổ cái `ok` cùng `trace_id`; ngưỡng lỗi là 0 ca. | Chỉ báo “đã hoàn” khi sổ cái trả `ok`; nếu lỗi 503 sau 3 lần thì báo “đang xử lý” và chuyển nhân viên. | Kỹ sư trưởng agent |
| 18 | Ngữ cảnh | Theo dõi hàng tuần tỉ lệ yêu cầu mở lại vì số tiền nhưng kiểm tra xác nhận số tiền đúng. | Hiển thị phép tính trong tin nhắn, ví dụ `30.000 đ × 50% = 15.000 đ`. | Trưởng nhóm CSKH |
| 4 | Giới hạn hệ thống | Theo dõi event `handoff_to_staff` với `reason=thieu_du_lieu`, phân tích theo loại yêu cầu mỗi tuần. | Chuyển nhân viên kèm tóm tắt dữ liệu đã có; đưa `quoc_te` ra khỏi phạm vi pilot. | PM trợ lý hoàn phí |
| 17 | Ngầm | Kiểm tra mẫu 100 đơn mỗi tuần so với bảng giá hiện hành; ngưỡng cảnh báo khi trên 1% đơn lệch. | Xoá cache khi bảng giá đổi và ghi phiên bản bảng giá vào trace để kiểm toán. | Kế toán trưởng |
