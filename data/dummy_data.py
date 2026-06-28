# data/dummy_data.py
# 대전 행정동별 더미 데이터 (실제 공공데이터 구조를 모방)

DAEJEON_DISTRICTS = {
    # 동구
    "원동": {"gu": "동구", "lat": 36.3317, "lng": 127.4540, "scores": {"transport": 72, "safety": 65, "convenience": 70, "cost": 82, "education": 60, "green": 55, "development": 45, "stability": 68}, "avg_rent": 42, "avg_deposit": 800, "avg_jeonse": 9500},
    "인동": {"gu": "동구", "lat": 36.3397, "lng": 127.4472, "scores": {"transport": 68, "safety": 62, "convenience": 65, "cost": 85, "education": 55, "green": 50, "development": 50, "stability": 65}, "avg_rent": 38, "avg_deposit": 700, "avg_jeonse": 8500},
    "효동": {"gu": "동구", "lat": 36.3257, "lng": 127.4612, "scores": {"transport": 55, "safety": 60, "convenience": 58, "cost": 88, "education": 52, "green": 62, "development": 40, "stability": 62}, "avg_rent": 35, "avg_deposit": 600, "avg_jeonse": 7800},
    "가양1동": {"gu": "동구", "lat": 36.3480, "lng": 127.4580, "scores": {"transport": 75, "safety": 70, "convenience": 72, "cost": 75, "education": 65, "green": 58, "development": 55, "stability": 72}, "avg_rent": 45, "avg_deposit": 900, "avg_jeonse": 10500},
    "가양2동": {"gu": "동구", "lat": 36.3520, "lng": 127.4610, "scores": {"transport": 70, "safety": 68, "convenience": 68, "cost": 78, "education": 62, "green": 55, "development": 52, "stability": 70}, "avg_rent": 43, "avg_deposit": 850, "avg_jeonse": 10000},
    "용운동": {"gu": "동구", "lat": 36.3382, "lng": 127.4648, "scores": {"transport": 62, "safety": 65, "convenience": 60, "cost": 80, "education": 68, "green": 70, "development": 48, "stability": 67}, "avg_rent": 40, "avg_deposit": 750, "avg_jeonse": 9000},
    "대동": {"gu": "동구", "lat": 36.3298, "lng": 127.4490, "scores": {"transport": 78, "safety": 63, "convenience": 75, "cost": 80, "education": 58, "green": 48, "development": 58, "stability": 65}, "avg_rent": 41, "avg_deposit": 780, "avg_jeonse": 9200},
    "삼성동": {"gu": "동구", "lat": 36.3195, "lng": 127.4537, "scores": {"transport": 65, "safety": 61, "convenience": 62, "cost": 87, "education": 54, "green": 52, "development": 43, "stability": 63}, "avg_rent": 36, "avg_deposit": 680, "avg_jeonse": 8200},
    "자양동": {"gu": "동구", "lat": 36.3150, "lng": 127.4570, "scores": {"transport": 58, "safety": 63, "convenience": 57, "cost": 90, "education": 50, "green": 65, "development": 38, "stability": 60}, "avg_rent": 33, "avg_deposit": 600, "avg_jeonse": 7500},
    "판암1동": {"gu": "동구", "lat": 36.3080, "lng": 127.4645, "scores": {"transport": 60, "safety": 62, "convenience": 60, "cost": 85, "education": 55, "green": 60, "development": 45, "stability": 64}, "avg_rent": 37, "avg_deposit": 700, "avg_jeonse": 8500},
    "판암2동": {"gu": "동구", "lat": 36.3050, "lng": 127.4700, "scores": {"transport": 55, "safety": 60, "convenience": 55, "cost": 88, "education": 52, "green": 62, "development": 42, "stability": 61}, "avg_rent": 35, "avg_deposit": 650, "avg_jeonse": 8000},
    "신흥동": {"gu": "동구", "lat": 36.3175, "lng": 127.4490, "scores": {"transport": 72, "safety": 64, "convenience": 68, "cost": 82, "education": 58, "green": 50, "development": 52, "stability": 66}, "avg_rent": 40, "avg_deposit": 760, "avg_jeonse": 9100},
    "성남동": {"gu": "동구", "lat": 36.3250, "lng": 127.4460, "scores": {"transport": 80, "safety": 66, "convenience": 78, "cost": 78, "education": 60, "green": 45, "development": 62, "stability": 68}, "avg_rent": 44, "avg_deposit": 860, "avg_jeonse": 10200},

    # 중구
    "은행선화동": {"gu": "중구", "lat": 36.3246, "lng": 127.4247, "scores": {"transport": 88, "safety": 72, "convenience": 92, "cost": 65, "education": 72, "green": 48, "development": 70, "stability": 74}, "avg_rent": 58, "avg_deposit": 1200, "avg_jeonse": 14000},
    "목동": {"gu": "중구", "lat": 36.3218, "lng": 127.4190, "scores": {"transport": 85, "safety": 70, "convenience": 88, "cost": 68, "education": 70, "green": 45, "development": 68, "stability": 72}, "avg_rent": 55, "avg_deposit": 1100, "avg_jeonse": 13000},
    "중촌동": {"gu": "중구", "lat": 36.3370, "lng": 127.4180, "scores": {"transport": 82, "safety": 71, "convenience": 85, "cost": 70, "education": 68, "green": 50, "development": 65, "stability": 73}, "avg_rent": 52, "avg_deposit": 1050, "avg_jeonse": 12500},
    "대흥동": {"gu": "중구", "lat": 36.3290, "lng": 127.4220, "scores": {"transport": 86, "safety": 69, "convenience": 90, "cost": 67, "education": 71, "green": 46, "development": 72, "stability": 71}, "avg_rent": 56, "avg_deposit": 1150, "avg_jeonse": 13500},
    "문화동": {"gu": "중구", "lat": 36.3310, "lng": 127.4260, "scores": {"transport": 84, "safety": 71, "convenience": 87, "cost": 69, "education": 73, "green": 52, "development": 68, "stability": 73}, "avg_rent": 54, "avg_deposit": 1080, "avg_jeonse": 12800},
    "부사동": {"gu": "중구", "lat": 36.3230, "lng": 127.4300, "scores": {"transport": 80, "safety": 68, "convenience": 82, "cost": 72, "education": 65, "green": 55, "development": 60, "stability": 70}, "avg_rent": 49, "avg_deposit": 980, "avg_jeonse": 11500},
    "태평1동": {"gu": "중구", "lat": 36.3170, "lng": 127.4330, "scores": {"transport": 76, "safety": 66, "convenience": 78, "cost": 74, "education": 62, "green": 58, "development": 55, "stability": 68}, "avg_rent": 46, "avg_deposit": 920, "avg_jeonse": 11000},
    "태평2동": {"gu": "중구", "lat": 36.3140, "lng": 127.4370, "scores": {"transport": 73, "safety": 65, "convenience": 75, "cost": 76, "education": 60, "green": 60, "development": 52, "stability": 67}, "avg_rent": 44, "avg_deposit": 880, "avg_jeonse": 10500},
    "유천1동": {"gu": "중구", "lat": 36.3090, "lng": 127.4220, "scores": {"transport": 70, "safety": 64, "convenience": 72, "cost": 78, "education": 58, "green": 62, "development": 50, "stability": 66}, "avg_rent": 42, "avg_deposit": 830, "avg_jeonse": 10000},
    "유천2동": {"gu": "중구", "lat": 36.3060, "lng": 127.4260, "scores": {"transport": 68, "safety": 63, "convenience": 70, "cost": 80, "education": 56, "green": 64, "development": 48, "stability": 65}, "avg_rent": 40, "avg_deposit": 800, "avg_jeonse": 9600},
    "사정동": {"gu": "중구", "lat": 36.3020, "lng": 127.4300, "scores": {"transport": 65, "safety": 62, "convenience": 67, "cost": 82, "education": 55, "green": 66, "development": 46, "stability": 64}, "avg_rent": 38, "avg_deposit": 760, "avg_jeonse": 9200},

    # 서구
    "도안동": {"gu": "서구", "lat": 36.3680, "lng": 127.3680, "scores": {"transport": 70, "safety": 85, "convenience": 82, "cost": 62, "education": 82, "green": 88, "development": 90, "stability": 83}, "avg_rent": 65, "avg_deposit": 1500, "avg_jeonse": 18000},
    "갈마1동": {"gu": "서구", "lat": 36.3560, "lng": 127.3780, "scores": {"transport": 82, "safety": 78, "convenience": 85, "cost": 68, "education": 78, "green": 72, "development": 72, "stability": 80}, "avg_rent": 58, "avg_deposit": 1250, "avg_jeonse": 15000},
    "갈마2동": {"gu": "서구", "lat": 36.3510, "lng": 127.3820, "scores": {"transport": 80, "safety": 76, "convenience": 83, "cost": 70, "education": 76, "green": 70, "development": 70, "stability": 78}, "avg_rent": 56, "avg_deposit": 1200, "avg_jeonse": 14500},
    "월평1동": {"gu": "서구", "lat": 36.3620, "lng": 127.3870, "scores": {"transport": 83, "safety": 80, "convenience": 86, "cost": 67, "education": 80, "green": 74, "development": 68, "stability": 81}, "avg_rent": 60, "avg_deposit": 1300, "avg_jeonse": 15500},
    "월평2동": {"gu": "서구", "lat": 36.3660, "lng": 127.3920, "scores": {"transport": 85, "safety": 82, "convenience": 88, "cost": 65, "education": 82, "green": 72, "development": 70, "stability": 82}, "avg_rent": 62, "avg_deposit": 1350, "avg_jeonse": 16000},
    "월평3동": {"gu": "서구", "lat": 36.3700, "lng": 127.3960, "scores": {"transport": 84, "safety": 81, "convenience": 87, "cost": 66, "education": 81, "green": 73, "development": 71, "stability": 81}, "avg_rent": 61, "avg_deposit": 1320, "avg_jeonse": 15800},
    "둔산1동": {"gu": "서구", "lat": 36.3510, "lng": 127.3870, "scores": {"transport": 90, "safety": 83, "convenience": 92, "cost": 60, "education": 88, "green": 78, "development": 75, "stability": 85}, "avg_rent": 72, "avg_deposit": 1700, "avg_jeonse": 20000},
    "둔산2동": {"gu": "서구", "lat": 36.3560, "lng": 127.3920, "scores": {"transport": 92, "safety": 85, "convenience": 94, "cost": 58, "education": 90, "green": 80, "development": 77, "stability": 87}, "avg_rent": 75, "avg_deposit": 1800, "avg_jeonse": 21000},
    "둔산3동": {"gu": "서구", "lat": 36.3600, "lng": 127.3960, "scores": {"transport": 91, "safety": 84, "convenience": 93, "cost": 59, "education": 89, "green": 79, "development": 76, "stability": 86}, "avg_rent": 73, "avg_deposit": 1750, "avg_jeonse": 20500},
    "변동": {"gu": "서구", "lat": 36.3420, "lng": 127.3920, "scores": {"transport": 78, "safety": 74, "convenience": 80, "cost": 72, "education": 72, "green": 68, "development": 65, "stability": 76}, "avg_rent": 52, "avg_deposit": 1050, "avg_jeonse": 12800},
    "정림동": {"gu": "서구", "lat": 36.3350, "lng": 127.3770, "scores": {"transport": 75, "safety": 72, "convenience": 77, "cost": 74, "education": 70, "green": 66, "development": 62, "stability": 74}, "avg_rent": 49, "avg_deposit": 980, "avg_jeonse": 11800},
    "용문동": {"gu": "서구", "lat": 36.3280, "lng": 127.3830, "scores": {"transport": 72, "safety": 70, "convenience": 74, "cost": 76, "education": 68, "green": 64, "development": 58, "stability": 72}, "avg_rent": 46, "avg_deposit": 920, "avg_jeonse": 11000},
    "탄방동": {"gu": "서구", "lat": 36.3450, "lng": 127.4020, "scores": {"transport": 85, "safety": 78, "convenience": 87, "cost": 64, "education": 80, "green": 70, "development": 72, "stability": 80}, "avg_rent": 63, "avg_deposit": 1380, "avg_jeonse": 16500},
    "내동": {"gu": "서구", "lat": 36.3390, "lng": 127.4080, "scores": {"transport": 82, "safety": 76, "convenience": 84, "cost": 66, "education": 78, "green": 68, "development": 70, "stability": 78}, "avg_rent": 60, "avg_deposit": 1300, "avg_jeonse": 15500},
    "가수원동": {"gu": "서구", "lat": 36.3250, "lng": 127.3720, "scores": {"transport": 62, "safety": 68, "convenience": 65, "cost": 82, "education": 62, "green": 72, "development": 55, "stability": 68}, "avg_rent": 42, "avg_deposit": 820, "avg_jeonse": 9800},
    "도마1동": {"gu": "서구", "lat": 36.3320, "lng": 127.4010, "scores": {"transport": 80, "safety": 74, "convenience": 82, "cost": 68, "education": 74, "green": 62, "development": 68, "stability": 76}, "avg_rent": 55, "avg_deposit": 1100, "avg_jeonse": 13200},
    "도마2동": {"gu": "서구", "lat": 36.3360, "lng": 127.4050, "scores": {"transport": 81, "safety": 75, "convenience": 83, "cost": 67, "education": 75, "green": 63, "development": 69, "stability": 77}, "avg_rent": 56, "avg_deposit": 1120, "avg_jeonse": 13500},
    "복수동": {"gu": "서구", "lat": 36.3200, "lng": 127.4120, "scores": {"transport": 76, "safety": 72, "convenience": 78, "cost": 72, "education": 70, "green": 65, "development": 62, "stability": 74}, "avg_rent": 50, "avg_deposit": 1000, "avg_jeonse": 12000},
    "기성동": {"gu": "서구", "lat": 36.3160, "lng": 127.3870, "scores": {"transport": 65, "safety": 70, "convenience": 67, "cost": 80, "education": 65, "green": 75, "development": 52, "stability": 70}, "avg_rent": 44, "avg_deposit": 860, "avg_jeonse": 10200},

    # 유성구
    "유성동": {"gu": "유성구", "lat": 36.3625, "lng": 127.3563, "scores": {"transport": 80, "safety": 78, "convenience": 85, "cost": 65, "education": 82, "green": 80, "development": 75, "stability": 80}, "avg_rent": 60, "avg_deposit": 1300, "avg_jeonse": 15500},
    "봉명동": {"gu": "유성구", "lat": 36.3695, "lng": 127.3493, "scores": {"transport": 83, "safety": 80, "convenience": 88, "cost": 63, "education": 85, "green": 78, "development": 77, "stability": 82}, "avg_rent": 63, "avg_deposit": 1400, "avg_jeonse": 16500},
    "구즉동": {"gu": "유성구", "lat": 36.3880, "lng": 127.3070, "scores": {"transport": 58, "safety": 75, "convenience": 62, "cost": 80, "education": 70, "green": 85, "development": 65, "stability": 74}, "avg_rent": 45, "avg_deposit": 900, "avg_jeonse": 10800},
    "노은1동": {"gu": "유성구", "lat": 36.4020, "lng": 127.3380, "scores": {"transport": 78, "safety": 82, "convenience": 80, "cost": 68, "education": 85, "green": 82, "development": 72, "stability": 82}, "avg_rent": 58, "avg_deposit": 1250, "avg_jeonse": 15000},
    "노은2동": {"gu": "유성구", "lat": 36.4070, "lng": 127.3450, "scores": {"transport": 80, "safety": 84, "convenience": 82, "cost": 67, "education": 87, "green": 83, "development": 74, "stability": 84}, "avg_rent": 60, "avg_deposit": 1300, "avg_jeonse": 15500},
    "노은3동": {"gu": "유성구", "lat": 36.4120, "lng": 127.3510, "scores": {"transport": 76, "safety": 83, "convenience": 78, "cost": 69, "education": 86, "green": 84, "development": 73, "stability": 83}, "avg_rent": 57, "avg_deposit": 1200, "avg_jeonse": 14500},
    "신성동": {"gu": "유성구", "lat": 36.3760, "lng": 127.3490, "scores": {"transport": 75, "safety": 79, "convenience": 77, "cost": 70, "education": 83, "green": 80, "development": 70, "stability": 80}, "avg_rent": 55, "avg_deposit": 1150, "avg_jeonse": 13800},
    "전민동": {"gu": "유성구", "lat": 36.4000, "lng": 127.3720, "scores": {"transport": 72, "safety": 82, "convenience": 75, "cost": 67, "education": 88, "green": 82, "development": 73, "stability": 83}, "avg_rent": 58, "avg_deposit": 1250, "avg_jeonse": 15000},
    "반석동": {"gu": "유성구", "lat": 36.4180, "lng": 127.3620, "scores": {"transport": 82, "safety": 83, "convenience": 80, "cost": 66, "education": 86, "green": 80, "development": 75, "stability": 83}, "avg_rent": 60, "avg_deposit": 1300, "avg_jeonse": 15500},
    "관평동": {"gu": "유성구", "lat": 36.4320, "lng": 127.3920, "scores": {"transport": 68, "safety": 80, "convenience": 72, "cost": 70, "education": 80, "green": 78, "development": 78, "stability": 80}, "avg_rent": 55, "avg_deposit": 1100, "avg_jeonse": 13200},
    "탑립동": {"gu": "유성구", "lat": 36.3940, "lng": 127.4050, "scores": {"transport": 65, "safety": 78, "convenience": 68, "cost": 72, "education": 77, "green": 75, "development": 70, "stability": 78}, "avg_rent": 50, "avg_deposit": 1000, "avg_jeonse": 12000},
    "온천1동": {"gu": "유성구", "lat": 36.3610, "lng": 127.3420, "scores": {"transport": 85, "safety": 78, "convenience": 87, "cost": 64, "education": 80, "green": 75, "development": 76, "stability": 80}, "avg_rent": 64, "avg_deposit": 1420, "avg_jeonse": 17000},
    "온천2동": {"gu": "유성구", "lat": 36.3660, "lng": 127.3470, "scores": {"transport": 83, "safety": 79, "convenience": 85, "cost": 65, "education": 81, "green": 76, "development": 74, "stability": 81}, "avg_rent": 62, "avg_deposit": 1370, "avg_jeonse": 16500},
    "지족동": {"gu": "유성구", "lat": 36.3990, "lng": 127.3500, "scores": {"transport": 75, "safety": 81, "convenience": 78, "cost": 68, "education": 84, "green": 81, "development": 72, "stability": 81}, "avg_rent": 57, "avg_deposit": 1200, "avg_jeonse": 14500},
    "어은동": {"gu": "유성구", "lat": 36.3730, "lng": 127.3600, "scores": {"transport": 78, "safety": 80, "convenience": 80, "cost": 66, "education": 85, "green": 78, "development": 72, "stability": 80}, "avg_rent": 58, "avg_deposit": 1230, "avg_jeonse": 14800},
    "궁동": {"gu": "유성구", "lat": 36.3680, "lng": 127.3650, "scores": {"transport": 76, "safety": 78, "convenience": 78, "cost": 68, "education": 82, "green": 76, "development": 70, "stability": 79}, "avg_rent": 55, "avg_deposit": 1150, "avg_jeonse": 13800},
    "덕명동": {"gu": "유성구", "lat": 36.3780, "lng": 127.3380, "scores": {"transport": 72, "safety": 80, "convenience": 74, "cost": 70, "education": 82, "green": 80, "development": 72, "stability": 80}, "avg_rent": 54, "avg_deposit": 1100, "avg_jeonse": 13200},
    "원신흥동": {"gu": "유성구", "lat": 36.3840, "lng": 127.3290, "scores": {"transport": 68, "safety": 78, "convenience": 70, "cost": 73, "education": 78, "green": 82, "development": 68, "stability": 78}, "avg_rent": 50, "avg_deposit": 1000, "avg_jeonse": 12000},
    "장대동": {"gu": "유성구", "lat": 36.3710, "lng": 127.3550, "scores": {"transport": 79, "safety": 79, "convenience": 81, "cost": 67, "education": 81, "green": 77, "development": 71, "stability": 79}, "avg_rent": 57, "avg_deposit": 1200, "avg_jeonse": 14400},
    "화암동": {"gu": "유성구", "lat": 36.3610, "lng": 127.3240, "scores": {"transport": 60, "safety": 76, "convenience": 63, "cost": 78, "education": 73, "green": 85, "development": 63, "stability": 76}, "avg_rent": 46, "avg_deposit": 920, "avg_jeonse": 11000},

    # 대덕구
    "오정동": {"gu": "대덕구", "lat": 36.3640, "lng": 127.4150, "scores": {"transport": 72, "safety": 68, "convenience": 74, "cost": 78, "education": 65, "green": 60, "development": 58, "stability": 70}, "avg_rent": 47, "avg_deposit": 950, "avg_jeonse": 11500},
    "중리동": {"gu": "대덕구", "lat": 36.3710, "lng": 127.4220, "scores": {"transport": 70, "safety": 66, "convenience": 72, "cost": 80, "education": 62, "green": 58, "development": 55, "stability": 68}, "avg_rent": 44, "avg_deposit": 880, "avg_jeonse": 10800},
    "석봉동": {"gu": "대덕구", "lat": 36.3780, "lng": 127.4290, "scores": {"transport": 65, "safety": 65, "convenience": 68, "cost": 82, "education": 60, "green": 62, "development": 52, "stability": 66}, "avg_rent": 41, "avg_deposit": 820, "avg_jeonse": 9800},
    "법동": {"gu": "대덕구", "lat": 36.3850, "lng": 127.4360, "scores": {"transport": 62, "safety": 64, "convenience": 65, "cost": 84, "education": 58, "green": 65, "development": 50, "stability": 65}, "avg_rent": 39, "avg_deposit": 780, "avg_jeonse": 9300},
    "신탄진동": {"gu": "대덕구", "lat": 36.4380, "lng": 127.4020, "scores": {"transport": 68, "safety": 67, "convenience": 70, "cost": 82, "education": 62, "green": 70, "development": 62, "stability": 68}, "avg_rent": 43, "avg_deposit": 850, "avg_jeonse": 10200},
    "회덕동": {"gu": "대덕구", "lat": 36.4120, "lng": 127.4180, "scores": {"transport": 60, "safety": 65, "convenience": 63, "cost": 85, "education": 58, "green": 68, "development": 55, "stability": 66}, "avg_rent": 38, "avg_deposit": 750, "avg_jeonse": 9000},
    "읍내동": {"gu": "대덕구", "lat": 36.4060, "lng": 127.4250, "scores": {"transport": 58, "safety": 63, "convenience": 60, "cost": 87, "education": 55, "green": 70, "development": 52, "stability": 64}, "avg_rent": 36, "avg_deposit": 710, "avg_jeonse": 8500},
    "덕암동": {"gu": "대덕구", "lat": 36.3930, "lng": 127.4320, "scores": {"transport": 55, "safety": 62, "convenience": 58, "cost": 88, "education": 54, "green": 72, "development": 50, "stability": 63}, "avg_rent": 34, "avg_deposit": 680, "avg_jeonse": 8100},
    "비래동": {"gu": "대덕구", "lat": 36.3720, "lng": 127.4500, "scores": {"transport": 63, "safety": 66, "convenience": 65, "cost": 83, "education": 60, "green": 65, "development": 53, "stability": 66}, "avg_rent": 40, "avg_deposit": 800, "avg_jeonse": 9500},
    "목상동": {"gu": "대덕구", "lat": 36.3820, "lng": 127.4450, "scores": {"transport": 58, "safety": 64, "convenience": 60, "cost": 86, "education": 56, "green": 68, "development": 50, "stability": 64}, "avg_rent": 37, "avg_deposit": 730, "avg_jeonse": 8700},
}

