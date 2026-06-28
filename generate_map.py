"""
generate_map.py
대전 행정동별 주거적합도 Folium 지도를 생성해 map_output/ 폴더에 저장합니다.
index.html에서 iframe으로 불러옵니다.
"""
import json, math, sys

# ── 더미 데이터 (data/dummy_data.py 내용을 직접 포함) ──────────────
DAEJEON_DISTRICTS = {
    "원동":       {"gu":"동구","lat":36.3317,"lng":127.4540,"scores":{"transport":72,"safety":65,"convenience":70,"cost":82,"education":60,"green":55,"development":45,"stability":68},"avg_rent":42,"avg_deposit":800,"avg_jeonse":9500},
    "인동":       {"gu":"동구","lat":36.3397,"lng":127.4472,"scores":{"transport":68,"safety":62,"convenience":65,"cost":85,"education":55,"green":50,"development":50,"stability":65},"avg_rent":38,"avg_deposit":700,"avg_jeonse":8500},
    "효동":       {"gu":"동구","lat":36.3257,"lng":127.4612,"scores":{"transport":55,"safety":60,"convenience":58,"cost":88,"education":52,"green":62,"development":40,"stability":62},"avg_rent":35,"avg_deposit":600,"avg_jeonse":7800},
    "가양1동":    {"gu":"동구","lat":36.3480,"lng":127.4580,"scores":{"transport":75,"safety":70,"convenience":72,"cost":75,"education":65,"green":58,"development":55,"stability":72},"avg_rent":45,"avg_deposit":900,"avg_jeonse":10500},
    "가양2동":    {"gu":"동구","lat":36.3520,"lng":127.4610,"scores":{"transport":70,"safety":68,"convenience":68,"cost":78,"education":62,"green":55,"development":52,"stability":70},"avg_rent":43,"avg_deposit":850,"avg_jeonse":10000},
    "용운동":     {"gu":"동구","lat":36.3382,"lng":127.4648,"scores":{"transport":62,"safety":65,"convenience":60,"cost":80,"education":68,"green":70,"development":48,"stability":67},"avg_rent":40,"avg_deposit":750,"avg_jeonse":9000},
    "대동":       {"gu":"동구","lat":36.3298,"lng":127.4490,"scores":{"transport":78,"safety":63,"convenience":75,"cost":80,"education":58,"green":48,"development":58,"stability":65},"avg_rent":41,"avg_deposit":780,"avg_jeonse":9200},
    "삼성동":     {"gu":"동구","lat":36.3195,"lng":127.4537,"scores":{"transport":65,"safety":61,"convenience":62,"cost":87,"education":54,"green":52,"development":43,"stability":63},"avg_rent":36,"avg_deposit":680,"avg_jeonse":8200},
    "성남동":     {"gu":"동구","lat":36.3250,"lng":127.4460,"scores":{"transport":80,"safety":66,"convenience":78,"cost":78,"education":60,"green":45,"development":62,"stability":68},"avg_rent":44,"avg_deposit":860,"avg_jeonse":10200},
    "은행선화동": {"gu":"중구","lat":36.3246,"lng":127.4247,"scores":{"transport":88,"safety":72,"convenience":92,"cost":65,"education":72,"green":48,"development":70,"stability":74},"avg_rent":58,"avg_deposit":1200,"avg_jeonse":14000},
    "목동":       {"gu":"중구","lat":36.3218,"lng":127.4190,"scores":{"transport":85,"safety":70,"convenience":88,"cost":68,"education":70,"green":45,"development":68,"stability":72},"avg_rent":55,"avg_deposit":1100,"avg_jeonse":13000},
    "중촌동":     {"gu":"중구","lat":36.3370,"lng":127.4180,"scores":{"transport":82,"safety":71,"convenience":85,"cost":70,"education":68,"green":50,"development":65,"stability":73},"avg_rent":52,"avg_deposit":1050,"avg_jeonse":12500},
    "대흥동":     {"gu":"중구","lat":36.3290,"lng":127.4220,"scores":{"transport":86,"safety":69,"convenience":90,"cost":67,"education":71,"green":46,"development":72,"stability":71},"avg_rent":56,"avg_deposit":1150,"avg_jeonse":13500},
    "문화동":     {"gu":"중구","lat":36.3310,"lng":127.4260,"scores":{"transport":84,"safety":71,"convenience":87,"cost":69,"education":73,"green":52,"development":68,"stability":73},"avg_rent":54,"avg_deposit":1080,"avg_jeonse":12800},
    "태평1동":    {"gu":"중구","lat":36.3170,"lng":127.4330,"scores":{"transport":76,"safety":66,"convenience":78,"cost":74,"education":62,"green":58,"development":55,"stability":68},"avg_rent":46,"avg_deposit":920,"avg_jeonse":11000},
    "태평2동":    {"gu":"중구","lat":36.3140,"lng":127.4370,"scores":{"transport":73,"safety":65,"convenience":75,"cost":76,"education":60,"green":60,"development":52,"stability":67},"avg_rent":44,"avg_deposit":880,"avg_jeonse":10500},
    "유천1동":    {"gu":"중구","lat":36.3090,"lng":127.4220,"scores":{"transport":70,"safety":64,"convenience":72,"cost":78,"education":58,"green":62,"development":50,"stability":66},"avg_rent":42,"avg_deposit":830,"avg_jeonse":10000},
    "도안동":     {"gu":"서구","lat":36.3680,"lng":127.3680,"scores":{"transport":70,"safety":85,"convenience":82,"cost":62,"education":82,"green":88,"development":90,"stability":83},"avg_rent":65,"avg_deposit":1500,"avg_jeonse":18000},
    "갈마1동":    {"gu":"서구","lat":36.3560,"lng":127.3780,"scores":{"transport":82,"safety":78,"convenience":85,"cost":68,"education":78,"green":72,"development":72,"stability":80},"avg_rent":58,"avg_deposit":1250,"avg_jeonse":15000},
    "갈마2동":    {"gu":"서구","lat":36.3510,"lng":127.3820,"scores":{"transport":80,"safety":76,"convenience":83,"cost":70,"education":76,"green":70,"development":70,"stability":78},"avg_rent":56,"avg_deposit":1200,"avg_jeonse":14500},
    "월평1동":    {"gu":"서구","lat":36.3620,"lng":127.3870,"scores":{"transport":83,"safety":80,"convenience":86,"cost":67,"education":80,"green":74,"development":68,"stability":81},"avg_rent":60,"avg_deposit":1300,"avg_jeonse":15500},
    "월평2동":    {"gu":"서구","lat":36.3660,"lng":127.3920,"scores":{"transport":85,"safety":82,"convenience":88,"cost":65,"education":82,"green":72,"development":70,"stability":82},"avg_rent":62,"avg_deposit":1350,"avg_jeonse":16000},
    "월평3동":    {"gu":"서구","lat":36.3700,"lng":127.3960,"scores":{"transport":84,"safety":81,"convenience":87,"cost":66,"education":81,"green":73,"development":71,"stability":81},"avg_rent":61,"avg_deposit":1320,"avg_jeonse":15800},
    "둔산1동":    {"gu":"서구","lat":36.3510,"lng":127.3870,"scores":{"transport":90,"safety":83,"convenience":92,"cost":60,"education":88,"green":78,"development":75,"stability":85},"avg_rent":72,"avg_deposit":1700,"avg_jeonse":20000},
    "둔산2동":    {"gu":"서구","lat":36.3560,"lng":127.3920,"scores":{"transport":92,"safety":85,"convenience":94,"cost":58,"education":90,"green":80,"development":77,"stability":87},"avg_rent":75,"avg_deposit":1800,"avg_jeonse":21000},
    "둔산3동":    {"gu":"서구","lat":36.3600,"lng":127.3960,"scores":{"transport":91,"safety":84,"convenience":93,"cost":59,"education":89,"green":79,"development":76,"stability":86},"avg_rent":73,"avg_deposit":1750,"avg_jeonse":20500},
    "탄방동":     {"gu":"서구","lat":36.3450,"lng":127.4020,"scores":{"transport":85,"safety":78,"convenience":87,"cost":64,"education":80,"green":70,"development":72,"stability":80},"avg_rent":63,"avg_deposit":1380,"avg_jeonse":16500},
    "내동":       {"gu":"서구","lat":36.3390,"lng":127.4080,"scores":{"transport":82,"safety":76,"convenience":84,"cost":66,"education":78,"green":68,"development":70,"stability":78},"avg_rent":60,"avg_deposit":1300,"avg_jeonse":15500},
    "도마1동":    {"gu":"서구","lat":36.3320,"lng":127.4010,"scores":{"transport":80,"safety":74,"convenience":82,"cost":68,"education":74,"green":62,"development":68,"stability":76},"avg_rent":55,"avg_deposit":1100,"avg_jeonse":13200},
    "도마2동":    {"gu":"서구","lat":36.3360,"lng":127.4050,"scores":{"transport":81,"safety":75,"convenience":83,"cost":67,"education":75,"green":63,"development":69,"stability":77},"avg_rent":56,"avg_deposit":1120,"avg_jeonse":13500},
    "복수동":     {"gu":"서구","lat":36.3200,"lng":127.4120,"scores":{"transport":76,"safety":72,"convenience":78,"cost":72,"education":70,"green":65,"development":62,"stability":74},"avg_rent":50,"avg_deposit":1000,"avg_jeonse":12000},
    "정림동":     {"gu":"서구","lat":36.3350,"lng":127.3770,"scores":{"transport":75,"safety":72,"convenience":77,"cost":74,"education":70,"green":66,"development":62,"stability":74},"avg_rent":49,"avg_deposit":980,"avg_jeonse":11800},
    "변동":       {"gu":"서구","lat":36.3420,"lng":127.3920,"scores":{"transport":78,"safety":74,"convenience":80,"cost":72,"education":72,"green":68,"development":65,"stability":76},"avg_rent":52,"avg_deposit":1050,"avg_jeonse":12800},
    "유성동":     {"gu":"유성구","lat":36.3625,"lng":127.3563,"scores":{"transport":80,"safety":78,"convenience":85,"cost":65,"education":82,"green":80,"development":75,"stability":80},"avg_rent":60,"avg_deposit":1300,"avg_jeonse":15500},
    "봉명동":     {"gu":"유성구","lat":36.3695,"lng":127.3493,"scores":{"transport":83,"safety":80,"convenience":88,"cost":63,"education":85,"green":78,"development":77,"stability":82},"avg_rent":63,"avg_deposit":1400,"avg_jeonse":16500},
    "노은1동":    {"gu":"유성구","lat":36.4020,"lng":127.3380,"scores":{"transport":78,"safety":82,"convenience":80,"cost":68,"education":85,"green":82,"development":72,"stability":82},"avg_rent":58,"avg_deposit":1250,"avg_jeonse":15000},
    "노은2동":    {"gu":"유성구","lat":36.4070,"lng":127.3450,"scores":{"transport":80,"safety":84,"convenience":82,"cost":67,"education":87,"green":83,"development":74,"stability":84},"avg_rent":60,"avg_deposit":1300,"avg_jeonse":15500},
    "노은3동":    {"gu":"유성구","lat":36.4120,"lng":127.3510,"scores":{"transport":76,"safety":83,"convenience":78,"cost":69,"education":86,"green":84,"development":73,"stability":83},"avg_rent":57,"avg_deposit":1200,"avg_jeonse":14500},
    "신성동":     {"gu":"유성구","lat":36.3760,"lng":127.3490,"scores":{"transport":75,"safety":79,"convenience":77,"cost":70,"education":83,"green":80,"development":70,"stability":80},"avg_rent":55,"avg_deposit":1150,"avg_jeonse":13800},
    "전민동":     {"gu":"유성구","lat":36.4000,"lng":127.3720,"scores":{"transport":72,"safety":82,"convenience":75,"cost":67,"education":88,"green":82,"development":73,"stability":83},"avg_rent":58,"avg_deposit":1250,"avg_jeonse":15000},
    "반석동":     {"gu":"유성구","lat":36.4180,"lng":127.3620,"scores":{"transport":82,"safety":83,"convenience":80,"cost":66,"education":86,"green":80,"development":75,"stability":83},"avg_rent":60,"avg_deposit":1300,"avg_jeonse":15500},
    "관평동":     {"gu":"유성구","lat":36.4320,"lng":127.3920,"scores":{"transport":68,"safety":80,"convenience":72,"cost":70,"education":80,"green":78,"development":78,"stability":80},"avg_rent":55,"avg_deposit":1100,"avg_jeonse":13200},
    "온천1동":    {"gu":"유성구","lat":36.3610,"lng":127.3420,"scores":{"transport":85,"safety":78,"convenience":87,"cost":64,"education":80,"green":75,"development":76,"stability":80},"avg_rent":64,"avg_deposit":1420,"avg_jeonse":17000},
    "온천2동":    {"gu":"유성구","lat":36.3660,"lng":127.3470,"scores":{"transport":83,"safety":79,"convenience":85,"cost":65,"education":81,"green":76,"development":74,"stability":81},"avg_rent":62,"avg_deposit":1370,"avg_jeonse":16500},
    "지족동":     {"gu":"유성구","lat":36.3990,"lng":127.3500,"scores":{"transport":75,"safety":81,"convenience":78,"cost":68,"education":84,"green":81,"development":72,"stability":81},"avg_rent":57,"avg_deposit":1200,"avg_jeonse":14500},
    "어은동":     {"gu":"유성구","lat":36.3730,"lng":127.3600,"scores":{"transport":78,"safety":80,"convenience":80,"cost":66,"education":85,"green":78,"development":72,"stability":80},"avg_rent":58,"avg_deposit":1230,"avg_jeonse":14800},
    "궁동":       {"gu":"유성구","lat":36.3680,"lng":127.3650,"scores":{"transport":76,"safety":78,"convenience":78,"cost":68,"education":82,"green":76,"development":70,"stability":79},"avg_rent":55,"avg_deposit":1150,"avg_jeonse":13800},
    "덕명동":     {"gu":"유성구","lat":36.3780,"lng":127.3380,"scores":{"transport":72,"safety":80,"convenience":74,"cost":70,"education":82,"green":80,"development":72,"stability":80},"avg_rent":54,"avg_deposit":1100,"avg_jeonse":13200},
    "장대동":     {"gu":"유성구","lat":36.3710,"lng":127.3550,"scores":{"transport":79,"safety":79,"convenience":81,"cost":67,"education":81,"green":77,"development":71,"stability":79},"avg_rent":57,"avg_deposit":1200,"avg_jeonse":14400},
    "화암동":     {"gu":"유성구","lat":36.3610,"lng":127.3240,"scores":{"transport":60,"safety":76,"convenience":63,"cost":78,"education":73,"green":85,"development":63,"stability":76},"avg_rent":46,"avg_deposit":920,"avg_jeonse":11000},
    "오정동":     {"gu":"대덕구","lat":36.3640,"lng":127.4150,"scores":{"transport":72,"safety":68,"convenience":74,"cost":78,"education":65,"green":60,"development":58,"stability":70},"avg_rent":47,"avg_deposit":950,"avg_jeonse":11500},
    "중리동":     {"gu":"대덕구","lat":36.3710,"lng":127.4220,"scores":{"transport":70,"safety":66,"convenience":72,"cost":80,"education":62,"green":58,"development":55,"stability":68},"avg_rent":44,"avg_deposit":880,"avg_jeonse":10800},
    "석봉동":     {"gu":"대덕구","lat":36.3780,"lng":127.4290,"scores":{"transport":65,"safety":65,"convenience":68,"cost":82,"education":60,"green":62,"development":52,"stability":66},"avg_rent":41,"avg_deposit":820,"avg_jeonse":9800},
    "법동":       {"gu":"대덕구","lat":36.3850,"lng":127.4360,"scores":{"transport":62,"safety":64,"convenience":65,"cost":84,"education":58,"green":65,"development":50,"stability":65},"avg_rent":39,"avg_deposit":780,"avg_jeonse":9300},
    "신탄진동":   {"gu":"대덕구","lat":36.4380,"lng":127.4020,"scores":{"transport":68,"safety":67,"convenience":70,"cost":82,"education":62,"green":70,"development":62,"stability":68},"avg_rent":43,"avg_deposit":850,"avg_jeonse":10200},
    "회덕동":     {"gu":"대덕구","lat":36.4120,"lng":127.4180,"scores":{"transport":60,"safety":65,"convenience":63,"cost":85,"education":58,"green":68,"development":55,"stability":66},"avg_rent":38,"avg_deposit":750,"avg_jeonse":9000},
    "비래동":     {"gu":"대덕구","lat":36.3720,"lng":127.4500,"scores":{"transport":63,"safety":66,"convenience":65,"cost":83,"education":60,"green":65,"development":53,"stability":66},"avg_rent":40,"avg_deposit":800,"avg_jeonse":9500},
}

