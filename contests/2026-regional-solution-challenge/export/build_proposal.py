"""proposal_draft.html -> proposal_draft.pdf (Microsoft Edge headless). 개인정보는 HTML의 [입력] 칸에 넣지 말고 로컬 사본에서만 채운다."""
import pathlib, subprocess, time

d = pathlib.Path(__file__).parent.resolve()
html, pdf = d / "proposal_draft.html", d / "proposal_draft.pdf"
edge = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"
pdf.unlink(missing_ok=True)
for _ in range(4):
    subprocess.run([edge, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pdf}", html.as_uri()], timeout=80)
    for _ in range(20):
        if pdf.exists() and pdf.stat().st_size > 1000:
            break
        time.sleep(0.5)
    if pdf.exists():
        break
print(pdf)
