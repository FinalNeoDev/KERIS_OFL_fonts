import os
from pathlib import Path

# 설정 (현재 디렉토리 구조에 맞게 변경)
FONT_DIR = 'web_fonts'
OUTPUT_FILE = 'index.html'
# 웹 폰트 형식인 woff, woff2도 기본 지원하도록 설정되어 있습니다.
SUPPORTED_EXTENSIONS = {'.ttf', '.otf', '.woff', '.woff2'}

def generate_html():
    font_dir_path = Path(FONT_DIR)
    
    # 1. 폰트 폴더 존재 여부 확인
    if not font_dir_path.exists() or not font_dir_path.is_dir():
        print(f"오류: '{FONT_DIR}' 폴더를 찾을 수 없습니다. 스크립트가 실행되는 위치를 확인해주세요.")
        return

    # 2. 지원되는 확장자를 가진 폰트 파일 목록 가져오기 및 정렬
    font_files = [f for f in font_dir_path.iterdir() if f.suffix.lower() in SUPPORTED_EXTENSIONS]
    font_files.sort(key=lambda x: x.name)

    if not font_files:
        print(f"경고: '{FONT_DIR}' 폴더에 폰트 파일이 없습니다.")
        return

    css_font_faces = []
    html_font_cards = []

    # 3. 각 폰트별로 CSS와 HTML 태그 생성
    for i, font_path in enumerate(font_files):
        font_filename = font_path.name
        font_name = font_path.stem  # 확장자를 제외한 파일명
        font_family = f"Font_{i}"   # CSS 에러 방지를 위한 안전한 클래스명
        
        # CSS 규칙 추가 (@font-face)
        css_font_faces.append(f"""
        @font-face {{
            font-family: '{font_family}';
            src: url('./{FONT_DIR}/{font_filename}');
        }}
        .preview-{font_family} {{ font-family: '{font_family}', sans-serif; }}
        """)

        # HTML 폰트 카드 추가
        html_font_cards.append(f"""
        <div class="font-card">
            <div class="font-info">
                <div class="font-name">{font_name}</div>
                <div class="font-preview preview-{font_family}" data-preview>다람쥐 헌 쳇바퀴에 타고파. The quick brown fox.</div>
            </div>
            <a href="./{FONT_DIR}/{font_filename}" download class="download-btn">다운로드</a>
        </div>
        """)

    # 4. 전체 HTML 템플릿 조립 (파이썬 f-string 이스케이프 처리 완료)
    html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KERIS OFL 폰트 미리보기 및 다운로드</title>
    <!-- css 디렉토리를 활용하시려면 아래 주석을 풀고 CSS 파일을 연결하세요 -->
    <!-- <link rel="stylesheet" href="./css/style.css"> -->
    <style>
        body {{ font-family: sans-serif; padding: 20px; background-color: #f6f8fa; color: #24292f; margin: 0; }}
        .container {{ max-width: 1000px; margin: 0 auto; }}
        .header {{ text-align: center; margin-bottom: 40px; }}
        .controls {{ display: flex; gap: 15px; margin-bottom: 30px; flex-wrap: wrap; }}
        .controls input {{ padding: 15px; font-size: 16px; border: 1px solid #d0d7de; border-radius: 6px; box-shadow: inset 0 1px 2px rgba(0,0,0,0.075); }}
        #previewInput {{ flex: 2; min-width: 300px; }}
        #searchInput {{ flex: 1; min-width: 200px; }}
        
        /* 자동 생성된 폰트 CSS */
        {''.join(css_font_faces)}

        .font-card {{ background: #ffffff; padding: 25px; margin-bottom: 20px; border-radius: 8px; border: 1px solid #d0d7de; display: flex; justify-content: space-between; align-items: center; }}
        .font-info {{ flex: 1; overflow: hidden; }}
        .font-name {{ font-size: 14px; color: #57606a; margin-bottom: 15px; font-weight: 600; }}
        .font-preview {{ font-size: 36px; word-break: break-all; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; line-height: 1.2; }}
        .download-btn {{ background-color: #2da44e; color: #ffffff; text-decoration: none; padding: 10px 20px; border-radius: 6px; font-weight: 600; font-size: 14px; margin-left: 20px; white-space: nowrap; }}
        .download-btn:hover {{ background-color: #2c974b; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>KERIS OFL Fonts 미리보기</h1>
            <p>원하는 문구를 입력하여 폰트를 확인하고, 필요한 폰트를 다운로드하세요.</p>
        </div>

        <div class="controls">
            <input type="text" id="previewInput" value="다람쥐 헌 쳇바퀴에 타고파. The quick brown fox." placeholder="미리보기 텍스트를 입력하세요">
            <input type="text" id="searchInput" placeholder="폰트 이름 검색">
        </div>

        <div id="fontList">
            {''.join(html_font_cards)}
        </div>
    </div>

    <script>
        // 텍스트 실시간 적용
        const previewInput = document.getElementById('previewInput');
        const previewElements = document.querySelectorAll('[data-preview]');

        previewInput.addEventListener('input', function() {{
            const text = this.value || '미리보기를 위한 텍스트입니다.';
            previewElements.forEach(el => {{ el.textContent = text; }});
        }});

        // 폰트 검색 기능
        const searchInput = document.getElementById('searchInput');
        const fontCards = document.querySelectorAll('.font-card');

        searchInput.addEventListener('input', function() {{
            const keyword = this.value.toLowerCase();
            fontCards.forEach(card => {{
                const fontName = card.querySelector('.font-name').textContent.toLowerCase();
                card.style.display = fontName.includes(keyword) ? 'flex' : 'none';
            }});
        }});
    </script>
</body>
</html>"""

    # 5. HTML 파일 쓰기 (기존 index.html 덮어쓰기)
    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ 성공: {len(font_files)}개의 폰트가 적용된 '{OUTPUT_FILE}' 파일이 생성되었습니다.")

if __name__ == '__main__':
    generate_html()
