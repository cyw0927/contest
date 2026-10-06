# 캐릭터 바이블 v1.0

두 인물은 가상의 청년이며 외형을 국적·정치적 우열과 연결하지 않는다. 2026년 22세, 2036년 32세. 2036년 기준 시트로 먼저 고정하고 2026년 얼굴은 동일인의 더 어린 버전으로 별도 파생해야 한다. 시트의 실제 얼굴을 문장보다 우선한다.

| 항목 | A | B |
| --- | --- | --- |
| 헤어 | 짙은 갈색 턱선 단발, 한쪽 귀 뒤로 넘김 | 짧은 짙은 곱슬머리 |
| 얼굴 | 타원형, 자연스러운 작은 주근깨, 어두운 갈색 눈 | 좁은 타원형, 갈색 눈, 옅은 수염 그림자 |
| 피부 | 따뜻한 베이지, 과도한 보정 없음 | 중간 올리브, 과도한 보정 없음 |
| 의상 | 차콜 면 오버셔츠·오프화이트 라운드 티·어두운 바지 | 탁한 올리브 면 오버셔츠·스톤그레이 티·어두운 바지 |
| 색 | 차콜/오프화이트 | 올리브/그레이 |
| 공간 | 합판 책상, 회색 벽, 단순 선반, 창문 측광 | 동일 수준의 합판 책상·회색 벽·단순 선반 |
| 기기 | 그래파이트 노트북, 검정 스마트폰, 회색 머그 | 같은 수준 기기와 머그 |
| 표정 | 집중·멈춤·작은 결심, 환호 없음 | 집중·멈춤·작은 수긍, 분노 과장 없음 |
| 카메라 | 눈높이, 35/50mm 느낌, 과한 뷰티 조명 없음 | 같은 거리·노출·렌즈 |

두 사람 모두 장신구·로고·유니폼·국기 소품 없음. 2026/2036 모두 대표 의상과 기기를 연속성 앵커로 유지한다. 나이 변화는 얼굴의 아주 작은 차이로 처리하고 시대 구분은 연도 카드·소리·편집에 맡긴다.

## 고정 프롬프트

### A

> Character A, the same fictional woman as the approved reference sheet, chin-length dark straight bob tucked behind one ear, oval face with subtle freckles, warm beige skin, dark brown eyes, charcoal cotton overshirt over off-white crewneck, dark trousers, no jewellery.

### B

> Character B, the same fictional man as the approved reference sheet, short dark curly hair, narrow oval face, olive skin, brown eyes, minimal beard shadow, muted olive cotton overshirt over stone-gray crewneck, dark trousers, no jewellery.

### 공통

> Use the approved reference image for identity. Preserve exact face, hairstyle, wardrobe, skin tone, room scale, laptop and smartphone. Equal living standards. No nationality signifiers. Natural restrained expression. No readable text or logos.

## 생성·검수 절차

1. 기준 시트에서 각 얼굴·의상·헤어를 확인한다.
2. 각 샷 생성에 시트를 입력 이미지로 전달한다. 텍스트 프롬프트만으로 동일 얼굴을 보장하지 않는다.
3. split screen은 좌우를 별도 생성하면 안정적이다. 합쳐진 테스트는 구도 검증용이다.
4. 2026 레퍼런스는 2036 시트를 편집 입력으로 파생하고 다른 사람으로 변하면 재생성한다.
5. 얼굴이 흔들리면 새 인물을 채택하지 않고 후면/손/화면 인서트로 대체한다.
6. 최종 선택 전 얼굴·손가락·옷 단추·스마트폰·노트북 힌지 일관성을 확인한다.

캐릭터 테스트 원본과 검수 결과는 [에셋 목록](../assets/asset-manifest.md)에 기록한다.
