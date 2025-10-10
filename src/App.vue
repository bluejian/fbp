<template>
  <div class="invitation">
    <!-- 메인 헤더 -->
    <section class="hero" :style="{ backgroundImage: `url(${heroBackgroundImage})` }">
      <div class="hero-overlay"></div>
      <div class="hero-content">
        <div class="hero-decoration">🐍</div>
        <h1 class="baby-name">{{ babyName }}</h1>
        <div class="name-decoration"></div>
        <p class="event-title">첫 돌잔치에 초대합니다</p>
        <div class="date-info">
          <p class="date">{{ eventDate }}</p>
          <p class="time">{{ eventTime }}</p>
        </div>
        <div class="hero-decoration">🎂</div>
      </div>
    </section>

    <!-- 초대 메시지 -->
    <section class="message">
      <div class="container">
        <p class="greeting">
          {{ message }}
        </p>
      </div>
    </section>

    <!-- 아기 사진 갤러리 -->
    <section class="gallery">
      <div class="container">
        <h2>소중한 순간들</h2>
        <div class="photo-grid">
          <div
            v-for="(photo, index) in photos"
            :key="index"
            class="photo-item"
            :style="{ backgroundImage: `url(${photo})` }"
            @click="openModal(index)"
          >
          </div>
        </div>
      </div>
    </section>

    <!-- 이미지 모달 -->
    <Teleport to="body">
      <div v-if="modalOpen" class="modal-overlay" @click="closeModal">
        <button class="modal-close" @click="closeModal">✕</button>
        <div
          class="modal-content"
          @click.stop
          @touchstart="handleTouchStart"
          @touchmove="handleTouchMove"
          @touchend="handleTouchEnd"
        >
          <button class="modal-prev" @click="prevImage" v-if="photos.length > 1">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="15 18 9 12 15 6"></polyline>
            </svg>
          </button>
          <img :src="photos[currentImageIndex]" :alt="`사진 ${currentImageIndex + 1}`" class="modal-image">
          <button class="modal-next" @click="nextImage" v-if="photos.length > 1">
            <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
              <polyline points="9 18 15 12 9 6"></polyline>
            </svg>
          </button>
        </div>
        <div class="modal-counter">{{ currentImageIndex + 1 }} / {{ photos.length }}</div>
      </div>
    </Teleport>

    <!-- 일시 및 장소 -->
    <section class="details">
      <div class="container">
        <h2>일시 및 장소</h2>
        <div class="detail-item">
          <span class="icon">📅</span>
          <div>
            <p class="label">일시</p>
            <p class="value">{{ eventDate }} {{ eventTime }}</p>
          </div>
        </div>
        <div class="detail-item">
          <span class="icon">📍</span>
          <div>
            <p class="label">장소</p>
            <p class="value">{{ venueName }}</p>
            <p class="address">{{ venueAddress }}</p>
          </div>
        </div>
        <div class="detail-item">
          <span class="icon">☎️</span>
          <div>
            <p class="label">연락처</p>
            <p class="value">{{ contactNumber }}</p>
          </div>
        </div>
      </div>
    </section>

    <!-- 지도 -->
    <section class="map">
      <div class="container">
        <h2>오시는 길</h2>
        <div class="map-placeholder">
          <p>지도가 여기에 표시됩니다</p>
          <p class="map-note">카카오맵 또는 네이버맵 API를 연동할 수 있습니다</p>
        </div>
        <div class="map-buttons">
          <a :href="kakaoMapUrl" target="_blank" class="map-btn">카카오맵</a>
          <a :href="naverMapUrl" target="_blank" class="map-btn">네이버맵</a>
        </div>
      </div>
    </section>

    <!-- 마음 전하실 곳 -->
    <section class="account">
      <div class="container">
        <h2>마음 전하실 곳</h2>
        <div class="account-info">
          <p class="account-holder">신랑측: {{ groomAccount }}</p>
          <p class="account-holder">신부측: {{ brideAccount }}</p>
        </div>
      </div>
    </section>

    <!-- 푸터 -->
    <footer class="footer">
      <p>{{ babyName }}이의 첫 돌을 축하해주세요 💝</p>
    </footer>
  </div>
