<template>
  <div class="pixar-brand-theme">
    <div class="scroll-container">
      <!-- Authentic Toy Story Room Intro -->
      <header class="pixar-hero" :style="{ backgroundImage: `url(getImg('/images/pixar-brand-bg.png'))` }">
        <div class="room-overlay"></div>
        <div class="hero-content reveal">
          <div class="pixar-intro">Disney • Pixar</div>
          <div class="bouncy-logo">
            <h1 class="pixar-font">
              <span class="l">J</span><span class="l">I</span><span class="l">A</span><span class="l">N</span>
            </h1>
          </div>
          <div class="sub-logo">BIRTHDAY STORY</div>
          
          <div class="baby-toy-frame">
            <div class="luxo-ball"></div>
            <img :src="getImg('/images/baby-cutout.png')" alt="Jian" class="baby-cutout" />
          </div>

          <div class="mission-brief">
            <p>{{ eventDate }}</p>
            <p>{{ venueName }}</p>
          </div>
        </div>
      </header>

      <!-- Talk Bubble Section -->
      <section class="message-section reveal">
        <div class="talk-bubble">
          <div class="bubble-content">
            <p>{{ message }}</p>
          </div>
          <div class="bubble-tail"></div>
        </div>
      </section>

      <!-- Scrapbook Gallery -->
      <section class="gallery-section reveal">
        <h2 class="pixar-sec-title">The Adventure Log</h2>
        <div class="gallery-grid">
          <div 
            v-for="(photo, index) in photos" 
            :key="index"
            class="photo-stick"
            @click="openModal(index)"
          >
            <div class="tape top"></div>
            <div class="img-box" :style="{ backgroundImage: `url(${photo})` }"></div>
          </div>
        </div>
      </section>

      <!-- Mission Control Info -->
      <section class="info-section reveal">
        <div class="control-board">
          <div class="monitor">
            <div class="screen">
              <div class="lcd-text">MISSION: CELEBRATE</div>
              <div class="data-row">
                <span class="key">DATE:</span>
                <span class="val">{{ eventDate }}</span>
              </div>
              <div class="data-row">
                <span class="key">BASE:</span>
                <span class="val">{{ venueName }}</span>
              </div>
            </div>
          </div>
          
          <div class="action-buttons">
            <a :href="kakaoMapUrl" target="_blank" class="pixar-btn yellow">NAV: KAKAO</a>
            <a :href="naverMapUrl" target="_blank" class="pixar-btn green">NAV: NAVER</a>
          </div>
        </div>
      </section>

      <footer class="pixar-footer">
        <div class="pixar-signature">PIXAR</div>
        <p>Animation Studios</p>
      </footer>
    </div>

    <!-- Modal -->
    <Teleport to="body">
      <Transition name="fade">
        <div v-if="modalOpen" class="modal-overlay" @click="closeModal">
          <img :src="photos[currentIndex]" class="modal-img" @click.stop />
          <div class="modal-close" @click="closeModal">DONE</div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script setup>
import { getImg } from '../utils/imagePath'
import { ref, onMounted } from 'vue'

const message = ref(`To Infinity and Beyond!\nOur favorite little adventurer\nis turning ONE today.\n\nYou're invited to join Jian's\nvery first birthday story!`)
const eventDate = ref('MARCH 07, 2026')
const venueName = ref('RUELLE PARTY PLACE')
const photos = ref([getImg('/images/photo1.jpg'), getImg('/images/photo2.jpg'), getImg('/images/photo3.jpg'), getImg('/images/photo4.jpg')])
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
@import url('https://fonts.googleapis.com/css2?family=Luckiest+Guy&family=Titan+One&family=Montserrat:wght@800&display=swap');

.pixar-brand-theme {
  background: #f0f0f0;
  color: #333;
  min-height: 100vh;
  display: flex;
  justify-content: center;
}

.scroll-container {
  width: 100%;
  max-width: 500px;
  background: #fff;
  position: relative;
  overflow-x: hidden;
}

.reveal {
  opacity: 0;
  transform: scale(0.9);
  transition: all 0.8s cubic-bezier(0.175, 0.885, 0.32, 1.275);
}
.visible {
  opacity: 1;
  transform: scale(1);
}

/* Hero */
.pixar-hero {
  height: 100vh;
  max-height: 800px;
  background-size: cover;
  background-position: center;
  position: relative;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
}

.room-overlay {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background: linear-gradient(to bottom, rgba(255,255,255,0.2) 0%, rgba(255,255,255,0.8) 100%);
}

.hero-content { position: relative; z-index: 10; padding: 0 40px; }

.pixar-intro {
  font-family: 'Montserrat', sans-serif;
  font-size: 0.8rem;
  font-weight: 800;
  color: #1e90ff;
  text-transform: uppercase;
  margin-bottom: 20px;
}

