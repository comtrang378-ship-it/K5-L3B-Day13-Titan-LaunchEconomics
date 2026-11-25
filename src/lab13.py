"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm.
Chạy trong thư mục src/: python3 lab13.py (cần pandas và statsmodels).
Dữ liệu trong hai file CSV là giả lập. Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import sys
from statistics import NormalDist

import pandas as pd
from statsmodels.stats.power import NormalIndPower
from statsmodels.stats.proportion import proportion_effectsize

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CHI_PHI_CO_DINH_THANG = 40_000_000
SO_YEU_CAU_THANG = 45_000


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
# Các hàm kiểm tra kinh tế của việc chạy lại.
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
# Mô hình chi phí dùng chung cho A2, A3 và các kịch bản B.
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

    if max_lan_chay is not None and max_lan_chay < 1:
        raise ValueError("max_lan_chay phải >= 1")

    request_ids = reqs["request_id"]
    runs_trong_pham_vi = runs[runs["request_id"].isin(request_ids)]
    if max_lan_chay is None:
        runs_tinh = runs_trong_pham_vi
        reqs_tinh = reqs
    else:
        runs_tinh = runs_trong_pham_vi[
            runs_trong_pham_vi["attempt"] <= max_lan_chay
        ]
        so_lan_chay = pd.to_numeric(reqs["so_lan_chay"], errors="raise")
        # Requests needing more attempts are handed to staff without simulated review/rework time.
        reqs_tinh = reqs[so_lan_chay <= max_lan_chay]

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
            reqs_tinh["phut_xem_lai_simulated"]
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
            reqs_tinh["phut_lam_lai_simulated"]
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
        reqs_tinh["ket_qua"] == "thanh_cong"
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


def co_mau_hai_ty_le(p1, p2, alpha=0.05, power=0.80):
    za = NormalDist().inv_cdf(1 - alpha / 2)
    zb = NormalDist().inv_cdf(power)
    p_bar = (p1 + p2) / 2
    variance = (
        2 * p_bar * (1 - p_bar)
    ) ** 0.5
    variance_alt = (
        p1 * (1 - p1) + p2 * (1 - p2)
    ) ** 0.5
    return math.ceil(
        (za * variance + zb * variance_alt) ** 2 / (p2 - p1) ** 2
    )


def tinh_a3(runs, reqs):
    print("\nA3 · Chi phí theo loại yêu cầu")
    print(f"{'Loại':12s} {'Yêu cầu':>9s} {'Thành công':>12s} "
          f"{'Tỉ lệ':>9s} {'Lần chạy/y/c':>14s} {'CPS (đ)':>12s}")
    for loai in ("noi_dia", "hang_nang", "quoc_te", "doi_tac"):
        reqs_loai = reqs[reqs["loai"] == loai]
        ket_qua = mo_hinh(runs, reqs_loai)
        so_yc = len(reqs_loai)
        so_chay = runs[
            runs["request_id"].isin(reqs_loai["request_id"])
        ]["attempt"].count()
        ti_le = ket_qua["thanh_cong"] / so_yc if so_yc else 0
        lan_chay_tb = so_chay / so_yc if so_yc else 0
        print(f"{loai:12s} {so_yc:9,d} {ket_qua['thanh_cong']:12,d} "
              f"{ti_le:8.1%} {lan_chay_tb:14.2f} {ket_qua['cps']:12,.0f}")


def tinh_a4(runs, reqs):
    pham_vi = reqs[reqs["loai"].isin(["noi_dia", "hang_nang"])]
    chi_phi = mo_hinh(runs, pham_vi)
    ti_le_thanh_cong_tren_tong_mau = chi_phi["thanh_cong"] / len(reqs)
    print("\nA4 · Chi phí cố định cho noi_dia + hang_nang")
    print(f"{'Khối lượng':24s} {'Thành công/tháng':>18s} "
          f"{'Cố định/việc':>16s} {'Tổng CPS':>14s}")
    for he_so in (1, 0.5):
        requests_per_month = SO_YEU_CAU_THANG * he_so
        successes_per_month = requests_per_month * ti_le_thanh_cong_tren_tong_mau
        fixed_per_success = CHI_PHI_CO_DINH_THANG / successes_per_month
        cps = chi_phi["cps"] + fixed_per_success
        label = "45.000 yêu cầu/tháng" if he_so == 1 else "Một nửa khối lượng"
        print(f"{label:24s} {successes_per_month:18,.0f} "
              f"{fixed_per_success:16,.0f} {cps:14,.0f} [simulated]")