</template>

<script setup>
import { ref } from 'vue'

// 아기 정보
const babyName = ref('이지안')

// 히어로 배경 이미지 (public/images/ 폴더에 이미지를 넣고 파일명만 변경하세요)
// 예: 'hero.jpg'를 넣었다면 '/images/hero.jpg'로 변경
const heroBackgroundImage = ref('/images/hero.jpg')

// 행사 정보
const eventDate = ref('2026년 03월 07일 토요일')
const eventTime = ref('오전 11시 30분')
const venueName = ref('○○웨딩홀 2층 그랜드홀')
const venueAddress = ref('서울특별시 강남구 테헤란로 123')
const contactNumber = ref('010-1234-5678')

// 초대 메시지
const message = ref(`
  태어나서 첫 돌을 맞이하는
  저희 아이의 소중한 날에
  함께해 주시면 감사하겠습니다.

  보내주신 사랑과 축복 가슴 깊이 간직하겠습니다.
`)

// 사진 갤러리 (public/images/ 폴더에 이미지를 넣고 파일명을 변경하세요)
// 예: photo1.jpg, photo2.jpg, photo3.jpg 등
const photos = ref([
  '/images/photo1.jpg',
  '/images/photo2.jpg',
  '/images/photo3.jpg',
  '/images/photo4.jpg',
  '/images/photo5.jpg',
  '/images/photo6.jpg',
])

// 계좌 정보
const groomAccount = ref('OO은행 123-456-789012 (아빠 이름)')
const brideAccount = ref('OO은행 987-654-321098 (엄마 이름)')

// 지도 링크
const kakaoMapUrl = ref('https://map.kakao.com/')
const naverMapUrl = ref('https://map.naver.com/')

// 이미지 모달
const modalOpen = ref(false)
const currentImageIndex = ref(0)

// 터치 스와이프
let touchStartX = 0
let touchEndX = 0

const handleTouchStart = (e) => {
  touchStartX = e.changedTouches[0].screenX
}

const handleTouchMove = (e) => {
  touchEndX = e.changedTouches[0].screenX
}

const handleTouchEnd = () => {
  if (touchStartX - touchEndX > 50) {
    // 왼쪽으로 스와이프 (다음 이미지)
    nextImage()
  }
  if (touchEndX - touchStartX > 50) {
    // 오른쪽으로 스와이프 (이전 이미지)
    prevImage()
  }
}

// 키보드 이벤트
const handleKeyDown = (e) => {
  if (!modalOpen.value) return

  if (e.key === 'Escape') {
    closeModal()
  } else if (e.key === 'ArrowLeft') {
    prevImage()
  } else if (e.key === 'ArrowRight') {
    nextImage()
  }
}

const openModal = (index) => {
  currentImageIndex.value = index
  modalOpen.value = true
  document.body.style.overflow = 'hidden'
  window.addEventListener('keydown', handleKeyDown)
}

const closeModal = () => {
  modalOpen.value = false
  document.body.style.overflow = ''
  window.removeEventListener('keydown', handleKeyDown)
}

const nextImage = () => {
  currentImageIndex.value = (currentImageIndex.value + 1) % photos.value.length
}

const prevImage = () => {
  currentImageIndex.value = (currentImageIndex.value - 1 + photos.value.length) % photos.value.length
}
</script>

<style scoped>
.invitation {
  max-width: 100%;
  background: #faf9f7;
}

/* 히어로 섹션 */
.hero {
  min-height: 100vh;
  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
  display: flex;
  align-items: center;
  justify-content: center;
  text-align: center;
  padding: 60px 20px;
  position: relative;
}

.hero-overlay {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: linear-gradient(
    135deg,
    rgba(255, 236, 210, 0.85) 0%,
    rgba(252, 182, 159, 0.85) 100%
  );
  backdrop-filter: blur(2px);
}

