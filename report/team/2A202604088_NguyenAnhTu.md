# Báo cáo cá nhân — Nguyễn Anh Tú, 2A202604088

## 1. Thông tin thành viên

- Họ tên: Nguyễn Anh Tú
- MSSV: 2A202604088
- Email: comtrang378@gmail.com
- Vai trong nhóm: Người kiểm số kiêm tổng hợp hồ sơ; phụ trách phần lớn nhiệm vụ A–E.

## 2. Phần việc phụ trách

Phối hợp trợ lý rà soát và hoàn thiện hồ sơ nhiệm vụ A–E; đối chiếu con số với hướng dẫn, CSV và rubric; ghi rõ các giả định `simulated` cùng giới hạn của kết quả.

## 3. Đóng góp cụ thể

- Ghi kết quả A1/A2 được cung cấp và hoàn thiện bảng A3, A4, B1–B4 theo hướng dẫn đối chiếu; đánh dấu các chi phí dựa trên trường `_simulated`.
- Tổng hợp hai lượt gắn nhãn độc lập do thành viên ở vai kiểm thử và lập trình web thực hiện cho 20 ca theo năm nhóm Google PAIR; đồng thuận 20/20. Ghi quy tắc phân biệt và đề xuất phát hiện/khắc phục; tên hai thành viên cần bổ sung vào TEAM.
- Hoàn thiện D1/D2 và `pilot_plan.yaml`: nêu rõ chọn MDE 6 điểm, 20 nhân viên mỗi nhánh, 5.980 yêu cầu thô (859 hiệu dụng) mỗi nhánh, ba luật dừng và power khoảng 0,64 nếu tác động thật chỉ 5 điểm.
- Hoàn thiện `chi_so.md`, thêm event có `trace_id` và rủi ro kinh tế; phối hợp xác nhận các chỉ số 82,83% (994/1.200), 27,12% (48/177), 4,25% (51/1.200) từ CSV.
- Cập nhật hướng dẫn ở README và tổng hợp kết quả vào báo cáo nhóm.

## 4. Bằng chứng

- [Bảng chi phí A/B](./bang_chi_phi.md)
- [Bảng lỗi và cách khắc phục](./bang_loi.md)
- [Kế hoạch pilot](./pilot_plan.yaml)
- [Chỉ số, event và rủi ro](./chi_so.md)
- [Báo cáo nhóm](./group_report.md)
- Hướng dẫn đã cập nhật: [README hồ sơ nhóm](./README.md) và [README source](../../src/README.md)

Phiếu chấm chéo chưa có điểm vì chưa xác định số nhóm Titan và chưa nhận được hồ sơ của nhóm được phân công. Danh tính cụ thể của hai người gắn nhãn cần bổ sung vào TEAM.

## 5. Công cụ AI đã dùng

Đã dùng Copilot để rà tài liệu, trích nội dung đề, đối chiếu công thức và soạn bản nháp hồ sơ. Các chỉ số được kiểm tra từ CSV bằng Python/pandas, YAML bằng `yaml.safe_load`, và thay đổi Markdown bằng `git diff --check`.

## 6. Tự đánh giá

Đã phối hợp hoàn thiện và rà lại các hồ sơ số liệu, đồng thời ghi rõ phần giả lập và giới hạn không có nhóm đối chứng. Cần bổ sung thông tin, đóng góp và bằng chứng của ba thành viên còn lại; ghi danh tính hai người gắn nhãn vào TEAM; và chấm chéo khi có hồ sơ nhóm đích.
