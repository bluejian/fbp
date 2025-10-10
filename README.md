# 돌잔치 모바일 초대장

Vite + Vue3로 만든 반응형 돌잔치 초대장입니다.

## 개발 환경 설정

```bash
# 의존성 설치
npm install

# 개발 서버 실행
npm run dev

# 빌드
npm run build

# 빌드 결과 미리보기
npm run preview
```

## GitHub Pages 배포

### 1. GitHub 저장소 생성
- 저장소 이름: 원하는 이름 (예: `rock`, `doljanchee`)

### 2. vite.config.js 수정
```javascript
base: '/저장소이름/', // 예: '/rock/'
```

### 3. GitHub Pages 설정
1. GitHub 저장소 → Settings → Pages
2. Source: GitHub Actions 선택

### 4. 코드 푸시
```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/jiwonman/저장소이름.git
git push -u origin main
```

푸시하면 자동으로 배포됩니다!
배포 URL: `https://jiwonman.github.io/저장소이름/`

## 이미지 추가하기

### 1. 이미지 파일 준비
- 히어로 배경: `hero.jpg` (가로 1600px 이상 권장)
- 갤러리 사진: `photo1.jpg`, `photo2.jpg`, ... `photo6.jpg` (정사각형 권장)

### 2. 이미지 추가
```
public/
  images/
    hero.jpg         <- 히어로 배경 이미지
    photo1.jpg       <- 갤러리 사진 1
    photo2.jpg       <- 갤러리 사진 2
    photo3.jpg       <- 갤러리 사진 3
    photo4.jpg       <- 갤러리 사진 4
    photo5.jpg       <- 갤러리 사진 5
    photo6.jpg       <- 갤러리 사진 6
```

### 3. 파일명이 다른 경우
`src/App.vue` 파일에서 이미지 경로를 수정하세요:
```javascript
// 예: baby-main.png를 사용하는 경우
const heroBackgroundImage = ref('/images/baby-main.png')

// 예: 다른 파일명을 사용하는 경우
const photos = ref([
  '/images/my-photo-1.jpg',
  '/images/my-photo-2.jpg',
  // ...
])
```

**중요**: 빌드 시 `public` 폴더의 내용이 자동으로 `dist`에 복사됩니다!

## 커스터마이징

`src/App.vue` 파일에서 다음 정보를 수정하세요:

- **아기 이름**: `babyName`
- **행사 일시**: `eventDate`, `eventTime`
- **장소 정보**: `venueName`, `venueAddress`
- **연락처**: `contactNumber`
- **초대 메시지**: `message`
- **계좌 정보**: `groomAccount`, `brideAccount`

## 기능

- ✅ 반응형 디자인 (모바일 최적화)
- ✅ 아기 사진 갤러리
- ✅ 일시 및 장소 안내
- ✅ 지도 링크 (카카오맵, 네이버맵)
- ✅ 계좌 정보
- ✅ 부드러운 애니메이션

## 추가 가능한 기능

- 카카오맵/네이버맵 API 연동
- 참석 여부 확인 기능
- 방명록
- 음악 재생
- 카카오톡 공유하기
