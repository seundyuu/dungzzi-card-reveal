# 월간리포트 — 이번달 나의 덩찌 프로토타입

**바로 보기**

| 페이지 | 링크 | 내용 |
|---|---|---|
| 전체 흐름 | https://seundyuu.github.io/dungzzi-card-reveal/ | 표지 → 주요 공부 시간 → 셔플 → 결과 공개 |
| 표지 | https://seundyuu.github.io/dungzzi-card-reveal/cover.html | 표지만 (「펼쳐보기」는 전체 흐름으로 이동) |
| 주요 공부 시간 | https://seundyuu.github.io/dungzzi-card-reveal/time.html | 아침 (기본). `?time=afternoon`, `?time=night`로 오후·밤 버전 |
| 결과 | https://seundyuu.github.io/dungzzi-card-reveal/result.html | 셔플 없이 덩찌 결과 공개만 |

표지 → 주요 공부 시간 → 카드 셔플 → 스켈레톤 → 덩찌 결과 공개까지 이어지는 인터랙션 프로토타입입니다. 「다시 재생」을 누르면 표지부터 다시 시작합니다.

- 디자인 원본: Figma 「월간리포트」 (표지 `142:453`, 주요 공부 시간 `234:1515`, 스켈레톤 `101:559`, 결과 `1:3726`)
- 수치·색·모션 타임라인·데이터 구조: [`design.md`](design.md)
- 구현 레퍼런스: [`index.html`](index.html) (HTML/CSS/JS 한 파일, 375 × 812 기준)
- `cover.html`, `time.html`, `result.html`은 `index.html`에서 만든다. `index.html`을 고친 뒤 `python3 scripts/make-pages.py` 실행
- 에셋: [`assets/`](assets) · 폰트: [`fonts/Pretendard/`](fonts/Pretendard) (SIL OFL)

값이 서로 다르면 **Figma가 우선**입니다.