.pixar-font {
  font-family: 'Titan One', cursive;
  font-size: 5rem;
  color: #ffcc00;
  -webkit-text-stroke: 4px #005bb7;
  letter-spacing: 5px;
  margin: 0;
}

.l { display: inline-block; animation: bounceHero 2s infinite ease-in-out; }
.l:nth-child(2) { animation-delay: 0.1s; }
.l:nth-child(3) { animation-delay: 0.2s; }
.l:nth-child(4) { animation-delay: 0.3s; }

@keyframes bounceHero {
  0%, 100% { transform: translateY(0); }
  50% { transform: translateY(-15px); }
}

.sub-logo {
  font-family: 'Luckiest Guy', cursive;
  font-size: 1.5rem;
  color: #ff3333;
  letter-spacing: 2px;
  margin-top: -10px;
}

.baby-toy-frame {
  margin-top: 50px;
  position: relative;
  width: 200px;
  height: 200px;
}

.luxo-ball {
  width: 100%;
  height: 100%;
  background: radial-gradient(circle at 30% 30%, #ffcc00, #ff9900);
  border-radius: 50%;
  border: 4px solid #005bb7;
  position: relative;
}
.luxo-ball::after {
  content: '★';
  position: absolute;
  top: 50%; left: 50%;
  transform: translate(-50%, -50%);
  font-size: 4rem;
  color: #ff3333;
}

.baby-cutout {
  position: absolute;
  width: 70%;
  bottom: 0px;
  left: 50%;
  transform: translateX(-50%);
  filter: drop-shadow(0 10px 10px rgba(0,0,0,0.2));
}

.mission-brief {
  font-family: 'Luckiest Guy', cursive;
  margin-top: 30px;
  font-size: 1.1rem;
  color: #444;
}

/* Section Message */
.message-section { padding: 80px 40px; }
.talk-bubble {
  background: #fff;
  border: 5px solid #333;
  border-radius: 40px;
  padding: 40px;
  position: relative;
  text-align: center;
  box-shadow: 10px 10px 0 rgba(0,0,0,0.05);
}
.bubble-content p { font-family: 'Luckiest Guy', cursive; font-size: 1.25rem; line-height: 1.8; color: #1e90ff; white-space: pre-line; margin: 0; }

/* Gallery */
.gallery-section { padding: 60px 20px; background: #50aeff; }
.pixar-sec-title { font-family: 'Titan One', cursive; text-align: center; color: #fff; font-size: 1.5rem; margin-bottom: 50px; -webkit-text-stroke: 1px #005bb7; }
.gallery-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }
.photo-stick { background: #fff; border: 4px solid #333; padding: 10px; position: relative; cursor: pointer; }
.img-box { aspect-ratio: 1; background-size: cover; background-position: center; }
.tape { position: absolute; width: 60px; height: 25px; background: rgba(255,204,0,0.7); top: -10px; left: 50%; transform: translateX(-50%) rotate(-2deg); }

/* Control Board */
.info-section { padding: 100px 30px; }
.control-board { background: #333; border-radius: 40px; padding: 40px; border: 8px solid #555; box-shadow: 0 10px 30px rgba(0,0,0,0.3); }
.monitor { background: #111; border: 15px solid #222; border-radius: 20px; padding: 20px; }
.lcd-text { font-family: 'Montserrat', sans-serif; font-weight: 800; color: #2db400; font-size: 0.8rem; margin-bottom: 20px; }
.data-row { margin-bottom: 10px; font-family: 'Luckiest Guy', cursive; font-size: 1.1rem; }
.key { color: #50aeff; margin-right: 10px; }
.val { color: #fff; }

.action-buttons { display: flex; flex-direction: column; gap: 15px; margin-top: 40px; }
.pixar-btn { padding: 15px; border-radius: 50px; text-decoration: none; font-family: 'Titan One', cursive; text-align: center; border: 4px solid #333; }
.yellow { background: #ffcc00; color: #333; }
.green { background: #03c75a; color: #fff; }

.pixar-footer { padding: 80px 40px; text-align: center; background: #fff; }
.pixar-signature { font-family: 'Montserrat', sans-serif; font-weight: 800; font-size: 2.5rem; color: #333; letter-spacing: 5px; }

/* Modal */
.modal-overlay { position: fixed; top: 0; left: 0; width: 100%; height: 100vh; background: #50aeff; display: flex; align-items: center; justify-content: center; z-index: 1000; }
.modal-img { max-width: 90%; max-height: 70vh; border: 8px solid #fff; border-radius: 30px; }
.modal-close { margin-top: 30px; font-family: 'Titan One', cursive; color: #fff; cursor: pointer; font-size: 1.5rem; }
</style>
