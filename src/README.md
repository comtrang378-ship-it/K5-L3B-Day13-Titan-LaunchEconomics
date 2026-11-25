# Source code

Code khởi đầu và dữ liệu giả lập của Lab 13. **Mọi lệnh chạy trong thư mục `src/`.**

- File bắt đầu chạy: `lab13.py` (khung code, cũng là file nộp). `lab13_starter.py` là bản gốc giống hệt để đối chiếu, không sửa.
- Cách chạy: `python3 lab13.py`.
- Input: `logix_runs.csv`, `logix_requests.csv` cùng thư mục, file yêu cầu đọc bằng `pd.read_csv('logix_requests.csv', keep_default_na=False)`.
- `lab13.py` chạy ba phép thử A1 và in kết quả A2–A4, các kịch bản B1–B4, cùng tính toán cỡ mẫu D1. Đối chiếu đầu ra với hồ sơ trong `report/team/`.
- File học viên được sửa: `lab13.py`. Không sửa hai file CSV.

## Cài đặt

Cần Python 3.10 trở lên. Lab không cần khoá API và không cần mạng trong lúc làm.

macOS / Linux:

```bash
cd src
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -c "import pandas, numpy, scipy, statsmodels; print('san sang')"
python lab13.py
```

Windows PowerShell:

```powershell
cd src
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python -c "import pandas, numpy, scipy, statsmodels; print('san sang')"
python lab13.py
```

Lệnh `python -c` kiểm tra thư viện phải in ra `san sang`.

## File trong thư mục

| File | Nội dung |
| --- | --- |
| `lab13.py` | Bài làm của nhóm: A1–A4, B1–B4 và D1; chi phí theo loại yêu cầu và giới hạn chạy lại được lọc theo `request_id` |
| `lab13_starter.py` | Bản gốc của `lab13.py`, giữ nguyên để đối chiếu. Tài liệu trong `docs/` gọi file này là "file khởi đầu" |
| `logix_runs.csv` | 1.624 lần chạy của agent |
| `logix_requests.csv` | 1.200 yêu cầu hoàn phí |
| `requirements.txt` | Thư viện cần cài |

Ý nghĩa từng cột và các công thức: [docs/du_lieu_va_cong_thuc.md](../docs/du_lieu_va_cong_thuc.md).

## Đọc dữ liệu đúng cách

```python
import pandas as pd
runs = pd.read_csv('logix_runs.csv')
reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
```

Thiếu `keep_default_na=False`, ô trống trong cột `quyet_dinh_xem_lai` bị đọc thành `NaN` và các phép so sánh phía sau sai.

## Kiểm tra trước khi nộp

- Chạy chương trình từ thư mục `src/`; ba phép thử A1 phải in **ĐẠT** với các đáp án `1,20`, `1,25`, `1,25`; đầu ra phải có A3, B1–B4 và D1.
- Đối chiếu kết quả tính từ CSV với hướng dẫn chi tiết; A2/A3 và các bảng B phải nằm trong `report/team/bang_chi_phi.md`, D1/D2 trong `report/team/pilot_plan.yaml`.
- Giữ nguyên CSV đầu vào; mọi chi phí tính từ cột `_simulated` phải được đánh dấu `simulated` trong hồ sơ.
- Kiểm tra mã YAML bằng `yaml.safe_load` và làm theo checklist trong `SUBMISSION.md` trước khi push.
