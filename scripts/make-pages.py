"""index.html에서 화면별 페이지를 만든다. index.html을 고친 뒤 다시 실행: python3 scripts/make-pages.py"""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
src = (root / 'index.html').read_text()
pages = {
    'popup.html':  ('popup',  '월간리포트 — 첫 진입 팝업'),
    'cover.html':  ('cover',  '월간리포트 — 표지'),
    'time.html':   ('time',   '월간리포트 — 주요 공부 시간'),
    'result.html': ('result', '월간리포트 — 덩찌 결과'),
    'time-morning.html':   ('time', '월간리포트 — 주요 공부 시간 (아침)', 'morning'),
    'time-afternoon.html': ('time', '월간리포트 — 주요 공부 시간 (오후)', 'afternoon'),
    'time-night.html':     ('time', '월간리포트 — 주요 공부 시간 (밤)', 'night'),
}
for name, (page, title, *rest) in pages.items():
    attrs = f'data-page="{page}"' + (f' data-time="{rest[0]}"' if rest else '')
    s = src.replace('<html lang="ko">', f'<html lang="ko" {attrs}>', 1)
    s = s.replace('<title>덩찌 카드 셔플</title>', f'<title>{title}</title>', 1)
    assert f'data-page="{page}"' in s and title in s
    (root / name).write_text(s)
    print('wrote', name)
