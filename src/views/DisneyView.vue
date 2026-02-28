<template>
  <div class="disney-theme">
    <div class="scroll-container">
      <!-- Magical Intro -->
      <section class="intro-section reveal">
        <div class="stars-bg"></div>
        <div class="content">
          <div class="sparkle-text">Once Upon a Time...</div>
          <h1 class="main-title">A Magical Celebration</h1>
          <div class="baby-portrait">
            <div class="castle-outline">
              <img :src="getImg('/images/disney-bg.png')" alt="Castle" class="castle-img" />
            </div>
            <!-- <img :src="getImg('/images/baby-cutout.png')" alt="Jian" class="baby-img" /> -->
          </div>
          <div class="welcome-text">지안이의 첫 번째 생일 파티에 초대합니다</div>
        </div>
      </section>

      <!-- Story Section -->
      <section class="story-section reveal">
        <div class="paper-texture">
          <p class="greeting">{{ message }}</p>
          <div class="divider">✨</div>
        </div>
      </section>

      <!-- Gallery -->
      <section class="gallery-section reveal">
        <h2 class="section-title">Magical Moments</h2>
        <div class="gallery-grid">
          <div 
            v-for="(photo, index) in photos" 
            :key="index"
            class="gallery-item"
            :style="{ backgroundImage: `url(${photo})` }"
            @click="openModal(index)"
          ></div>
        </div>
      </section>

      <!-- Event Info -->
      <section class="info-section reveal">
        <div class="info-card">
          <div class="info-row">
            <div class="label">WHEN</div>
            <div class="value">{{ eventDate }}</div>
          </div>
          <div class="info-row">
            <div class="label">WHERE</div>
            <div class="value">{{ venueName }}</div>
          </div>
          <div class="info-row">
            <div class="label">MAP</div>
            <div class="map-placeholder">루엘 파티플레이스</div>
            <div class="map-buttons">
              <a :href="kakaoMapUrl" target="_blank" class="btn kakao">카카오맵</a>
              <a :href="naverMapUrl" target="_blank" class="btn naver">네이버맵</a>
            </div>
          </div>
        </div>
      </section>

      <footer class="footer">
        <div class="signature">Princess JIAN</div>
      </footer>
    </div>

    <!-- Modal (Simplification for brevity, same as before) -->
    <div v-if="modalOpen" class="modal" @click="modalOpen = false">
       <img :src="photos[currentIndex]" class="modal-img" />
    </div>
  </div>
</template>

<script setup>
import { getImg } from '../utils/imagePath'
import { ref, onMounted } from 'vue'

const message = ref(`꿈같은 시간들이 모여\n지안이의 첫 번째 생일이 되었습니다.\n\n지안이의 앞날이 동화처럼 반짝일 수 있도록\n함께 자리를 빛내어 마법을 더해주세요.`)
const eventDate = ref('2026. 03. 07 SAT PM 6:00')
const venueName = ref('루엘 파티플레이스 (수원)')
const photos = ref([getImg('/images/photo1.jpg'), getImg('/images/photo2.jpg'), getImg('/images/photo3.jpg'), getImg('/images/photo4.jpg')])
const kakaoMapUrl = 'https://map.kakao.com/link/to/236178717'
const naverMapUrl = 'https://naver.me/GOPeemGQ'

const modalOpen = ref(false)
const currentIndex = ref(0)
const openModal = (i) => { currentIndex.value = i; modalOpen.value = true }

onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible') })
  }, { threshold: 0.1 })
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el))
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Dancing+Script:wght@700&family=Gowun+Batang:wght@400;700&family=Playfair+Display:ital,wght@0,700;1,700&display=swap');

.disney-theme {
  font-family: 'Gowun Batang', serif;
  background: #fdfaf6;
  color: #2c3e50;
  min-height: 100vh;
  display: flex;
  justify-content: center;
}

.scroll-container {
  width: 100%;
  max-width: 500px;
  background: #fff;
  box-shadow: 0 0 50px rgba(0,0,0,0.05);
}

