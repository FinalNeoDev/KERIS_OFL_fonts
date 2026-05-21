import os
from pathlib import Path

# 설정
FONT_DIR = 'web_fonts'
OUTPUT_FILE = 'index.html'
SUPPORTED_EXTENSIONS = {'.ttf', '.otf', '.woff', '.woff2'}

def generate_html():
    font_dir_path = Path(FONT_DIR)
    
    if not font_dir_path.exists() or not font_dir_path.is_dir():
        print(f"오류: '{FONT_DIR}' 폴더를 찾을 수 없습니다. 스크립트가 실행되는 위치를 확인해주세요.")
        return

    font_files = [f for f in font_dir_path.iterdir() if f.suffix.lower() in SUPPORTED_EXTENSIONS]
    font_files.sort(key=lambda x: x.name)

    if not font_files:
        print(f"경고: '{FONT_DIR}' 폴더에 폰트 파일이 없습니다.")
        return

    html_font_cards = []

    for i, font_path in enumerate(font_files):
        font_filename = font_path.name
        font_name = font_path.stem  
        font_family = f"Font_{i}"   
        
        # GitHub Repo 기반 jsDelivr CDN 주소 (다운로드 속도 최적화)
        cdn_download_url = f"https://cdn.jsdelivr.net/gh/FinalNeoDev/KERIS_OFL_fonts@main/{FONT_DIR}/{font_filename}"

        html_font_cards.append(f"""
        <div class="font-card">
            <div class="font-info">
                <div class="font-name">{font_name}</div>
                <div class="font-preview" data-font-family="{font_family}" data-font-url="./{FONT_DIR}/{font_filename}" data-preview>가나다라마바사아자차카타파하01234567890</div>
            </div>
            <a href="{cdn_download_url}" class="download-btn">빠른 다운로드</a>
        </div>
        """)

    # 전체 HTML 템플릿 조립
    html_content = f"""<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>KERIS의 OFL 폰트모음(KERIS_OFL_fonts)</title>
    <style>
        body {{ font-family: sans-serif; padding: 20px; background-color: #f6f8fa; color: #24292f; margin: 0; }}
        .container {{ max-width: 1000px; margin: 0 auto; }}
        
        .header {{ text-align: center; margin-bottom: 20px; }}
        .header h1 {{ margin-bottom: 5px; }}
        .header h2 {{ font-size: 20px; color: #57606a; margin-top: 0; margin-bottom: 20px; font-weight: normal; }}
        
        .notice-box {{ background: #eaf5ff; padding: 15px 20px; border-radius: 8px; font-size: 14px; text-align: left; margin-bottom: 20px; border: 1px solid #b6e3ff; color: #0969da; line-height: 1.6; }}
        .notice-box p {{ margin: 0 0 5px 0; }}
        .notice-box p:last-child {{ margin-bottom: 0; }}
        .notice-box a {{ color: #0969da; text-decoration: underline; }}
        
        .project-links {{ background: #ffffff; padding: 15px 20px; border-radius: 8px; border: 1px solid #d0d7de; margin-bottom: 30px; text-align: left; }}
        .project-links h3 {{ margin-top: 0; font-size: 16px; color: #24292f; margin-bottom: 10px; }}
        .project-links ul {{ margin: 0; padding-left: 20px; font-size: 14px; line-height: 1.6; }}
        .project-links a {{ color: #0969da; text-decoration: none; }}
        .project-links a:hover {{ text-decoration: underline; }}
        
        .more-link {{ display: inline-block; margin-bottom: 15px; font-weight: 600; color: #2da44e; text-decoration: none; font-size: 15px; }}
        .more-link:hover {{ text-decoration: underline; color: #2c974b; }}

        .controls {{ display: flex; gap: 15px; margin-bottom: 30px; flex-wrap: wrap; }}
        .controls input {{ padding: 15px; font-size: 16px; border: 1px solid #d0d7de; border-radius: 6px; box-shadow: inset 0 1px 2px rgba(0,0,0,0.075); }}
        #previewInput {{ flex: 2; min-width: 300px; }}
        #searchInput {{ flex: 1; min-width: 200px; }}
        
        /* 로딩 중일 때 부드러운 전환 효과 */
        .font-preview {{ font-size: 36px; word-break: break-all; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; line-height: 1.2; transition: opacity 0.3s ease; }}
        .font-preview.loading {{ opacity: 0.3; }}

        .font-card {{ background: #ffffff; padding: 25px; margin-bottom: 20px; border-radius: 8px; border: 1px solid #d0d7de; display: flex; justify-content: space-between; align-items: center; }}
        .font-info {{ flex: 1; overflow: hidden; }}
        .font-name {{ font-size: 14px; color: #57606a; margin-bottom: 15px; font-weight: 600; }}
        
        .download-btn {{ background-color: #2da44e; color: #ffffff; text-decoration: none; padding: 10px 20px; border-radius: 6px; font-weight: 600; font-size: 14px; margin-left: 20px; white-space: nowrap; transition: background-color 0.2s; }}
        .download-btn:hover {{ background-color: #2c974b; }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>KERIS의 OFL 폰트모음(KERIS_OFL_fonts)</h1>
            <h2>웹폰트로 불러와 사용하기</h2>
        </div>

        <div class="notice-box">
            <p><strong>주의:</strong> KERIS 공모폰트를 제외한 폰트의 정확한 사용범위는 폰트 제작사의 규정에 따라 다를 수 있으므로 사용 전 확인바랍니다.</p>
            <p>- OFL라이선스 폰트를 편하게 사용 목적</p>
            <p>- 자료출처: <a href="https://copyright.keris.or.kr/wft/fntDwnld" target="_blank">https://copyright.keris.or.kr/wft/fntDwnld</a></p>
            <p>- 공공 목적의 무료 폰트로 제공되며, 사용 결과에 대한 책임은 지지 않습니다.</p>
            <p>- 문의: <a href="mailto:finalneodev@gmail.com">finalneodev@gmail.com</a></p>
        </div>

        <div class="project-links">
            <h3>📌 FinalNeoDev 소개</h3>
            <a href="https://finalneodev.github.io" target="_blank" class="more-link">🚀 FinalNeoDev 더 알아보기</a>
            <ul>
                <li><a href="https://finalneodev.github.io/Korea_Holidays/" target="_blank">공휴일 & 영업일 계산기 (Web UI)</a></li>
                <li><a href="https://finalneodev.github.io/Korea_Holidays/overtime.html" target="_blank">야근 및 휴일 가산수당 계산기 (Web UI)</a></li>
            </ul>
        </div>

        <div class="controls">
            <input type="text" id="previewInput" value="가나다라마바사아자차카타파하01234567890" placeholder="미리보기 텍스트를 입력하세요">
            <input type="text" id="searchInput" placeholder="폰트 이름 검색">
        </div>

        <div id="fontList">
            {''.join(html_font_cards)}
        </div>
    </div>

    <script>
        // 1. 텍스트 실시간 변경 기능
        const previewInput = document.getElementById('previewInput');
        const previewElements = document.querySelectorAll('[data-preview]');

        previewInput.addEventListener('input', function() {{
            const text = this.value || '미리보기를 위한 텍스트입니다.';
            previewElements.forEach(el => {{ el.textContent = text; }});
        }});

        // 2. 검색 기능
        const searchInput = document.getElementById('searchInput');
        const fontCards = document.querySelectorAll('.font-card');

        searchInput.addEventListener('input', function() {{
            const keyword = this.value.toLowerCase();
            fontCards.forEach(card => {{
                const fontName = card.querySelector('.font-name').textContent.toLowerCase();
                card.style.display = fontName.includes(keyword) ? 'flex' : 'none';
            }});
        }});

        // 3. 지연 로딩 (Intersection Observer) 기능
        const observerOptions = {{
            root: null,
            rootMargin: '200px', // 화면에 나타나기 200px 전부터 미리 로딩 시작
            threshold: 0
        }};

        const fontObserver = new IntersectionObserver((entries, observer) => {{
            entries.forEach(entry => {{
                if (entry.isIntersecting) {{
                    const previewEl = entry.target.querySelector('.font-preview');
                    const fontFamily = previewEl.getAttribute('data-font-family');
                    const fontUrl = previewEl.getAttribute('data-font-url');

                    // 이미 로딩된 폰트인지 확인
                    if (!document.getElementById('style-' + fontFamily)) {{
                        const style = document.createElement('style');
                        style.id = 'style-' + fontFamily;
                        style.innerHTML = `
                            @font-face {{
                                font-family: '${{fontFamily}}';
                                src: url('${{fontUrl}}');
                                font-display: swap; 
                            }}
                            .applied-${{fontFamily}} {{ font-family: '${{fontFamily}}', sans-serif; }}
                        `;
                        document.head.appendChild(style);
                        
                        previewEl.classList.add('applied-' + fontFamily);
                    }}
                    
                    observer.unobserve(entry.target);
                }}
            }});
        }}, observerOptions);

        fontCards.forEach(card => fontObserver.observe(card));
    </script>
</body>
</html>"""

    with open(OUTPUT_FILE, 'w', encoding='utf-8') as f:
        f.write(html_content)
    
    print(f"✅ 성공: {len(font_files)}개의 폰트가 적용된 (CDN 고속 다운로드 적용) '{OUTPUT_FILE}' 파일이 업데이트되었습니다.")

if __name__ == '__main__':
    generate_html()
