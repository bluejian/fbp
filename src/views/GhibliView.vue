<template>
  <div class="ghibli-brand-theme">
    <div class="scroll-container">
      <!-- Authentic Totoro Bus Stop Header -->
      <header class="ghibli-hero">
        <div class="watercolor-canvas" :style="{ backgroundImage: `url('/images/ghibli-brand-bg.png')` }">
          <div class="rain-overlay"></div>
          <div class="fog-overlay"></div>
        </div>
        <div class="hero-content reveal">
          <h1 class="ghibli-brand-title">JI-AN</h1>
          <div class="japanese-sub">となりの ジ안 이</div>
          <div class="spirit-frame">
            <img src="/images/baby-cutout.png" alt="Jian" class="baby-spirit" />
            <div class="leaf-umbrella">🍃</div>
          </div>
          <div class="event-brief">
            <p class="hand-cursive">{{ eventDate }}</p>
            <p class="location-ink">{{ venueName }}</p>
          </div>
        </div>
      </header>

      <!-- Ink Brush Message Area -->
      <section class="message-section reveal">
        <div class="ink-box">
          <div class="susuwatari">● ○ ●</div>
          <p class="greeting-text">{{ message }}</p>
          <div class="stamp-seal">지안</div>
        </div>
      </section>

      <!-- Watercolor Gallery -->
      <section class="gallery-section reveal">
        <h2 class="ghibli-sec-title">소중한 일상 조각들</h2>
        <div class="gallery-grid">
          <div 
            v-for="(photo, index) in photos" 
            :key="index"
            class="watercolor-frame"
            @click="openModal(index)"
          >
            <div class="photo-inner" :style="{ backgroundImage: `url(${photo})` }"></div>
            <div class="deckle-edge"></div>
          </div>
        </div>
      </section>

      <!-- Forest Path Info -->
      <section class="info-section">
        <div class="path-container reveal">
          <div class="station-sign">
            <span class="station-name">RUELLE BUS STOP</span>
            <span class="next-stat">→ HAPPINESS</span>
          </div>
          <div class="info-details">
            <div class="info-row">
              <span class="icon">📅</span>
              <div class="val">{{ eventDate }}</div>
            </div>
            <div class="info-row">
              <span class="icon">📍</span>
              <div class="val">{{ venueName }}</div>
            </div>
          </div>
          
          <div class="bus-buttons">
            <a :href="kakaoMapUrl" target="_blank" class="ghibli-ink-btn">KAKAOMAP</a>
            <a :href="naverMapUrl" target="_blank" class="ghibli-ink-btn">NAVERMAP</a>
          </div>
        </div>
      </section>

      <footer class="ghibli-footer">
        <div class="ghibli-logo">STUDIO GHIBLI</div>
        <p>A Night in the Forest with JIAN</p>
      </footer>
    </div>

    <!-- Modal -->
    <Teleport to="body">
      <Transition name="fade">
        <div v-if="modalOpen" class="modal-overlay" @click="closeModal">
          <img :src="photos[currentIndex]" class="modal-img" @click.stop />
          <div class="modal-close" @click="closeModal">✕</div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'

const message = ref(`어느 무성한 숲 속,\n작은 요정 지안이가 찾아온 지 일 년.\n\n바람이 전하는 따뜻한 초대장에 실어\n여러분을 행복의 숲으로 부릅니다.\n소중한 걸음을 함께해 주세요.`)
const eventDate = ref('2026. 03. 07')
const venueName = ref('루엘 파티플레이스')
const photos = ref(['/images/photo1.jpg', '/images/photo2.jpg', '/images/photo3.jpg', '/images/photo4.jpg'])
const kakaoMapUrl = 'https://map.kakao.com/link/to/236178717'
const naverMapUrl = 'https://naver.me/GOPeemGQ'

const modalOpen = ref(false)
const currentIndex = ref(0)
const openModal = (i) => { currentIndex.value = i; modalOpen.value = true }
const closeModal = () => { modalOpen.value = false }

onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible') })
  }, { threshold: 0.1 })
  document.querySelectorAll('.reveal').forEach(el => observer.observe(el))
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Myeongjo:wght@400;800&family=Nanum+Pen+Script&family=Noto+Serif+JP:wght@700&display=swap');

.ghibli-brand-theme {
  background: #2d3e40;
  color: #3e4c33;
  min-height: 100vh;
  display: flex;
  justify-content: center;
}

.scroll-container {
  width: 100%;
  max-width: 500px;
  background: #fdfaf3; /* Aged Paper */
  position: relative;
  overflow-x: hidden;
}

.reveal {
  opacity: 0;
  transform: translateY(20px);
  transition: all 1.5s cubic-bezier(0.19, 1, 0.22, 1);
}
.visible {
  opacity: 1;
  transform: translateY(0);
}

