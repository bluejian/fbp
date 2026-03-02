<template>
  <div class="forest-world">
    <!-- HERO SECTION -->
    <header class="hero-section">
      <div class="hero-bg"></div>
      <div class="hero-content fade-in">
        <h1 class="hero-title">Jian's 1st Birthday</h1>
        <div class="main-portrait-wrap">
          <img :src="getImg('/images/photo1.jpg')" alt="Jian Portrait" class="main-portrait" />
        </div>
        
        <div class="scroll-ind">
          <span>아래로 스크롤해주세요</span>
          <div class="arrow-down">▼</div>
        </div>
      </div>
    </header>

    <!-- GREETING SECTION -->
    <section class="greeting-section fade-in">
      <div class="greeting-card">
        <div class="leaf-decor top-left">🌿</div>
        <p class="greeting-text">
          어느 작은 숲속에 피어난 새싹처럼<br/><br/>
          조금씩 자라나는 지안이를 보며<br/>
          저희 가족은 매일 감사와 행복을 배웁니다.<br/><br/><br/>
          
          지안이의 여정이 햇살처럼 따뜻하고<br/>
          나무처럼 푸르게 자라날 수 있도록<br/>
          귀한 걸음 하시어 축복해 주시면 감사하겠습니다.
        </p>
        <div class="leaf-decor bottom-right">🌿</div>
      </div>
    </section>

    <!-- GALLERY SECTION -->
    <section class="gallery-section">
      <h2 class="section-title fade-in">Memory Leaves</h2>
      <div class="gallery-grid">
        <div 
          v-for="(photo, i) in photos" 
          :key="i"
          class="gallery-item-wrap fade-in"
          :style="{ transitionDelay: `${(i % 2) * 0.15}s` }"
        >
          <div class="polaroid" @click="openModal(i)">
            <img :src="photo" alt="gallery image" />
          </div>
        </div>
      </div>
      
      <!-- Easter Egg Mario Link -->
      <div class="easter-egg-wrap fade-in">
        <router-link to="/mario" class="hidden-mario-link">
          <span class="mushroom-hint">🍄</span>
        </router-link>
      </div>
    </section>

    <!-- INFO & LOCATION SECTION -->
    <section class="info-section fade-in">
      <div class="info-card">
        <div class="info-header">INVITATION</div>
        
        <!-- Invitation Photos Carousel -->
        <div class="info-carousel">
          <button class="carousel-btn prev" @click.stop="prevInfoPhoto" v-if="infoPhotos.length > 1">◀</button>
          
          <div class="carousel-window" @click="openModal('info', currentInfoPhoto)">
            <div class="carousel-track" :style="{ transform: `translateX(${-currentInfoPhoto * 100}%)` }">
              <div class="carousel-slide" v-for="(photo, i) in infoPhotos" :key="'info-'+i">
                <img :src="photo" alt="Parking & Location Info" />
              </div>
            </div>
          </div>
          
          <button class="carousel-btn next" @click.stop="nextInfoPhoto" v-if="infoPhotos.length > 1">▶</button>
          
          <div class="carousel-dots">
            <span v-for="(_, i) in infoPhotos" :key="'dot-'+i" :class="['dot', { active: i === currentInfoPhoto }]"></span>
          </div>
        </div>

        <div class="info-body">
          <p><strong>일시:</strong> {{ eventDate }}</p>
          <p><strong>장소:</strong> {{ venueName }}</p>
        </div>
        <div class="map-actions">
          <a :href="kakaoMapUrl" target="_blank" class="map-btn kakao">카카오맵</a>
          <a :href="naverMapUrl" target="_blank" class="map-btn naver">네이버맵</a>
        </div>
        <div class="family-sig">
          지안이네 가족 올림
        </div>
      </div>
    </section>

    <!-- Photo Modal -->
    <Transition name="fade">
      <div v-if="modalOpen" class="photo-modal" @click="closeModal">
        <div class="modal-content" @click.stop>
          <button class="nav-btn prev-btn" @click.stop="prevPhoto" v-if="activePhotos.length > 1">◀</button>
          <img :src="activePhotos[modalIndex]" class="modal-img" />
          <button class="nav-btn next-btn" @click.stop="nextPhoto" v-if="activePhotos.length > 1">▶</button>
        </div>
        <div class="modal-close" @click="closeModal">✕</div>
      </div>
    </Transition>
  </div>
</template>

<script setup>
import { getImg } from '../utils/imagePath'
import { ref, onMounted } from 'vue'