# 행정동별 장점/주의점 텍스트 (더미 AI 생성 텍스트)
DISTRICT_DESCRIPTIONS = {
    "둔산2동": {
        "pros": ["대전 최대 상업·행정 중심지로 편의시설 최우수", "지하철 2호선(예정) 및 버스 네트워크 탁월", "대형마트·병원·문화시설 도보 접근 가능"],
        "cons": ["임대료가 대전 평균보다 30% 높음", "주말 유동인구 많아 소음 발생 가능"],
        "tags": ["편의성 최우수", "교통 편리", "고물가 주의"]
    },
    "도안동": {
        "pros": ["갑천 생태공원 인접 녹지 풍부", "대전에서 최신 신도시로 주거환경 쾌적", "어린이집·학교 등 교육시설 우수"],
        "cons": ["지하철 접근성 상대적으로 낮음", "아직 상업시설 성숙 중으로 생활편의 불완전"],
        "tags": ["녹지 풍부", "신도시", "교육 우수"]
    },
    "노은2동": {
        "pros": ["학원가·학교 밀집으로 교육환경 우수", "안전하고 조용한 주거 환경", "대형마트·편의시설 접근 양호"],
        "cons": ["원도심 대비 임대료 약간 높음", "지하철역까지 버스 환승 필요"],
        "tags": ["교육 최우수", "안전", "가족형 주거"]
    },
    "은행선화동": {
        "pros": ["대전역·정부청사 접근성 최우수", "대흥동 문화·예술지구와 인접", "공공기관·업무지구 도보 통근 가능"],
        "cons": ["원도심 특성상 건물 노후화", "유흥가 인접 구역 존재"],
        "tags": ["교통 편리", "직주근접", "원도심"]
    },
    "봉명동": {
        "pros": ["유성온천·유성구청 인접 생활편의 우수", "카이스트·충남대 접근성으로 교육 인프라 우수", "젊은 층 많아 활기찬 생활환경"],
        "cons": ["유성 온천지구 유흥가와 인접 가능", "주차 공간 부족 지역 존재"],
        "tags": ["대학가 인접", "활기찬 환경", "젊은층 선호"]
    },
}

