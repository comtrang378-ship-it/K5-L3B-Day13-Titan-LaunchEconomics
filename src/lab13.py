"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Điền các chỗ ghi VIẾT Ở ĐÂY (đánh dấu TODO CP1…CP4). Dữ liệu trong hai file CSV là giả lập.
Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# TODO CP1: viết ba hàm dưới đây cho tới khi kiem_tra_dap_an_biet_truoc() in ĐẠT.
def so_lan_chay_ky_vong(p, k=None):
    """
    Số lần chạy trung bình cho 1 yêu cầu.
    k=None: chạy lại đến khi đúng.
    """
    if not 0 <= p <= 1:
        raise ValueError("p phải nằm trong khoảng [0, 1]")

    if k is None:
        if p == 0:
            return float("inf")
        return 1 / p

    if k < 1:
        raise ValueError("k phải >= 1")

    if p == 0:
        return float(k)

    return (1 - (1 - p) ** k) / p

def ti_le_thanh_cong(p, k=None):
    """
    Xác suất yêu cầu thành công sau tối đa k lần chạy.
    """
    if not 0 <= p <= 1:
        raise ValueError("p phải nằm trong khoảng [0, 1]")

    if k is None:
        return 1.0 if p > 0 else 0.0

    if k < 1:
        raise ValueError("k phải >= 1")

    return 1 - (1 - p) ** k



def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """
    Chi phí mỗi việc thành công tính theo bội số
    giá của một lần chạy.
    """
    so_lan = so_lan_chay_ky_vong(p, k)
    thanh_cong = ti_le_thanh_cong(p, k)

    if thanh_cong == 0:
        return float("inf")

    return so_lan / thanh_cong



def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
# TODO CP1: viết mo_hinh; CP2 gọi lại hàm này với tham số giá và hệ số đã đổi.
def mo_hinh(
    runs,
    reqs,
    gia_vao=26,
    gia_ra=130,
    gia_tool=15,
    luong_phut=2000,
    he_so_xem_lai=1.0,
    he_so_lam_lai=1.0,
    max_lan_chay=None
):
    """
    Tính tổng chi phí của Agent dựa trên trace.

    Token và tool tính trên mọi lần chạy.
    Thời gian xem lại và làm lại lấy từ dữ liệu simulated.
    """

    # Giới hạn số lần chạy nếu được yêu cầu
    if max_lan_chay is not None:
        runs_tinh = runs[runs["attempt"] <= max_lan_chay]
    else:
        runs_tinh = runs

    # 1. Chi phí token
    chi_phi_token_vao = (
        runs_tinh["tokens_in"].sum() / 1000 * gia_vao
    )

    chi_phi_token_ra = (
        runs_tinh["tokens_out"].sum() / 1000 * gia_ra
    )

    token = chi_phi_token_vao + chi_phi_token_ra

    # 2. Chi phí gọi tool
    tool = runs_tinh["tool_calls"].sum() * gia_tool

    # 3. Chi phí nhân viên xem lại (simulated)
    phut_xem_lai = (
        pd.to_numeric(
            reqs["phut_xem_lai_simulated"]
        ).sum()
    )

    xem_lai = (
        phut_xem_lai
        * luong_phut
        * he_so_xem_lai
    )

    # 4. Chi phí nhân viên làm lại (simulated)
    phut_lam_lai = (
        pd.to_numeric(
            reqs["phut_lam_lai_simulated"]
        ).sum()
    )

    lam_lai = (
        phut_lam_lai
        * luong_phut
        * he_so_lam_lai
    )

    # 5. Tổng chi phí
    tong = token + tool + xem_lai + lam_lai

    # 6. Số yêu cầu thành công
    thanh_cong = (
        reqs["ket_qua"] == "thanh_cong"
    ).sum()

    # 7. Chi phí mỗi việc thành công
    cps = (
        tong / thanh_cong
        if thanh_cong > 0
        else float("inf")
    )

    return {
        "token": token,
        "tool": tool,
        "xem_lai": xem_lai,
        "lam_lai": lam_lai,
        "tong": tong,
        "thanh_cong": thanh_cong,
        "cps": cps
    }


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    # TODO CP1 · Nhiệm vụ A3: tính lại theo từng giá trị của cột loai.
    # TODO CP2 · Nhiệm vụ B: đổi từng yếu tố, ghi vào bảng độ nhạy.
    # TODO CP4 · Nhiệm vụ D: cỡ mẫu.
    #   from statsmodels.stats.proportion import proportion_effectsize
    #   from statsmodels.stats.power import NormalIndPower