.hero-content {
  position: relative;
  z-index: 1;
  color: #fff;
  text-shadow: 2px 2px 8px rgba(0,0,0,0.2);
  max-width: 800px;
  padding: 40px;
  background: rgba(255, 255, 255, 0.1);
  border-radius: 30px;
  backdrop-filter: blur(10px);
  border: 2px solid rgba(255, 255, 255, 0.3);
}

.hero-decoration {
  font-size: 3rem;
  margin: 20px 0;
  animation: float 3s ease-in-out infinite;
}

.baby-name {
  font-size: 4rem;
  font-weight: 700;
  margin-bottom: 20px;
  animation: fadeInUp 1s ease;
  letter-spacing: 0.05em;
}

.name-decoration {
  width: 120px;
  height: 3px;
  background: linear-gradient(to right, transparent, #fff, transparent);
  margin: 0 auto 30px;
  border-radius: 2px;
  animation: fadeInUp 1s ease 0.1s backwards;
}

.event-title {
  font-size: 1.6rem;
  margin-bottom: 40px;
  font-weight: 300;
  animation: fadeInUp 1s ease 0.2s backwards;
  letter-spacing: 0.1em;
}

.date-info {
  animation: fadeInUp 1s ease 0.4s backwards;
  padding: 20px;
  background: rgba(255, 255, 255, 0.15);
  border-radius: 20px;
  margin-top: 20px;
}

.date {
  font-size: 1.4rem;
  margin-bottom: 10px;
  font-weight: 500;
}

.time {
  font-size: 1.2rem;
  opacity: 0.95;
}

/* 섹션 공통 */
section {
  padding: 60px 20px;
}

.container {
  max-width: 600px;
  margin: 0 auto;
}

h2 {
  text-align: center;
  font-size: 2rem;
  margin-bottom: 40px;
  color: #d4896b;
}

/* 메시지 섹션 */
.message {
  background: #fff;
}

.greeting {
  text-align: center;
  line-height: 2;
  white-space: pre-line;
  font-size: 1.1rem;
  color: #555;
}

/* 갤러리 */
.gallery {
  background: #f5f3f0;
}

.photo-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
}

@media (max-width: 768px) {
  .photo-grid {
    grid-template-columns: repeat(2, 1fr);
  }
}

.photo-item {
  aspect-ratio: 1;
  background-size: cover;
  background-position: center;
  border-radius: 12px;
  box-shadow: 0 4px 12px rgba(0,0,0,0.1);
  transition: transform 0.3s ease;
  cursor: pointer;
}

.photo-item:hover {
  transform: scale(1.05);
}

/* 상세 정보 */
.details {
  background: #fff;
}

.detail-item {
  display: flex;
  gap: 20px;
  margin-bottom: 32px;
  padding: 20px;
  background: #f9f9f9;
  border-radius: 12px;
}

.icon {
  font-size: 2rem;
}

.label {
  font-weight: 600;
  color: #d4896b;
  margin-bottom: 8px;
}

.value {
  font-size: 1.1rem;
  margin-bottom: 4px;
}

.address {
  color: #666;
  font-size: 0.95rem;
}

/* 지도 */
.map {
  background: #f5f3f0;
}

.map-placeholder {
  background: #fff;
  padding: 80px 20px;
  text-align: center;
  border-radius: 12px;
  margin-bottom: 20px;
  border: 2px dashed #ddd;
}

.map-note {
  color: #999;
  font-size: 0.9rem;
  margin-top: 8px;
}

.map-buttons {
  display: flex;
  gap: 12px;
  justify-content: center;
}

.map-btn {
  flex: 1;
  max-width: 150px;
  padding: 12px 24px;
  background: #fff;
  border: 2px solid #d4896b;
  color: #d4896b;
  text-decoration: none;
  border-radius: 8px;
  font-weight: 600;
  text-align: center;
  transition: all 0.3s ease;
}

.map-btn:hover {
  background: #d4896b;
  color: #fff;
}

/* 계좌 정보 */
.account {
  background: #fff;
}

.account-info {
  text-align: center;
  padding: 20px;
  background: #f9f9f9;
  border-radius: 12px;
}

