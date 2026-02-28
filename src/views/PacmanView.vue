<template>
  <div class="pacman-concept-theme">
    <div class="arcade-cabinet">
      <!-- CRT Screen Effect Container -->
      <div class="crt-screen">
        <div class="scanlines"></div>
        <div class="screen-glow"></div>
        
        <!-- Game Intro Overlay -->
        <Transition name="game-start">
          <div v-if="gameStarted" class="game-content">
            <header class="game-header">
              <div class="p1-score">1UP<br/>{{ score.toLocaleString() }}</div>
              <div class="high-score">HIGH SCORE<br/>524,000</div>
              <div class="lives">
                <div class="life"></div><div class="life"></div>
              </div>
            </header>

            <div class="scroll-area">
              <!-- Maze Hero -->
              <section class="maze-hero reveal">
                <div class="maze-container">
                  <div class="maze-path">
                    <div class="dot-row"><span></span><span></span><span></span><span></span></div>
                    <div class="pac-hero"></div>
                  </div>
                  <h1 class="pixel-name">JI-AN</h1>
                  <div class="level-indicator">LEVEL 01</div>
                </div>
              </section>

              <!-- Story Level -->
              <section class="level-section reveal">
                <div class="level-banner">STAGE: GREETING</div>
                <div class="ghost-message">
                  <div class="ghost-icon red"></div>
                  <div class="pixel-bubble">{{ message }}</div>
                </div>
              </section>

              <!-- Gallery Level -->
              <section class="gallery-level reveal">
                <h2 class="pixel-h2">SELECT ITEM</h2>
                <div class="gallery-grid">
                  <div 
                    v-for="(photo, index) in photos" 
                    :key="index"
                    class="item-slot"
                    @click="openModal(index)"
                  >
                    <div class="photo-pixel" :style="{ backgroundImage: `url(${photo})` }"></div>
                    <div class="point-value">1000 PTS</div>
                  </div>
                </div>
              </section>

              <!-- Goal Section -->
              <section class="goal-section reveal">
                <div class="gate-sign">FRUITS OF JOY</div>
                <div class="info-block">
                  <div class="row"><span class="lbl">DATE:</span> {{ eventDate }}</div>
                  <div class="row"><span class="lbl">LOC:</span> {{ venueName }}</div>
                </div>
                <div class="maze-footer">
                  <div class="cherry-icon"></div>
                  <div class="nav-btns">
                    <a :href="kakaoMapUrl" target="_blank" class="pixel-btn blue">NAV_KAKAO</a>
                    <a :href="naverMapUrl" target="_blank" class="pixel-btn yellow">NAV_NAVER</a>
                  </div>
                </div>
              </section>
            </div>
          </div>
          
          <div v-else class="start-screen" @click="startGame">
            <div class="pacman-logo">JI-AN</div>
            <div class="game-info">1980 / 2026</div>
            <div class="insert-coin">CLICK TO START GAME</div>
            <div class="credit">CREDIT 01</div>
          </div>
        </Transition>
      </div>

      <div class="cabinet-base">
        <div class="joystick-flat">
          <div class="stick"></div>
          <div class="btn-group">
            <span class="btn red"></span>
            <span class="btn blue"></span>
          </div>
        </div>
      </div>
    </div>

    <!-- Retro Modal -->
    <Teleport to="body">
      <Transition name="pixel-fade">
        <div v-if="modalOpen" class="retro-modal" @click="modalOpen = false">
          <div class="modal-frame">
             <div class="frame-edge">PAUSE</div>
             <img :src="photos[currentIndex]" class="modal-img" />
             <div class="close-txt">PRESS ANY BUTTON TO RESUME</div>
          </div>
        </div>
      </Transition>
    </Teleport>
  </div>
</template>

<script setup>
import { getImg } from '../utils/imagePath'
import { ref, onMounted } from 'vue'

const gameStarted = ref(false)
const score = ref(0)
const message = ref(`WAKA WAKA!\n지안이의 첫 번째 스테이지가\n드디어 시작되었습니다!\n\n최종 보스(돌잡이)를 향한\n지안이의 여정에 함께해주시고\n많은 축하 포인트 부탁드려요!`)
const eventDate = ref('2026.03.07 18:00')
const venueName = ref('루엘 파티플레이스')
const photos = ref([getImg('/images/photo1.jpg'), getImg('/images/photo2.jpg'), getImg('/images/photo3.jpg'), getImg('/images/photo4.jpg')])
const kakaoMapUrl = 'https://map.kakao.com/link/to/236178717'
const naverMapUrl = 'https://naver.me/GOPeemGQ'