def tinh_b(runs, reqs):
    goc = mo_hinh(runs, reqs)
    cac_kich_ban = [
        ("Giá token gấp đôi", {"gia_vao": 52, "gia_ra": 260}),
        ("Giá token giảm một nửa", {"gia_vao": 13, "gia_ra": 65}),
        ("Xem lại gấp đôi", {"he_so_xem_lai": 2}),
        ("Xem lại giảm một nửa", {"he_so_xem_lai": 0.5}),
        ("Làm lại gấp đôi", {"he_so_lam_lai": 2}),
        ("Làm lại giảm một nửa", {"he_so_lam_lai": 0.5}),
        ("Lương tăng 25%", {"luong_phut": 2500}),
        ("Tối đa 2 lần chạy", {"max_lan_chay": 2}),
        ("Chỉ 1 lần chạy", {"max_lan_chay": 1}),
    ]
    print("\nB1 · Độ nhạy")
    print(f"{'Kịch bản':28s} {'CPS (đ)':>12s} {'Thay đổi':>12s}")
    ket_qua_kich_ban = {}
    for ten, tham_so in cac_kich_ban:
        ket_qua = mo_hinh(runs, reqs, **tham_so)
        thay_doi = ket_qua["cps"] / goc["cps"] - 1
        ket_qua_kich_ban[ten] = ket_qua
        print(f"{ten:28s} {ket_qua['cps']:12,.0f} "
              f"{thay_doi:11.1%} [simulated]")

    cap_token_xem_lai = mo_hinh(
        runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2
    )
    print("\nB2 · Kịch bản kết hợp")
    print(f"Token gấp đôi + xem lại gấp đôi: "
          f"{cap_token_xem_lai['cps']:,.0f} đ/việc "
          f"({cap_token_xem_lai['cps'] / goc['cps'] - 1:.1%}) [simulated]")
    xep_hang = sorted(
        (
            ("Số ca làm lại", ket_qua_kich_ban["Làm lại gấp đôi"]["cps"] / goc["cps"] - 1),
            ("Tỉ lệ xem lại", ket_qua_kich_ban["Xem lại gấp đôi"]["cps"] / goc["cps"] - 1),
            ("Lương nhân viên", ket_qua_kich_ban["Lương tăng 25%"]["cps"] / goc["cps"] - 1),
        ),
        key=lambda item: item[1],
        reverse=True,
    )
    print("Ba yếu tố nhạy nhất: " + " > ".join(name for name, _ in xep_hang))

    print("\nB3 · Chi phí cả hệ thống khi giới hạn số lần chạy")
    print(f"{'Giới hạn':12s} {'Chi phí trợ lý':>18s} {'Không thành công':>18s} "
          f"{'Cả hệ thống':>18s} {'CPS':>12s}")
    for max_lan in (1, 2, 3):
        ket_qua = mo_hinh(runs, reqs, max_lan_chay=max_lan)
        that_bai = len(reqs) - ket_qua["thanh_cong"]
        chi_phi_he_thong = ket_qua["tong"] + that_bai * BASELINE
        print(f"{max_lan:12d} {ket_qua['tong']:18,.0f} {that_bai:18,d} "
              f"{chi_phi_he_thong:18,.0f} {ket_qua['cps']:12,.0f} [simulated]")

    tinh_b4(runs, reqs)