.account-holder {
  margin-bottom: 12px;
  font-size: 1.05rem;
  line-height: 1.8;
}

/* 푸터 */
.footer {
  background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
  color: #fff;
  text-align: center;
  padding: 40px 20px;
  font-size: 1.1rem;
}

/* 애니메이션 */
@keyframes fadeInUp {
  from {
    opacity: 0;
    transform: translateY(30px);
  }
  to {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes float {
  0%, 100% {
    transform: translateY(0px);
  }
  50% {
    transform: translateY(-15px);
  }
}

/* 반응형 */
@media (max-width: 640px) {
  .hero {
    min-height: 100vh;
    padding: 40px 20px;
  }

  .hero-content {
    padding: 30px 20px;
  }

  .hero-decoration {
    font-size: 2rem;
    margin: 10px 0;
  }

  .baby-name {
    font-size: 2.5rem;
  }

  .name-decoration {
    width: 80px;
  }

  .event-title {
    font-size: 1.2rem;
  }

  .date {
    font-size: 1.1rem;
  }

  .time {
    font-size: 1rem;
  }

  h2 {
    font-size: 1.6rem;
  }

  .photo-grid {
    grid-template-columns: 1fr;
  }
}

/* 이미지 모달 */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background: rgba(0, 0, 0, 0.9);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 9999;
  animation: fadeIn 0.3s ease;
}

.modal-content {
  position: relative;
  max-width: 90vw;
  max-height: 90vh;
  display: flex;
  align-items: center;
  justify-content: center;
}

.modal-image {
  max-width: 100%;
  max-height: 90vh;
  object-fit: contain;
  border-radius: 8px;
  animation: zoomIn 0.3s ease;
}

.modal-close {
  position: fixed;
  top: 20px;
  right: 20px;
  background: rgba(0, 0, 0, 0.5);
  border: 2px solid rgba(255, 255, 255, 0.8);
  color: #fff;
  width: 44px;
  height: 44px;
  border-radius: 50%;
  font-size: 24px;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  z-index: 10001;
}

.modal-close:hover {
  background: rgba(255, 255, 255, 0.9);
  color: #000;
  transform: rotate(90deg);
}

.modal-prev,
.modal-next {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(0, 0, 0, 0.5);
  border: 2px solid rgba(255, 255, 255, 0.8);
  color: #fff;
  width: 50px;
  height: 50px;
  border-radius: 50%;
  cursor: pointer;
  display: flex;
  align-items: center;
  justify-content: center;
  transition: all 0.3s ease;
  z-index: 10001;
}

.modal-prev {
  left: 20px;
}

.modal-next {
  right: 20px;
}

.modal-prev:hover,
.modal-next:hover {
  background: rgba(255, 255, 255, 0.9);
  color: #000;
  transform: translateY(-50%) scale(1.15);
}

.modal-counter {
  position: fixed;
  bottom: 30px;
  left: 50%;
  transform: translateX(-50%);
  color: #fff;
  font-size: 16px;
  background: rgba(0, 0, 0, 0.6);
  padding: 10px 20px;
  border-radius: 25px;
  border: 1px solid rgba(255, 255, 255, 0.3);
  z-index: 10001;
}

@keyframes fadeIn {
  from {
    opacity: 0;
  }
  to {
    opacity: 1;
  }
}

@keyframes zoomIn {
  from {
    opacity: 0;
    transform: scale(0.8);
  }
  to {
    opacity: 1;
    transform: scale(1);
  }
}

@media (max-width: 768px) {
  .modal-close {
    top: 15px;
    right: 15px;
    width: 40px;
    height: 40px;
    font-size: 20px;
  }

  .modal-prev,
  .modal-next {
    width: 44px;
    height: 44px;
    opacity: 0.8;
  }

  .modal-prev {
    left: 10px;
  }

  .modal-next {
    right: 10px;
  }

  .modal-counter {
    bottom: 20px;
    font-size: 14px;
    padding: 8px 16px;
  }
}
</style>