# 기본 설명 (위 목록에 없는 동 사용)
DEFAULT_PROS = ["대중교통 접근성 양호", "생활편의시설 인접", "비교적 조용한 주거환경"]
DEFAULT_CONS = ["일부 노후 주거시설 존재", "심야 교통 다소 불편"]

# 직장/학교 위치 더미 데이터
WORKPLACES = {
    "정부청사역": {"lat": 36.3510, "lng": 127.3870},
    "대전역": {"lat": 36.3322, "lng": 127.4344},
    "유성구청": {"lat": 36.3625, "lng": 127.3563},
    "충남대학교": {"lat": 36.3688, "lng": 127.3430},
    "KAIST": {"lat": 36.3738, "lng": 127.3607},
    "대전시청": {"lat": 36.3511, "lng": 127.3849},
    "대전복합터미널": {"lat": 36.3203, "lng": 127.4320},
    "둔산동 업무지구": {"lat": 36.3560, "lng": 127.3920},
    "연구개발특구(대덕)": {"lat": 36.3810, "lng": 127.3640},
    "직접 입력": {"lat": None, "lng": None},
}

# 프리셋 설정
PRESETS = {
    "교통 우선형": {"transport": 5, "safety": 3, "convenience": 3, "cost": 2, "education": 2, "green": 1, "development": 2, "stability": 2},
    "가성비 우선형": {"transport": 2, "safety": 3, "convenience": 3, "cost": 5, "education": 2, "green": 2, "development": 3, "stability": 3},
    "안전 우선형": {"transport": 2, "safety": 5, "convenience": 3, "cost": 2, "education": 3, "green": 3, "development": 1, "stability": 4},
    "신혼부부형": {"transport": 2, "safety": 4, "convenience": 3, "cost": 2, "education": 5, "green": 3, "development": 3, "stability": 4},
    "대학원생형": {"transport": 4, "safety": 3, "convenience": 4, "cost": 5, "education": 3, "green": 2, "development": 1, "stability": 2},
    "자연 선호형": {"transport": 1, "safety": 3, "convenience": 2, "cost": 3, "education": 2, "green": 5, "development": 2, "stability": 3},
}