def tinh_b4(runs, reqs):
    pham_vi = reqs[reqs["loai"].isin(["noi_dia", "hang_nang"])]
    request_ids = pham_vi["request_id"]
    runs_pham_vi = runs[runs["request_id"].isin(request_ids)]
    so_da_chay_ok = runs_pham_vi.loc[
        runs_pham_vi["status"] == "ok", "request_id"
    ].nunique()
    so_lam_lai = (pham_vi["ket_qua"] == "lam_lai").sum()
    so_thanh_cong = (pham_vi["ket_qua"] == "thanh_cong").sum()
    token_tool = (
        runs_pham_vi["tokens_in"].sum() / 1000 * GIA_VAO
        + runs_pham_vi["tokens_out"].sum() / 1000 * GIA_RA
        + runs_pham_vi["tool_calls"].sum() * GIA_TOOL
    )
    chi_phi_xem_lai = so_da_chay_ok * 5 * LUONG_PHUT
    chi_phi_lam_lai_9 = so_lam_lai * 9 * LUONG_PHUT
    cps_9 = (token_tool + chi_phi_xem_lai + chi_phi_lam_lai_9) / so_thanh_cong
    phut_lam_lai_tb = round(pd.to_numeric(
        reqs.loc[reqs["ket_qua"] == "lam_lai", "phut_lam_lai_simulated"],
        errors="raise",
    ).mean(), 1)
    chi_phi_lam_lai_sim = so_lam_lai * phut_lam_lai_tb * LUONG_PHUT
    cps_sim = (token_tool + chi_phi_xem_lai + chi_phi_lam_lai_sim) / so_thanh_cong
    break_even_9 = (
        BASELINE * so_thanh_cong - token_tool - chi_phi_lam_lai_9
    ) / (so_da_chay_ok * LUONG_PHUT)
    break_even_sim = (
        BASELINE * so_thanh_cong - token_tool - chi_phi_lam_lai_sim
    ) / (so_da_chay_ok * LUONG_PHUT)
    print("\nB4 · Xem lại 100% trong phạm vi pilot")
    print(f"5 phút xem lại/ca, 9 phút làm lại/ca: "
          f"{cps_9:,.0f} đ = {cps_9 / BASELINE:.2f}x baseline [simulated]")
    print(f"{phut_lam_lai_tb:.1f} phút làm lại/ca theo dữ liệu: "
          f"{cps_sim:,.0f} đ = {cps_sim / BASELINE:.2f}x baseline [simulated]")
    print(f"Hoà vốn: xem lại <= {break_even_9:.1f} phút (9 phút làm lại), "
          f"hoặc <= {break_even_sim:.1f} phút ({phut_lam_lai_tb:.1f} phút làm lại).")


def tinh_d1():
    p1, p2 = 0.70, 0.75
    alpha, power, icc = 0.05, 0.80, 0.02
    n_5_diem = co_mau_hai_ty_le(p1, p2, alpha, power)
    design_effect_75 = 1 + (75 - 1) * icc
    n_raw_75 = math.ceil(n_5_diem * design_effect_75)
    n_staff_75 = math.ceil(n_raw_75 / 75)
    n_6_diem_eff = co_mau_hai_ty_le(p1, 0.76, alpha, power)
    staff_per_arm = 20
    m = 1
    while staff_per_arm * m / (1 + (m - 1) * icc) < n_6_diem_eff:
        m += 1
    design_effect_6 = 1 + (m - 1) * icc
    raw_per_arm = staff_per_arm * m
    effective_per_arm = raw_per_arm / design_effect_6
    power_at_5 = NormalIndPower().power(
        effect_size=proportion_effectsize(p1, p2),
        nobs1=n_6_diem_eff,
        alpha=alpha,
        ratio=1,
        alternative="two-sided",
    )

    print("\nD1 · Cỡ mẫu (ICC = 0,02; alpha = 0,05; power = 0,80)")
    print(f"Chia theo yêu cầu, MDE 5 điểm: {n_5_diem:,} mỗi nhánh.")
    print(f"Theo nhân viên, 75 yêu cầu/người: DE = {design_effect_75:.2f}; "
          f"{n_raw_75:,} yêu cầu/nhánh, khoảng {n_staff_75} nhân viên/nhánh "
          f"({2 * n_staff_75} tổng), không đủ 40.")
    print(f"20 nhân viên/nhánh: trần hiệu dụng 20/ICC = "
          f"{staff_per_arm / icc:,.0f} < {n_5_diem:,}, không đủ MDE 5 điểm.")
    print(f"6 depot/nhánh: trần hiệu dụng 6/ICC = {6 / icc:,.0f}.")
    print(f"MDE 6 điểm: mục tiêu hiệu dụng {n_6_diem_eff:,}/nhánh; "
          f"{staff_per_arm} nhân viên x {m} yêu cầu = {raw_per_arm:,} "
          f"yêu cầu thô/nhánh; DE = {design_effect_6:.2f}; "
          f"N hiệu dụng = {effective_per_arm:,.0f}.")
    print(f"Nếu tác động thật là 5 điểm, power xấp xỉ {power_at_5:.2f}.")


if __name__ == '__main__':
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:12s} {gia_tri:>14,.0f}')
    tinh_a3(runs, reqs)
    tinh_a4(runs, reqs)
    tinh_b(runs, reqs)
    tinh_d1()