/* Hero */
.ghibli-hero {
  height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: flex-end;
  align-items: center;
  text-align: center;
  padding-bottom: 60px;
}

.watercolor-canvas {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background-size: cover;
  background-position: center;
  z-index: 1;
}

.hero-content { position: relative; z-index: 10; padding: 0 40px; }

.ghibli-brand-title {
  font-family: 'Noto Serif JP', serif;
  font-size: 3rem;
  color: #1a2a20;
  margin-bottom: 0px;
  letter-spacing: 5px;
}

.japanese-sub {
  font-family: 'Nanum Pen Script', cursive;
  font-size: 1.5rem;
  color: #5d7c4b;
  margin-bottom: 40px;
}

.spirit-frame {
  position: relative;
  width: 200px;
  height: 200px;
  margin: 0 auto 30px;
}

.baby-spirit {
  position: absolute;
  width: 75%;
  bottom: 0px;
  left: 50%;
  transform: translateX(-50%);
  filter: sepia(0.2) contrast(1.1);
  animation: spiritFloat 4s infinite ease-in-out;
}

.leaf-umbrella {
  position: absolute;
  top: 10px; right: 20px;
  font-size: 2.5rem;
  transform: rotate(15deg);
  animation: sway 3s infinite ease-in-out;
}

@keyframes spiritFloat {
  0%, 100% { transform: translate(-50%, 0); }
  50% { transform: translate(-50%, -8px); }
}

@keyframes sway {
  0%, 100% { transform: rotate(15deg); }
  50% { transform: rotate(25deg); }
}

.hand-cursive { font-family: 'Nanum Pen Script', cursive; font-size: 1.8rem; color: #4a5d3f; margin-bottom: 5px; }

/* Inker Box */
.message-section { padding: 100px 40px; }
.ink-box { border: 1px solid #dcd7c9; padding: 50px 30px; position: relative; text-align: center; background: #fffcf5; }
.susuwatari { font-size: 1rem; color: #333; margin-bottom: 30px; opacity: 0.6; }
.greeting-text { font-family: 'Nanum Myeongjo', serif; font-size: 1.1rem; line-height: 2.4; color: #4a5d3f; white-space: pre-line; }
.stamp-seal { position: absolute; bottom: 20px; right: 20px; border: 2px solid #b23a3a; color: #b23a3a; padding: 5px 10px; font-weight: 800; font-size: 0.8rem; transform: rotate(-5deg); opacity: 0.7; }

/* Gallery */
.gallery-section { padding: 60px 20px; background: #e9f5db; }
.ghibli-sec-title { font-family: 'Nanum Pen Script', cursive; text-align: center; font-size: 2.2rem; color: #5d7c4b; margin-bottom: 50px; }
.gallery-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }
.watercolor-frame { background: #fff; padding: 8px; box-shadow: 0 4px 10px rgba(0,0,0,0.05); cursor: pointer; position: relative; }
.photo-inner { aspect-ratio: 1; background-size: cover; background-position: center; border: 1px solid #f0f0f0; }

/* Path sign */
.info-section { padding: 100px 30px; }
.path-container { text-align: left; }
.station-sign { border: 2px solid #5d7c4b; border-radius: 40px; padding: 20px; text-align: center; margin-bottom: 50px; background: #fff; }
.station-name { display: block; font-family: 'Noto Serif JP', serif; font-size: 1.2rem; border-bottom: 1px solid #eee; padding-bottom: 10px; margin-bottom: 5px; }
.next-stat { font-family: 'Nanum Pen Script', cursive; font-size: 1.2rem; color: #a3b18a; }

.info-row { display: flex; align-items: center; margin-bottom: 25px; font-family: 'Nanum Myeongjo', serif; }
.icon { font-size: 1.2rem; margin-right: 15px; }
.val { font-size: 1.1rem; font-weight: 800; }

.bus-buttons { display: flex; gap: 10px; margin-top: 50px; }
.ghibli-ink-btn { flex: 1; padding: 15px; border: 1px solid #5d7c4b; color: #5d7c4b; text-decoration: none; font-size: 0.9rem; font-weight: 800; text-align: center; }

.ghibli-footer { padding: 100px 40px; text-align: center; border-top: 1px solid #e0e0e0; background: #fff; }
.ghibli-logo { font-family: 'Noto Serif JP', serif; letter-spacing: 5px; color: #333; margin-bottom: 10px; font-size: 0.9rem; }

/* Modal */
.modal-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100vh; background: #fdfaf3; display: flex; align-items: center; justify-content: center; z-index: 1000; }
.modal-img { max-width: 90%; max-height: 80vh; border: 1px solid #dcd7c9; box-shadow: 0 20px 50px rgba(0,0,0,0.1); }
.modal-close { position: absolute; top: 30px; right: 30px; font-size: 2rem; cursor: pointer; }
</style>