# 챗봇 응답 패턴
CHATBOT_RESPONSES = {
    "교통": {
        "keywords": ["교통", "지하철", "버스", "통근", "대중교통", "역"],
        "response": """대전의 대중교통은 **지하철 1호선**과 **버스 네트워크**로 구성됩니다.

🚇 **지하철 접근성 우수 지역**: 둔산동, 탄방동, 내동, 은행선화동
🚌 **버스 노선 풍부 지역**: 중구, 서구 주요 지역
🚇 **2호선 예정 구간**: 도안~반석~노은 라인 (개통 시 서·유성구 교통 대폭 개선 예정)

출근지를 입력하시면 통근 시간 기준으로 최적 지역을 추천해드릴게요!"""
    },
    "안전": {
        "keywords": ["안전", "치안", "범죄", "CCTV", "야간"],
        "response": """대전의 안전지수는 지역별로 차이가 있습니다.

🟢 **안전 상위 지역**: 도안동, 노은동, 유성구 신도시권
🟡 **보통 수준**: 둔산동, 갈마동, 월평동
🔴 **주의 권고 지역**: 일부 원도심 구역 (중구 일부)

**야간 편의점 접근성**이 중요하시다면 둔산·탄방 라인을 추천드려요. 
CCTV 설치 밀도는 서구>유성구>중구>동구>대덕구 순입니다."""
    },
    "월세": {
        "keywords": ["월세", "전세", "보증금", "임대", "가격", "비용", "예산"],
        "response": """대전 지역별 평균 월세 수준 (2025년 기준)입니다.

💰 **30~40만원대**: 동구, 대덕구 외곽
💰 **40~50만원대**: 중구, 동구 주요 지역
💰 **50~60만원대**: 서구, 유성구 일반 지역
💰 **60~75만원대**: 둔산동, 도안동, 봉명동 등 프리미엄 지역

예산을 조건 입력에 넣으시면 예산 내 최적 지역을 필터링해 드립니다."""
    },
    "학교": {
        "keywords": ["학교", "교육", "학원", "어린이집", "초등", "중학교", "대학교"],
        "response": """대전의 교육 인프라 우수 지역입니다.

🏫 **초·중·고 학군 우수**: 노은동, 도안동, 둔산동
👨‍🎓 **대학 인접 지역**: 어은동·궁동(충남대), 어은동(KAIST), 봉명동
🎓 **학원가 밀집**: 노은동, 둔산1·2동
👶 **어린이집 접근성**: 도안동, 노은동, 갈마동

신혼부부나 자녀가 있으시다면 노은2동, 도안동을 강력 추천드립니다!"""
    },
    "개발": {
        "keywords": ["개발", "재개발", "신도시", "호재", "투자", "미래"],
        "response": """대전 주요 개발/정비 현황입니다.

🏗️ **개발 진행 중**:
- 도안 신도시: 갑천지구 지속 개발
- 대전역세권: 역 복합개발 추진
- 원도심(은행선화·대흥동): 도시재생뉴딜 사업

📋 **예정/계획**:
- 지하철 2호선 트램 (월평~반석 구간)
- 관평동 산업단지 연계 주거개발
- 신탄진 역세권 개발

투자 관점이라면 도안동·대전역 인근 지역의 중장기 가치 상승 가능성이 높습니다."""
    },
    "추천": {
        "keywords": ["추천", "어디가", "어느 동네", "살기 좋은", "best", "좋은 곳"],
        "response": """조건에 따라 다르지만, 대전 인기 주거지 TOP 5를 소개합니다!

🥇 **둔산2동** - 편의시설·교통 최고, 임대료 높음
🥈 **도안동** - 신도시 쾌적함, 녹지 풍부, 미래가치 높음
🥉 **노은2동** - 교육환경 최우수, 안전하고 조용함
4️⃣ **봉명동** - 대학가 인접, 젊고 활기찬 분위기
5️⃣ **탄방동** - 교통 편리, 편의시설 양호, 합리적 임대료

왼쪽 패널에서 조건을 입력하시면 **맞춤형 추천**을 받으실 수 있어요!"""
    },
    "대전": {
        "keywords": ["대전", "특징", "소개", "어떤 도시"],
        "response": """대전은 **충청권 중심 광역시**로 주거 매력이 높은 도시입니다! 🏙️

📍 **5개 자치구**: 동구, 중구, 서구, 유성구, 대덕구
🚄 **교통**: KTX 대전역, 고속도로 요충지
🔬 **특성**: 대덕연구개발특구, 정부대전청사, KAIST·충남대
🏗️ **개발**: 도안 신도시, 대전역세권 개발

- 서울 대비 임대료 50~60% 수준
- 대중교통 1호선 + 버스 네트워크
- 2호선 트램 추진 중으로 미래 교통 기대

어떤 조건으로 주거지를 찾고 계신지 알려주세요!"""
    },
}

DEFAULT_CHATBOT_RESPONSE = """안녕하세요! 대전 맞춤형 주거 AI 상담사입니다. 🏠

다음과 같은 질문을 해보세요:
- "대전에서 교통 좋은 곳 어디야?"
- "월세 50만원 이하로 살기 좋은 동네?"
- "아이 키우기 좋은 지역 알려줘"
- "안전한 동네 추천해줘"
- "개발 호재 있는 곳은?"

**왼쪽 패널**에서 상세 조건을 입력하시면 AI가 맞춤 추천 지역 TOP 5를 제공해드립니다!"""