.reveal {
  opacity: 0;
  transform: translateY(30px);
  transition: all 1s ease-out;
}
.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Intro */
.intro-section {
  padding: 80px 20px;
  text-align: center;
  position: relative;
  overflow: hidden;
  background: linear-gradient(to bottom, #fdfbfb 0%, #ebedee 100%);
}

.sparkle-text {
  font-family: 'Dancing Script', cursive;
  font-size: 1.5rem;
  color: #d4af37;
  margin-bottom: 10px;
}

.main-title {
  font-family: 'Playfair Display', serif;
  font-size: 2.2rem;
  margin-bottom: 40px;
  letter-spacing: -1px;
}

.baby-portrait {
  position: relative;
  width: 100%;
  max-width: 320px;
  margin: 0 auto 40px;
}

.castle-outline {
  width: 100%;
  aspect-ratio: 1;
  border-radius: 50% 50% 0 0;
  overflow: hidden;
  border: 4px solid #fff;
  box-shadow: 0 10px 30px rgba(0,0,0,0.1);
}

.castle-img { width: 100%; height: 100%; object-fit: cover; opacity: 0.8; }

.baby-img {
  position: absolute;
  width: 70%;
  bottom: -20px;
  left: 50%;
  transform: translateX(-50%);
  filter: drop-shadow(0 15px 25px rgba(0,0,0,0.2));
  animation: float 4s infinite ease-in-out;
}

@keyframes float {
  0%, 100% { transform: translate(-50%, 0); }
  50% { transform: translate(-50%, -15px); }
}

.welcome-text {
  font-size: 1.1rem;
  color: #7f8c8d;
  margin-top: 20px;
}

/* Story */
.story-section {
  padding: 80px 40px;
  text-align: center;
  background: #fff;
}

.greeting {
  font-size: 1.2rem;
  line-height: 2.5;
  white-space: pre-line;
  color: #444;
}

.divider { margin-top: 30px; font-size: 1.5rem; color: #d4af37; }

/* Gallery */
.gallery-section { padding: 60px 20px; background: #fdfaf6; }
.section-title { text-align: center; margin-bottom: 40px; font-family: 'Playfair Display', serif; font-size: 1.5rem; }
.gallery-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 15px; }
.gallery-item { aspect-ratio: 1; background-size: cover; background-position: center; border-radius: 10px; border: 5px solid #fff; box-shadow: 0 4px 10px rgba(0,0,0,0.1); }

/* Info */
.info-section { padding: 80px 30px; }
.info-card { background: #fff; border: 1px solid #eee; border-radius: 20px; padding: 40px 30px; box-shadow: 0 10px 40px rgba(0,0,0,0.03); }
.info-row { margin-bottom: 30px; }
.label { font-size: 0.8rem; letter-spacing: 0.2em; color: #d4af37; margin-bottom: 5px; font-weight: bold; }
.value { font-size: 1.1rem; color: #333; }

.map-placeholder { height: 150px; background: #f9f9f9; border-radius: 15px; display: flex; align-items: center; justify-content: center; margin: 20px 0; color: #ccc; border: 1px dashed #ddd; }
.map-buttons { display: flex; gap: 10px; }
.btn { flex: 1; padding: 12px; border-radius: 30px; text-decoration: none; font-size: 0.9rem; text-align: center; font-weight: bold; }
.kakao { background: #fee500; color: #3c1e1e; }
.naver { background: #03c75a; color: #fff; }

.footer { padding: 80px 20px; text-align: center; background: #fff; border-top: 1px solid #f0f0f0; }
.signature { font-family: 'Dancing Script', cursive; font-size: 2rem; color: #d4af37; }

/* Modal */
.modal { position: fixed; top: 0; left: 0; width: 100%; height: 100vh; background: rgba(0,0,0,0.9); z-index: 1000; display: flex; align-items: center; justify-content: center; }
.modal-img { max-width: 90%; max-height: 80vh; border: 3px solid #fff; }
</style>
