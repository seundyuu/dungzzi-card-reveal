# 월간리포트 — 이번달 나의 덩찌 프로토타입 (v2)

> **v2 브랜치**: 개발·정책 이슈로 07 스켈레톤 · 08 결과 화면을 바꾼 버전 (Figma `282:5795`, `248:3194`).
> 결과 카드에서 활동 타일 4개와 「전체 유저 중 8%」 문구를 빼고, 한 줄 소개를 카드 아래 타일로 옮김. 「종료하기」 추가.
> 바로 보기: https://seundyuu.github.io/dungzzi-card-reveal/v2/ · 이전 버전(main): https://seundyuu.github.io/dungzzi-card-reveal/

**바로 보기**

| 페이지 | 링크 | 내용 |
|---|---|---|
| 전체 흐름 | https://seundyuu.github.io/dungzzi-card-reveal/v2/ | 첫 진입 팝업 → 표지 → 주요 공부 시간 → 퀴즈 → 밥그릇 → 순위 → 셔플 → 결과 → 공유 → 마이페이지 |
| 첫 진입 팝업 | https://seundyuu.github.io/dungzzi-card-reveal/v2/popup.html | 홈 위 바텀시트만 (「실록 보러가기」는 표지로 이동) |
| 표지 | https://seundyuu.github.io/dungzzi-card-reveal/v2/cover.html | 표지부터 (「펼쳐보기」는 주요 공부 시간으로 이동) |
| 주요 공부 시간 — 아침 | https://seundyuu.github.io/dungzzi-card-reveal/v2/time-morning.html | 아침 버전 |
| 주요 공부 시간 — 점심 | https://seundyuu.github.io/dungzzi-card-reveal/v2/time-afternoon.html | 점심 버전 |
| 주요 공부 시간 — 저녁 | https://seundyuu.github.io/dungzzi-card-reveal/v2/time-night.html | 저녁 버전 |
| 결과 | https://seundyuu.github.io/dungzzi-card-reveal/v2/result.html | 셔플 없이 덩찌 결과 공개만 (「친구에게 공유하기」 → 아이폰에서는 기본 공유하기, PC에서는 iOS 공유 시트 예시) |
| 결과 — 한 줄 소개 2줄 | https://seundyuu.github.io/dungzzi-card-reveal/v2/result.html?line=2 | 소개 타일이 2줄일 때 (카드 380) |
| 마이페이지 | https://seundyuu.github.io/dungzzi-card-reveal/v2/mypage.html | 「우쑤한국사 12월 실록 보기」로 실록 다시 열기 |

첫 진입 팝업 → 표지 → 주요 공부 시간 → 카드 셔플 → 스켈레톤 → 덩찌 결과 공개까지 이어지는 인터랙션 프로토타입입니다. 「다시 재생」을 누르면 첫 진입 팝업부터 다시 시작합니다.

- 디자인 원본: Figma 「월간리포트」 (작업 공간 `160:1415`, 전체 흐름 섹션 `239:2215`, 탭 영역 `239:1607`, 첫 진입 팝업 `160:773`, 표지 `142:453`, 주요 공부 시간 `234:1515`, 스켈레톤 `101:559`, 결과 `1:3726`)
- 수치·색·모션 타임라인·데이터 구조: [`design.md`](design.md)
- 구현 레퍼런스: [`index.html`](index.html) (HTML/CSS/JS 한 파일, 375 × 812 기준)
- `popup.html`, `cover.html`, `time*.html`, `result.html`, `mypage.html`은 `index.html`에서 만든다. `index.html`을 고친 뒤 `python3 scripts/make-pages.py` 실행
- 에셋: [`assets/`](assets) · 폰트: [`fonts/Pretendard/`](fonts/Pretendard) (SIL OFL)

값이 서로 다르면 **Figma가 우선**입니다.
