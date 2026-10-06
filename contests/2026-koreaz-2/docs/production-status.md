# 제작 현황과 누락 산출물 점검

2026-10-06 / v1.0. 작업 시작 시 main은 origin/main과 동일한 9b29f5a, 변경사항 없음. 기존 28개 파일의 기본 문서·100초 대본·자막·9장면 초안을 읽은 뒤 이어서 개편했다. 삭제·Git 초기화 없음.

## 요청 산출물 대응

| 요청 | 실제 경로 | 이번 작업 |
| --- | --- | --- |
| rules.md | docs/submission-rules.md, docs/rules.md 안내 | 기존 규정 보강 |
| concept.md | docs/concept.md | 5막·선택권·행동·제외 아이디어 반영 |
| research.md | docs/research.md | 조사 10항목·출처·영상 반영 여부 |
| characters.md | docs/characters.md | 신규 |
| visual-language.md | docs/visual-language.md | 신규 |
| storyboard.md | docs/storyboard.md | 18샷·요청 필드 전부 |
| narration_ko.md | script/narration_ko.md | 90초 제작 전체본 |
| subtitles_en.srt | subtitles/subtitles_en.srt | 자연스러운 번역·초안 타이밍 |
| shotlist.md | script/shotlist.md | 18샷 작업 표 |
| image-prompts.md | prompts/image_prompts.md | 기존 파일명 유지·18샷 |
| video-prompts.md | prompts/video_prompts.md | 기존 파일명 유지·5초 이하 |
| editing-plan.md | docs/editing-plan.md | 신규 |
| audio-plan.md | docs/audio-plan.md | 신규 |
| ai-usage.md | assets/ai-usage.md | 실제 사용·미사용 구분 |
| submission-checklist.md | docs/submission-checklist.md | 신규 |
| asset-manifest.md | assets/asset-manifest.md | 신규·실제 테스트 결과 |

## 제작 순서

1. 캐릭터·T01/T02/T03·타이틀 테스트를 검수하고 취약한 구도를 기록한다.
2. 2026 얼굴 파생과 필요한 키프레임을 만든다. 처음부터 전체 18샷을 생성하지 않는다.
3. 영상 생성 도구가 연결되면 최대 5초씩 생성한다. 현재 호출 가능한 영상 생성 도구는 확인되지 않았다.
4. 한국어 녹음, 음악·효과음을 제작하고 가편집한다.
5. UI·영어 자막을 합성하고 실재 음성에 맞춰 싱크를 조정한다.
6. 완성 MP4 출력·권리·규정 검수 후 SNS/구글폼 제출한다.

현재 산출물은 제작 설계와 초기 비주얼 검증 패키지다. 완성 제출 영상·녹음·음악·접수 증빙이 있다는 뜻은 아니다.

## 실제 완료 상태

캐릭터 시트·3종 핵심 비주얼·병원 단서 보정·타이틀·5초 UI 모션 뷰어를 실제 파일로 저장하고 제작자 검수를 기록했다. 전체 영상 생성은 시작하지 않았다. S01–S18을 완료했다고 표시하지 않았다.