def compute_composite(scores, weights=None):
    if weights is None:
        weights = {k:1 for k in scores}
    total_w = sum(weights.values())
    if total_w == 0:
        return 0
    return sum(scores[k] * weights.get(k, 1) for k in scores) / total_w

def score_to_color(score):
    """0~100 점수를 HSL 색상으로 변환 (저→빨강, 고→파랑)"""
    # 50점 미만: 빨강계열, 50~70: 노랑계열, 70~85: 연두계열, 85+: 파랑계열
    if score >= 85:
        return "#12a6ff"   # 파랑 (최고)
    elif score >= 75:
        return "#4dd4ac"   # 청록
    elif score >= 65:
        return "#ffd043"   # 노랑
    elif score >= 55:
        return "#ff9f43"   # 주황
    else:
        return "#ff6b6b"   # 빨강

def generate_base_map():
    try:
        import folium
    except ImportError:
        print("folium 없음 – 스킵")
        return

    import os
    os.makedirs("map_output", exist_ok=True)

    # ── 기본 지도 (OSM) ──
    m = folium.Map(
        location=[36.3504, 127.3845],
        zoom_start=12,
        tiles="OpenStreetMap",
        attr="© OpenStreetMap contributors"
    )

    # ── 각 행정동 마커 ──
    for dong, info in DAEJEON_DISTRICTS.items():
        composite = compute_composite(info["scores"])
        color = score_to_color(composite)

        popup_html = f"""
        <div style="font-family:'Noto Sans KR',sans-serif;min-width:200px;padding:4px;">
          <div style="font-weight:900;font-size:15px;color:#12a6ff;border-bottom:2px solid #12a6ff;padding-bottom:6px;margin-bottom:8px;">{dong}</div>
          <div style="color:#555;font-size:12px;margin-bottom:6px;">{info['gu']}</div>
          <div style="font-size:13px;margin-bottom:4px;">🏆 종합 점수 <b style="color:#12a6ff;font-size:16px;">{composite:.0f}</b>점</div>
          <hr style="border:1px solid #eee;margin:8px 0;">
          <table style="width:100%;font-size:11px;border-collapse:collapse;">
            <tr><td>🚌 교통</td><td style="text-align:right;font-weight:700;">{info['scores']['transport']}점</td></tr>
            <tr><td>🔒 안전</td><td style="text-align:right;font-weight:700;">{info['scores']['safety']}점</td></tr>
            <tr><td>🏪 편의</td><td style="text-align:right;font-weight:700;">{info['scores']['convenience']}점</td></tr>
            <tr><td>💰 비용</td><td style="text-align:right;font-weight:700;">{info['scores']['cost']}점</td></tr>
            <tr><td>🏫 교육</td><td style="text-align:right;font-weight:700;">{info['scores']['education']}점</td></tr>
            <tr><td>🌳 녹지</td><td style="text-align:right;font-weight:700;">{info['scores']['green']}점</td></tr>
            <tr><td>🏗️ 개발</td><td style="text-align:right;font-weight:700;">{info['scores']['development']}점</td></tr>
            <tr><td>🏠 안정</td><td style="text-align:right;font-weight:700;">{info['scores']['stability']}점</td></tr>
          </table>
          <hr style="border:1px solid #eee;margin:8px 0;">
          <div style="font-size:11px;">
            <div>💵 평균 월세: <b>{info['avg_rent']}만원</b></div>
            <div>📋 평균 보증금: <b>{info['avg_deposit']}만원</b></div>
            <div>🏡 평균 전세: <b>{info['avg_jeonse']:,}만원</b></div>
          </div>
        </div>
        """

        folium.CircleMarker(
            location=[info["lat"], info["lng"]],
            radius=max(8, min(20, composite / 5.5)),
            color=color,
            fill=True,
            fill_color=color,
            fill_opacity=0.75,
            weight=2,
            popup=folium.Popup(popup_html, max_width=250),
            tooltip=f"{dong} ({composite:.0f}점)"
        ).add_to(m)

    m.save("map_output/base_map.html")
    print("✅ base_map.html 생성 완료")