const eventDate = ref('2026년 3월 7일 (토) 오후 6:00')
const venueName = ref('루엘 파티플레이스 (수원)')
const kakaoMapUrl = 'https://map.kakao.com/link/to/236178717'
const naverMapUrl = 'https://naver.me/GOPeemGQ'

// Use actual user photos
const photos = ref([
  getImg('/images/boxjian.jpeg'),
  getImg('/images/angjian.jpeg'),
  getImg('/images/boojian.jpeg'),
  getImg('/images/smilejian.jpeg'),
  getImg('/images/angryjian.jpeg'),
  getImg('/images/jiansmile.jpeg')
])

// Info/Parking Photos
const infoPhotos = ref([
  getImg('/images/mario/parking2.jpg'),
  getImg('/images/mario/parking1.png'),
])

// === INFO CAROUSEL LOGIC ===
const currentInfoPhoto = ref(0)
const nextInfoPhoto = () => { currentInfoPhoto.value = (currentInfoPhoto.value + 1) % infoPhotos.value.length }
const prevInfoPhoto = () => { currentInfoPhoto.value = (currentInfoPhoto.value - 1 + infoPhotos.value.length) % infoPhotos.value.length }

// === MODAL LOGIC ===
const modalOpen = ref(false)
const modalIndex = ref(0)
const modalType = ref('gallery') // 'gallery' or 'info'

import { computed } from 'vue'
const activePhotos = computed(() => modalType.value === 'gallery' ? photos.value : infoPhotos.value)

const openModal = (type, i) => { 
  modalType.value = type
  modalIndex.value = i
  modalOpen.value = true 
}
const closeModal = () => { modalOpen.value = false }
const nextPhoto = () => { modalIndex.value = (modalIndex.value + 1) % activePhotos.value.length }
const prevPhoto = () => { modalIndex.value = (modalIndex.value - 1 + activePhotos.value.length) % activePhotos.value.length }

// === INTERSECTION OBSERVER FOR FADE-INS ===
onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      if (entry.isIntersecting) {
        entry.target.classList.add('visible')
      }
    })
  }, { threshold: 0.15 })

  document.querySelectorAll('.fade-in').forEach((el) => {
    observer.observe(el)
  })
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@400;700&display=swap');

.forest-world {
  --green-dark: #2c3e2d;
  --green-mid: #4a5d23;
  --beige-bg: #fdfbf7;
  --wood-brown: #6b4423;
  --text-dark: #3a3a3a;
  
  background-color: var(--beige-bg);
  background-image: url('/images/wt_py.jpeg');
  background-repeat: repeat;
  background-size: 400px; /* Adjust size to make the pattern look natural */
  background-blend-mode: multiply; /* Optional, helps it blend into the beige */
  font-family: 'Nanum Myeongjo', serif;
  color: var(--text-dark);
  min-height: 100vh;
}

/* FADE-IN ANIMATION CLASSES */
.fade-in {
  opacity: 0;
  transform: translateY(40px);
  transition: opacity 1s ease-out, transform 1s ease-out;
}
.fade-in.visible {
  opacity: 1;
  transform: translateY(0);
}

/* --- HERO SCENE --- */
.hero-section {
  position: relative;
  min-height: 100dvh;
  display: flex; flex-direction: column; justify-content: center; align-items: center;
  text-align: center;
  overflow: hidden;
}
.hero-bg {
  position: absolute; inset: 0;
  background: radial-gradient(circle at 50% 30%, rgba(253, 251, 247, 1) 0%, rgba(220, 215, 195, 0.4) 100%);
  z-index: 0;
}
.hero-content {
  position: relative; z-index: 10;
  display: flex; flex-direction: column; align-items: center;
}
.hero-title {
  font-size: 8vw; color: var(--green-dark);
  margin-bottom: 4vh; font-weight: 700; letter-spacing: 2px;
}
.main-portrait-wrap {
  width: 65vw; max-width: 320px;
  aspect-ratio: 3/4;
  border-radius: 200px 200px 10px 10px;
  overflow: hidden;
  box-shadow: 0 15px 35px rgba(44, 62, 45, 0.15);
  border: 10px solid #fff;
  margin-bottom: 2vh;
}
.main-portrait {
  width: 100%; height: 100%; object-fit: cover;
}
.scroll-ind {
  position: absolute; bottom: -10vh; left: 50%; transform: translateX(-50%);
  display: flex; flex-direction: column; align-items: center;
  font-size: 3vw; color: var(--green-mid); opacity: 0.7; z-index: 10;
}
.arrow-down {
  margin-top: 8px; font-size: 4vw;
  animation: bounce 2s infinite ease-in-out;
}
@keyframes bounce {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-8px); }
}

