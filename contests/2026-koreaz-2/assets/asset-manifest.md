# 에셋 명세·비주얼 검수

2026-10-06. **실제 생성·저장한 파일만** 아래에 기록한다. 이미지 생성: built-in ImageGen, 모델 버전/시드 도구 응답 미노출. 외부 이미지·음원·폰트 파일 미사용. 원본 캐릭터·T01/T02/T03 및 T03 보정 총 5회 이미지 호출. UI·타이포·HTML은 사용자 후편집 지침에 따라 직접 제작.

## 실제 파일

| ID | 샷 | 파일 | 종류 | 크기 | SHA-256 | 상태 |
| --- | --- | --- | --- | --- | --- | --- |
| CHAR-01 | S01–S18 | [AB_reference_2036_v001.png](../assets/characters/AB_reference_2036_v001.png) | AI image | 1672×941, 1.88MiB | `136961b8bbb7` | 검증용 |
| T01 | S01/S16 | [T01_same_morning_v001.png](../assets/storyboard/T01_same_morning_v001.png) | AI image | 1672×941, 1.76MiB | `e0a3876fb137` | 검증용 |
| T02-PLATE | S04–S06 | [T02_plate_v001.png](../assets/storyboard/T02_plate_v001.png) | AI image | 1672×941, 1.49MiB | `7bd5fbe8c3d5` | 검증용 |
| T02-START | S04 | [T02_start_v001.png](../assets/storyboard/T02_start_v001.png) | post-production composite | 1672×941, 1.47MiB | `9dd247b81650` | 검증용 |
| T02-END | S05/S06 | [T02_composite_v001.png](../assets/storyboard/T02_composite_v001.png) | post-production composite | 1672×941, 1.47MiB | `94a08f1be979` | 검증용 |
| T03-V1 | S07/S08/S10 | [T03_public_montage_v001.png](../assets/storyboard/T03_public_montage_v001.png) | AI image | 1672×941, 1.74MiB | `ef12a586543a` | 검증용 |
| T03-V2 | S07/S08/S10 | [T03_public_montage_v002.png](../assets/storyboard/T03_public_montage_v002.png) | AI image edit | 1672×941, 1.70MiB | `76818f43b3fb` | 검증용 |
| TITLE-01 | S17 | [TITLE_statement_v001.png](../assets/storyboard/TITLE_statement_v001.png) | original typography | 1920×1080, 0.03MiB | `f35e1950ddc9` | 검증용 |
| TITLE-02 | S18 | [TITLE_question_v001.png](../assets/storyboard/TITLE_question_v001.png) | original typography | 1920×1080, 0.02MiB | `712b69739681` | 검증용 |
| TITLE-03 | S18 | [TITLE_end_v001.png](../assets/storyboard/TITLE_end_v001.png) | original typography | 1920×1080, 0.03MiB | `26cb78c6fa1d` | 검증용 |
| UI-01 | S03–S16 | [ui-components.svg](../assets/storyboard/ui-components.svg) | original vector | 1.6KiB | `c0575ab1548e` | 검증용 |
| PREVIEW-01 | tests | [visual-tests.html](../assets/storyboard/visual-tests.html) | original HTML | 5.4KiB | `3221b52265e5` | 검증용 |

## 제작자 검수 결과

| 테스트 | 확인 | 한계·보완 |
| --- | --- | --- |
| 캐릭터 | 얼굴·헤어·차콜/올리브 의상·기기가 기준 시트에 고정됨 | 실제 5초 영상에서의 얼굴 안정성은 미검증. 2026 얼굴 별도 파생 필요 |
| T01 같은 아침 | 두 인물·같은 책상 수준·같은 노출이 처음부터 읽힘 | 모니터 뒷면이므로 동의·AI 결과는 화면 인서트로 연결. 최종 UI 장면 플레이트로는 사용하지 않음 |
| T02 이동 | 정면 화면 확보. 같은 카드·열린/닫힌 문·목적 노드로 통과/정지 표시. HTML에 5초 동작 포함 | UI는 실제 서비스가 아닌 창작. 관객 무음 이해 검수는 아직 하지 않음 |
| T03 확장 | 학교/접수/공공 창구의 인물·공간 검증. v1 병원 식별 약점을 찾아 v2 보강 | 최종 몽타주는 3분할 대신 공간별 5초 클립. 공공 모니터가 뒷면이라 역방향 인서트 필요. 기업은 후속 샷 |
| 타이틀 | 정확한 문구·FHD·여백·5초씩 읽히는 순서를 직접 렌더 | 실제 영상 배경 위 가독성과 최종 폰트 이용 조건 추가 확인 |

‘성공’은 여기서 제작 가능한 구도와 장치의 확인을 뜻한다. 일반 관객 이해·감정·기억 검수나 완성 클립 검수를 완료했다는 뜻은 아니다. 세 테스트만으로 작품이 제출 가능하다고 판정하지 않는다.

## 후속 에셋 요청서

| 대상 | 필요 입력 | 납품/검수 기준 | 상태 |
| --- | --- | --- | --- |
| 2026 A/B 파생 | CHAR-01 | 동일인 22세·대표 의상 유지 | 미생성 |
| S01–S16 플레이트 | 캐릭터·샷별 프롬프트 | 얼굴·손·화면·16:9·구도 | 미완료 |
| S01–S16 클립 | 승인 플레이트 | 각 5초, FHD/30fps 편집 적합, 얼굴/기기 안정 | 영상 도구 연결 필요 |
| 음성 | 한국어 전체본 | 샷별 발화·최종 싱크 | 미녹음 |
| 음악·효과음 | 오디오 계획 | 권리 확인·대사 비가림 | 미제작 |
| 최종본 | 승인 클립/음성/UI | 90초 MP4·영어 번인·권리 검수 | 미출력 |

해시 전체값은 최종 제출본에서 별도 기록한다. 폰트 바이너리는 저장소에 없다. 생성 이미지는 참고 시트/테스트로만 채택한 상태이며 최종 영상에 반영한 부분은 AI 기록에서 갱신한다.
