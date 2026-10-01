# -*- coding: utf-8 -*-
# 修正宣传页下载按钮 href → v1.0.0 正式安装包
p = 'index.html'
s = open(p, encoding='utf-8').read()
old = '<a class="btn primary" href="#">\u2b07 \u4e0b\u8f7d LabCode</a>'
new = '<a class="btn primary" href="https://github.com/hulufeng/LabCode/releases/download/v1.0.0/LabCode-Setup-1.0.0.exe">\u2b07 \u4e0b\u8f7d LabCode</a>'
if old not in s:
    # 兜底：按 href="#" 定位
    import re
    m = re.search(r'<a class="btn primary" href="#"[^>]*>\s*[^\s]+\s*[\u4e00-\u9fff]+\s*LabCode</a>', s)
    assert m, 'anchor not found: ' + old[:40]
    s = s.replace(m.group(0), new)
else:
    s = s.replace(old, new)
open(p, 'w', encoding='utf-8').write(s)
print('href updated OK')