/* --- GREETING SCENE --- */
.greeting-section {
  padding: 20vh 5vw;
  display: flex; justify-content: center; align-items: center;
  /* Make greeting background slightly transparent to let pattern show through, or remove the background gradient entirely */
  background: transparent;
}
.greeting-card {
  background: #fff;
  padding: 12vw 8vw;
  border-radius: 16px;
  box-shadow: 0 20px 50px rgba(44, 62, 45, 0.08);
  position: relative;
  max-width: 500px;
  width: 90vw;
  border: 1px solid rgba(107, 68, 35, 0.1);
  text-align: center;
}
.leaf-decor {
  position: absolute;
  font-size: 6vw;
  opacity: 0.6;
}
.leaf-decor.top-left { top: 6vw; left: 6vw; transform: scaleX(-1); }
.leaf-decor.bottom-right { bottom: 6vw; right: 6vw; }
.greeting-text {
  font-size: 4.2vw; line-height: 2.4; color: var(--wood-brown); margin: 0;
}

/* --- GALLERY SCENE --- */
.gallery-section {
  padding: 10vh 5vw;
  /* Soft overlay to differentiate from greeting, but still let pattern show slightly if desired. 
     Using a semi-transparent gradient */
  background: linear-gradient(180deg, rgba(253, 251, 247, 0) 0%, rgba(230, 227, 218, 0.8) 100%);
  text-align: center;
}
.section-title {
  font-size: 7vw; color: var(--green-dark); margin-bottom: 8vh;
  letter-spacing: 3px; font-weight: 400; font-family: 'Times New Roman', serif;
}
.gallery-grid {
  display: grid;
  grid-template-columns: repeat(2, 1fr);
  gap: 4vw;
  margin-bottom: 10vh;
}
.gallery-item-wrap {
  display: flex; justify-content: center;
}
/* Polaroid Style for standard scrolling */
.polaroid {
  background: #fff; padding: 2vw 2vw 10vw 2vw;
  box-shadow: 0 10px 20px rgba(0,0,0,0.08);
  cursor: pointer; position: relative;
  transition: transform 0.3s, box-shadow 0.3s;
}
/* Alternate rotation for organic feel */
.gallery-grid .gallery-item-wrap:nth-child(even) .polaroid { transform: rotate(2deg); }
.gallery-grid .gallery-item-wrap:nth-child(odd) .polaroid { transform: rotate(-2deg); }
.polaroid:hover { transform: rotate(0deg) scale(1.03) !important; box-shadow: 0 15px 30px rgba(0,0,0,0.12); z-index: 5; }
.polaroid img {
  width: 100%; aspect-ratio: 1/1; object-fit: cover;
  border-radius: 2px;
}

/* Easter Egg */
.easter-egg-wrap {
  margin-top: 5vh; display: flex; justify-content: center;
}
.hidden-mario-link {
  display: inline-block; width: 50px; height: 50px;
  text-decoration: none; text-align: center; line-height: 50px;
  background: rgba(44, 62, 45, 0.05); border-radius: 50%;
  transition: transform 0.3s, background 0.3s; border: 1px dashed rgba(44, 62, 45, 0.2);
}
.hidden-mario-link:hover { transform: scale(1.1); background: rgba(44, 62, 45, 0.1); }
.mushroom-hint { font-size: 24px; filter: grayscale(0.8); opacity: 0.6; }
.hidden-mario-link:hover .mushroom-hint { filter: grayscale(0); opacity: 1; }

/* --- INFO SCENE --- */
.info-section {
  padding: 10vh 5vw 15vh 5vw;
  display: flex; justify-content: center; align-items: center;
  background: transparent;
}
.info-card {
  background: #fff; width: 100%; max-width: 450px;
  padding: 10vw 6vw; border-radius: 12px;
  box-shadow: 0 10px 40px rgba(107, 68, 35, 0.08);
  text-align: center;
  border: 1px solid rgba(107, 68, 35, 0.1);
}
.info-header {
  color: var(--green-mid); font-size: 5vw; margin-bottom: 6vw; letter-spacing: 3px; font-weight: 700;
}