def generate_weighted_map(weights, output_name="weighted_map.html"):
    try:
        import folium
    except ImportError:
        return []

    import os
    os.makedirs("map_output", exist_ok=True)

    m = folium.Map(
        location=[36.3504, 127.3845],
        zoom_start=12,
        tiles="OpenStreetMap",
        attr="© OpenStreetMap contributors"
    )

    scored = []
    for dong, info in DAEJEON_DISTRICTS.items():
        composite = compute_composite(info["scores"], weights)
        scored.append((dong, composite, info))

    scored.sort(key=lambda x: -x[1])
    top5 = scored[:5]
    top5_names = {d for d, _, _ in top5}

    for dong, composite, info in scored:
        color = score_to_color(composite)
        is_top = dong in top5_names
        rank = next((i+1 for i, (d,_,_) in enumerate(top5) if d==dong), None)

        popup_html = f"""
        <div style="font-family:'Noto Sans KR',sans-serif;min-width:200px;padding:4px;">
          <div style="font-weight:900;font-size:15px;color:#12a6ff;border-bottom:2px solid #12a6ff;padding-bottom:6px;margin-bottom:8px;">
            {f'🥇#{rank} ' if rank else ''}{dong}
          </div>
          <div style="color:#555;font-size:12px;margin-bottom:6px;">{info['gu']}</div>
          <div style="font-size:13px;margin-bottom:4px;">🏆 맞춤 점수 <b style="color:#12a6ff;font-size:16px;">{composite:.1f}</b>점</div>
          <hr style="border:1px solid #eee;margin:8px 0;">
          <div style="font-size:11px;">
            <div>💵 평균 월세: <b>{info['avg_rent']}만원</b></div>
            <div>📋 평균 보증금: <b>{info['avg_deposit']}만원</b></div>
          </div>
        </div>
        """

        radius = 22 if is_top else max(7, min(16, composite/6))
        weight = 3 if is_top else 1.5

        folium.CircleMarker(
            location=[info["lat"], info["lng"]],
            radius=radius,
            color="#ffd043" if is_top else color,
            fill=True,
            fill_color=color,
            fill_opacity=0.85 if is_top else 0.65,
            weight=weight,
            popup=folium.Popup(popup_html, max_width=250),
            tooltip=f"{'⭐ ' if is_top else ''}{dong} ({composite:.1f}점)"
        ).add_to(m)

    m.save(f"map_output/{output_name}")
    return top5


if __name__ == "__main__":
    generate_base_map()
    default_weights = {k:1 for k in ["transport","safety","convenience","cost","education","green","development","stability"]}
    top5 = generate_weighted_map(default_weights)
    print("TOP5:", [(d, f"{s:.1f}") for d,s,_ in top5])
    print("✅ 모든 지도 생성 완료!")