const modalOpen = ref(false)
const currentIndex = ref(0)
const openModal = (i) => { currentIndex.value = i; modalOpen.value = true }

const startGame = () => {
  gameStarted.value = true
  setInterval(() => { if(gameStarted.value) score.value += 10 }, 500)
}

onMounted(() => {
  const observer = new IntersectionObserver((entries) => {
    entries.forEach(e => { if (e.isIntersecting) e.target.classList.add('visible') })
  }, { threshold: 0.1 })
  
  // Need to wait for gameStarted to be true to observe elements inside it
  // For now, simpler reveal logic or just css animations
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

.pacman-concept-theme {
  background: #111;
  min-height: 100vh;
  display: flex;
  justify-content: center;
  align-items: center;
  font-family: 'Press Start 2P', cursive;
  color: #fff;
  text-transform: uppercase;
}

.arcade-cabinet {
  width: 100%;
  max-width: 500px;
  background: #333;
  border: 10px solid #222;
  border-radius: 20px;
  box-shadow: 0 50px 100px rgba(0,0,0,0.5);
  overflow: hidden;
}

.crt-screen {
  background: #000;
  height: 80vh;
  position: relative;
  border: 15px solid #1a1a1a;
  box-shadow: inset 0 0 50px rgba(30, 144, 255, 0.2);
}

.scanlines {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background: linear-gradient(rgba(18, 16, 16, 0) 50%, rgba(0, 0, 0, 0.1) 50%), linear-gradient(90deg, rgba(255, 0, 0, 0.03), rgba(0, 255, 0, 0.01), rgba(0, 0, 255, 0.03));
  background-size: 100% 4px, 3px 100%;
  pointer-events: none;
  z-index: 100;
}

.screen-glow {
  position: absolute;
  top: 0; left: 0; width: 100%; height: 100%;
  background: radial-gradient(circle, rgba(30,144,255,0.05) 0%, transparent 80%);
  pointer-events: none;
}

/* Start Screen */
.start-screen {
  height: 100%;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  text-align: center;
  cursor: pointer;
}

.pacman-logo { font-size: 3rem; color: #ffff00; text-shadow: 5px 5px #ff0000; margin-bottom: 20px; }
.game-info { font-size: 0.6rem; color: #ffb8ff; margin-bottom: 60px; }
.insert-coin { font-size: 0.8rem; color: #ffff00; animation: blink 0.8s infinite steps(2); }
.credit { position: absolute; bottom: 30px; font-size: 0.6rem; color: #fff; }

@keyframes blink { 0% { opacity: 1; } 100% { opacity: 0; } }

/* Game Content */
.game-content { height: 100%; display: flex; flex-direction: column; }

.game-header {
  padding: 20px;
  display: flex;
  justify-content: space-between;
  font-size: 0.5rem;
  color: #ff0000;
  border-bottom: 2px solid #1e90ff;
}

.lives { display: flex; gap: 10px; margin-top: 10px; }
.life { width: 15px; height: 15px; background: #ffff00; border-radius: 50%; clip-path: polygon(100% 20%, 50% 50%, 100% 80%, 100% 100%, 0 100%, 0 0, 100% 0); }

.scroll-area { 
  flex: 1; 
  overflow-y: auto; 
  padding: 20px;
}

.maze-hero { margin-bottom: 60px; }
.maze-container {
  border: 4px solid #1e90ff;
  padding: 40px 20px;
  position: relative;
}

.maze-path {
  height: 40px;
  background: repeating-linear-gradient(90deg, #fff 0, #fff 5px, transparent 5px, transparent 20px);
  position: relative;
  margin-bottom: 30px;
}

.pac-hero {
  position: absolute;
  left: 0; top: 0; width: 40px; height: 40px;
  background: #ffff00; border-radius: 50%;
  clip-path: polygon(100% 20%, 50% 50%, 100% 80%, 100% 100%, 0 100%, 0 0, 100% 0);
  animation: movePac 10s infinite linear, chompPac 0.3s infinite linear;
}

@keyframes movePac { 0% { left: 0%; } 100% { left: 90%; } }
@keyframes chompPac { 
  0% { clip-path: polygon(100% 20%, 50% 50%, 100% 80%, 100% 100%, 0 100%, 0 0, 100% 0); }
  50% { clip-path: polygon(100% 50%, 100% 50%, 50% 50%, 100% 50%, 100% 50%, 0 100%, 0 0); }
}

.pixel-name { font-size: 2.2rem; color: #ffff00; margin-bottom: 10px; }
.level-indicator { font-size: 0.6rem; color: #ffb852; }

/* Level Message */
.level-banner { background: #1e90ff; color: #fff; padding: 10px; font-size: 0.6rem; margin-bottom: 30px; }
.ghost-message { display: flex; gap: 20px; align-items: center; }
.ghost-icon { width: 40px; height: 40px; border-radius: 20px 20px 0 0; position: relative; flex-shrink: 0; }
.ghost-icon::after { content: '👀'; position: absolute; top: 8px; left: 8px; font-size: 14px; }
.red { background: #ff0000; box-shadow: 0 0 15px rgba(255,0,0,0.5); }
.pixel-bubble { font-size: 0.55rem; line-height: 2; color: #fff; text-align: left; }

/* Gallery */
.gallery-level { margin-top: 80px; }
.pixel-h2 { font-size: 0.8rem; color: #00ffff; margin-bottom: 30px; }
.gallery-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 20px; }
.item-slot { border: 2px solid #fff; padding: 10px; text-align: center; }
.photo-pixel { aspect-ratio: 1; background-size: cover; background-position: center; border: 2px solid #1e90ff; margin-bottom: 10px; }
.point-value { font-size: 0.4rem; color: #ffff00; }

/* Goal */
.goal-section { margin-top: 80px; border: 3px solid #ffff00; padding: 30px 10px; background: rgba(255,255,0,0.05); }
.gate-sign { color: #ff0000; font-size: 0.6rem; margin-bottom: 30px; }
.info-block { font-size: 0.6rem; line-height: 2; margin-bottom: 40px; text-align: left; padding: 0 10px;}
.lbl { color: #1e90ff; }

.nav-btns { display: flex; flex-direction: column; gap: 15px; margin-top: 30px; }
.pixel-btn { padding: 15px; text-decoration: none; font-size: 0.55rem; border: 3px solid #fff; text-align: center; color: #fff; }
.blue { background: #1e90ff; }
.yellow { background: #ffb852; color: #000; }

/* Cabinet Bottom */
.cabinet-base {
  background: #222;
  height: 100px;
  display: flex;
  justify-content: center;
  align-items: center;
  border-top: 5px solid #111;
}

.joystick-flat {
  display: flex;
  align-items: center;
  gap: 40px;
}

.stick {
  width: 40px; height: 40px; background: #000; border-radius: 50%;
  position: relative; border: 4px solid #444;
}
.stick::after {
  content: ''; position: absolute; top: 10px; left: 10px; width: 20px; height: 20px; background: #ff0000; border-radius: 50%;
}

.btn-group { display: flex; gap: 15px; }
.btn { width: 30px; height: 30px; border-radius: 50%; border: 3px solid #444; }
.btn.red { background: #ff0000; }
.btn.blue { background: #1e90ff; }

/* Modal */
.retro-modal { position: fixed; top: 0; left: 0; width: 100%; height: 100vh; background: rgba(0,0,0,0.9); z-index: 2000; display: flex; align-items: center; justify-content: center; padding: 20px; }
.modal-frame { border: 4px solid #ff0000; padding: 20px; background: #000; width: 100%; max-width: 400px; text-align: center; }
.frame-edge { font-size: 0.8rem; color: #ff0000; margin-bottom: 20px; }
.modal-img { width: 100%; border: 2px solid #fff; margin-bottom: 20px; }
.close-txt { font-size: 0.5rem; color: #ffff00; animation: blink 0.5s infinite steps(2); }

/* Transitions */
.game-start-enter-active, .game-start-leave-active { transition: all 1s steps(5); }
.game-start-enter-from, .game-start-leave-to { opacity: 0; transform: scale(0.5); }
</style>