/* Info Carousel */
.info-carousel {
  position: relative;
  margin-bottom: 6vw;
  width: 100%;
}
.carousel-window {
  width: 100%;
  aspect-ratio: 4/3;
  overflow: hidden;
  border-radius: 8px;
  box-shadow: 0 5px 15px rgba(0,0,0,0.1);
  background: #fdfbf7;
  cursor: zoom-in;
}
.carousel-track {
  display: flex;
  height: 100%;
  transition: transform 0.4s ease-in-out;
}
.carousel-slide {
  min-width: 100%;
  height: 100%;
  display: flex;
  justify-content: center;
  align-items: center;
}
.carousel-slide img {
  width: 100%;
  height: 100%;
  object-fit: cover;
}
.carousel-btn {
  position: absolute;
  top: 50%;
  transform: translateY(-50%);
  background: rgba(255,255,255,0.8);
  color: var(--green-dark);
  border: none;
  width: 8vw; height: 8vw; max-width: 40px; max-height: 40px;
  border-radius: 50%;
  display: flex; justify-content: center; align-items: center;
  font-size: 3.5vw;
  cursor: pointer;
  z-index: 2;
  box-shadow: 0 2px 10px rgba(0,0,0,0.1);
}
.carousel-btn.prev { left: -4vw; }
.carousel-btn.next { right: -4vw; }
@media (min-width: 768px) {
  .carousel-btn.prev { left: -20px; font-size: 16px; }
  .carousel-btn.next { right: -20px; font-size: 16px; }
}

.carousel-dots {
  display: flex; justify-content: center; gap: 6px; margin-top: 12px;
}
.dot {
  width: 6px; height: 6px; border-radius: 50%; background: #ddd; transition: 0.3s;
}
.dot.active {
  background: var(--green-dark); transform: scale(1.3);
}

.info-body p {
  color: var(--text-dark); font-size: 4vw; line-height: 2; margin: 0 0 2vw 0;
}
.map-actions {
  display: flex; gap: 3vw; justify-content: center; margin-top: 8vw; margin-bottom: 8vw;
}
.map-btn {
  flex: 1; padding: 3vw 0; border-radius: 8px; text-decoration: none; font-size: 3.8vw;
  font-weight: 700; transition: opacity 0.2s;
}
.map-btn.kakao { background: #FEE500; color: #392020; }
.map-btn.naver { background: #03C75A; color: #fff; }
.map-btn:active { opacity: 0.8; }

.family-sig {
  font-size: 4.5vw; color: var(--wood-brown); margin-top: 4vw;
  border-top: 1px solid #eee; padding-top: 6vw; font-weight: 700;
}

/* --- MODAL --- */
.photo-modal {
  position: fixed; inset: 0;
  background: rgba(20, 25, 20, 0.95); z-index: 9999;
  display: flex; justify-content: center; align-items: center;
  backdrop-filter: blur(8px);
}
.modal-content {
  position: relative; width: 90vw; max-width: 800px; height: 80dvh;
  display: flex; justify-content: center; align-items: center;
}
.modal-img {
  max-width: 100%; max-height: 100%; object-fit: contain;
  box-shadow: 0 0 30px rgba(0,0,0,0.4); border-radius: 4px; border: 4px solid #fff;
}
.modal-close {
  position: absolute; top: 3vh; right: 5vw;
  color: #fff; font-size: 8vw; cursor: pointer; opacity: 0.7; z-index: 10000;
}
.nav-btn {
  background: none; border: none; color: #fff; font-size: 8vw;
  cursor: pointer; position: absolute; top: 50%; transform: translateY(-50%);
  opacity: 0.8; padding: 4vw; z-index: 10000;
}
.prev-btn { left: -5vw; }
.next-btn { right: -5vw; }

.fade-enter-active, .fade-leave-active { transition: opacity 0.3s ease; }
.fade-enter-from, .fade-leave-to { opacity: 0; }

/* DESKTOP ADJUSTMENTS */
@media (min-width: 768px) {
  .hero-title { font-size: 3rem; }
  .hero-subtitle { font-size: 1.2rem; }
  .scroll-ind { font-size: 1rem; }
  .arrow-down { font-size: 1.5rem; }
  
  .greeting-text { font-size: 1.2rem; }
  
  .section-title { font-size: 2.5rem; margin-bottom: 60px; }
  .gallery-grid { gap: 30px; }
  
  .info-card { padding: 50px 40px; }
  .info-header { font-size: 1.6rem; margin-bottom: 40px; }
  .info-carousel { margin-bottom: 40px; }
  .info-body p { font-size: 1.1rem; margin-bottom: 15px; }
  .map-actions { gap: 20px; margin-top: 40px; margin-bottom: 40px; }
  .map-btn { padding: 15px 0; font-size: 1.1rem; }
  .family-sig { font-size: 1.2rem; padding-top: 30px; }
  
  .modal-close { font-size: 2rem; right: 30px; top: 30px; }
  .nav-btn { font-size: 3rem; }
  .prev-btn { left: 0; }
  .next-btn { right: 0; }
}
</style>
