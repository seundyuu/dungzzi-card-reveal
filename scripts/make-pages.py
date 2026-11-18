"""index.html에서 화면별 페이지를 만든다. index.html을 고친 뒤 다시 실행: python3 scripts/make-pages.py"""
from pathlib import Path
root = Path(__file__).resolve().parent.parent
src = (root / 'index.html').read_text()
pages = {
    'cover.html':  ('cover',  '월간리포트 — 표지'),
    'result.html': ('result', '월간리포트 — 덩찌 결과'),
}
for name, (page, title) in pages.items():
    s = src.replace('<html lang="ko">', f'<html lang="ko" data-page="{page}">', 1)
    s = s.replace('<title>덩찌 카드 셔플</title>', f'<title>{title}</title>', 1)
    assert f'data-page="{page}"' in s and title in s
    (root / name).write_text(s)
    print('wrote', name)
