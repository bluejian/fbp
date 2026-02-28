<template>
  <div class="mario-neople-theme" ref="mainContainer">
    <!-- Modern BGM Controller -->
    <div class="bgm-bar" :class="{ active: bgmPlaying }" @click="toggleBgm">
      <div class="bgm-icon">
        <svg v-if="bgmPlaying" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18">
          <path d="M12 3v10.55c-.59-.34-1.27-.55-2-.55C7.79 13 6 14.79 6 17s1.79 4 4 4 4-1.79 4-4V7h4V3h-6z"/>
        </svg>
        <svg v-else xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill="currentColor" width="18" height="18">
          <path d="M4.34 2.93L2.93 4.34 7.29 8.7 7 9H3v6h4l5 5v-6.59l4.18 4.18c-.65.49-1.38.88-2.18 1.11v2.06c1.34-.3 2.57-.97 3.56-1.88l2.1 2.1 1.41-1.41L4.34 2.93zM19 12c0 .82-.15 1.61-.41 2.34l1.53 1.53c.56-1.17.88-2.48.88-3.87 0-4.28-2.99-7.86-7-8.77v2.06c2.89.86 5 3.54 5 6.71zm-7-8l-1.88 1.88L12 7.76zm4.5 8c0-1.77-1.02-3.29-2.5-4.03v1.79l2.48 2.48c.01-.08.02-.16.02-.24z"/>
        </svg>
      </div>
      <div class="bgm-eq" v-if="bgmPlaying">
        <span></span><span></span><span></span><span></span>
      </div>
      <div class="bgm-label">{{ bgmPlaying ? 'Super Mario Bros.' : 'TAP TO PLAY' }}</div>
      <audio ref="bgmAudio" loop>
        <source src="/audio/spmario.mp4" type="audio/mpeg">
      </audio>
    </div>

    <!-- Scrolling World -->
    <div class="level-wrapper">
      
      <!-- Scene 1: Intro (World 1-1) -->
      <section class="scene intro-scene" id="scene1">
        <div class="sticky-content">
          <div class="sky-bg"></div>
          <div class="parallax-hills" :style="{ transform: `translateX(${-scrollProgress1 * 30}%)` }"></div>
          
          <div class="ui-overlay">
            <div class="game-info">
              <span>MARIO</span><br/><span>{{ score.toString().padStart(6, '0') }}</span>
            </div>
            <div class="world-info">
              <span>WORLD</span><br/><span>1-1</span>
            </div>
          </div>

          <div class="greeting-message" :style="{ opacity: 1 - scrollProgress1 * 2 }">
            <h1 class="pixel-title">JI-AN'S 1ST<br/>birthday</h1>
            <p class="pixel-sub">PRESS SCROLL TO START</p>
          </div>

          <!-- Scene 1 Bricks -->
          <div class="pixel-elements" :style="{ transform: `translateX(${-scrollProgress1 * 120}%)` }">
             <div class="brick-row" style="left: 400px; bottom: 200px;">
                <div class="brick"></div><div class="q-block" @click="jumpMario"></div><div class="brick"></div>
             </div>
             <div class="pipe" style="left: 800px; bottom: 60px;"></div>
          </div>
        </div>
      </section>

      <!-- Scene 2: Gallery (Underground?) -->
      <section class="scene gallery-scene" id="scene2">
        <div class="sticky-content dark-bg">
          <div class="underground-bg"></div>
          <div class="scene-title">LEVEL: THE GALLERY</div>
          
          <div class="photo-conveyor" :style="{ transform: `translateX(${100 - scrollProgress2 * 200}%)` }">
            <div 
              v-for="(photo, index) in photos" 
              :key="index" 
              class="photo-brick"
              @click="openModal(index)"
            >
              <img :src="photo" alt="Jian" />
              <div class="brick-frame"></div>
            </div>
          </div>
        </div>
      </section>

      <!-- Scene 3: The Big Party (Castle) -->
      <section class="scene party-scene" id="scene3">
        <div class="sticky-content castle-bg">
          <div class="fireworks-container" v-if="hitFinal">
             <div class="firework red"></div><div class="firework blue"></div>
          </div>

          <div class="final-elements" :style="{ transform: `translateX(${50 - scrollProgress3 * 100}%)` }">
             <div class="q-block big-q" :class="{ 'hit-anim': hitFinal }" style="left: 200px; bottom: 300px;"></div>
             <div class="castle-gate" style="left: 500px; bottom: 60px;"></div>
          </div>

          <Transition name="pixel-pop">
            <div v-if="hitFinal" class="party-info-card">
              <div class="card-inner">
                <div class="card-title">YOU CLEARED THE STAGE!</div>
                <div class="details">
                  <p><strong>DATE:</strong> {{ eventDate }}</p>
                  <p><strong>LOC:</strong> {{ venueName }}</p>
                </div>
                <div class="btn-group">
                  <a :href="kakaoMapUrl" target="_blank" class="pixel-btn blue">MAP_KAKAO</a>
                  <a :href="naverMapUrl" target="_blank" class="pixel-btn green">MAP_NAVER</a>
                </div>
              </div>
            </div>
          </Transition>
        </div>
      </section>
    </div>

    <!-- The Hero: Jian-Mario (Fixed Position) -->
    <div class="fixed-mario-wrapper" :class="{ 'mario-walk': isWalking, 'mario-jump': isJumping }">
      <div class="jian-mario" :style="{ transform: `translateX(${marioX}px) translateY(${-marioY}px)` }">
        <div class="mario-costume">
          <img src="/images/mario-outfit-2.png" alt="outfit" />
          <div class="face-circle pixel-blend">
            <img src="/images/baby-cutout.png" alt="face" />
          </div>
        </div>
      </div>
    </div>

    <!-- Modal -->
    <div v-if="modalOpen" class="retro-modal" @click="modalOpen = false">
      <div class="modal-box">
        <img :src="photos[currentIndex]" />
        <div class="close-txt">TAP TO CLOSE</div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from 'vue'

const score = ref(120307)
const message = ref(`지안마리오의 첫 번째 모험!\n드디어 최종 성에 도착했습니다.`)
const eventDate = ref('2026.03.07 18:00')
const venueName = ref('루엘 파티플레이스')
const photos = ref(['/images/photo1.jpg', '/images/photo2.jpg', '/images/photo3.jpg', '/images/photo4.jpg'])
const kakaoMapUrl = 'https://map.kakao.com/link/to/236178717'
const naverMapUrl = 'https://naver.me/GOPeemGQ'

// Scroll State
const scrollProgress1 = ref(0)
const scrollProgress2 = ref(0)
const scrollProgress3 = ref(0)

// Mario State
const marioX = ref(0)
const marioY = ref(0)
const isWalking = ref(false)
const isJumping = ref(false)
const hitFinal = ref(false)

const bgmPlaying = ref(false)
const bgmAudio = ref(null)
const modalOpen = ref(false)
const currentIndex = ref(0)

const openModal = (i) => { currentIndex.value = i; modalOpen.value = true }

const toggleBgm = () => {
  if (bgmPlaying.value) bgmAudio.value.pause()
  else bgmAudio.value.play().catch(() => {})
  bgmPlaying.value = !bgmPlaying.value
}

const handleScroll = () => {
  const scrollY = window.scrollY
  const vh = window.innerHeight
  
  // Section 1 Progress (vh * 3 length)
  scrollProgress1.value = Math.min(Math.max(scrollY / (vh * 2), 0), 1)
  
  // Section 2 Progress
  const s2Start = vh * 3
  scrollProgress2.value = Math.min(Math.max((scrollY - s2Start) / (vh * 2), 0), 1)

  // Section 3 Progress
  const s3Start = vh * 6
  scrollProgress3.value = Math.min(Math.max((scrollY - s3Start) / (vh * 2), 0), 1)

  // Side-scrolling Logic for Mario Position X
  // We want him to walk across the screen in each section
  if (scrollProgress1.value > 0 && scrollProgress1.value < 1) {
     marioX.value = (scrollProgress1.value * 200) - 100 // Move from left to right
  } else if (scrollProgress2.value > 0 && scrollProgress2.value < 1) {
     marioX.value = (scrollProgress2.value * 200) - 100
  } else if (scrollProgress3.value > 0 && scrollProgress3.value < 1) {
     marioX.value = (scrollProgress3.value * 200) - 100
  } else {
     marioX.value = 0
  }

  // Animation Toggle
  isWalking.value = true
  clearTimeout(window.walkTimeout)
  window.walkTimeout = setTimeout(() => { isWalking.value = false }, 100)

  // Final Reveal Trigger
  if (scrollProgress3.value > 0.8 && !hitFinal.value) {
    jumpMario()
    hitFinal.value = true
  }
}

const jumpMario = () => {
  if (isJumping.value) return
  isJumping.value = true
  marioY.value = 100
  setTimeout(() => {
    marioY.value = 0
    isJumping.value = false
  }, 400)
}

onMounted(() => {
  window.addEventListener('scroll', handleScroll)
})

onUnmounted(() => {
  window.removeEventListener('scroll', handleScroll)
})
</script>

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

.mario-neople-theme {
  background: #000;
  font-family: 'Press Start 2P', cursive;
  color: #fff;
  text-transform: uppercase;
}

.level-wrapper {
  position: relative;
}

.scene {
  height: 300vh; /* Long section for scroll progress */
  position: relative;
}

.sticky-content {
  position: sticky;
  top: 0;
  height: 100vh;
  width: 100%;
  overflow: hidden;
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
}

/* Backgrounds */
.sky-bg { background: #5c94fc; position: absolute; inset: 0; }
.parallax-hills {
  position: absolute; bottom: 0; left: 0; width: 300%; height: 200px;
  background-image: url('/images/mario-bg.png');
  background-size: contain; background-repeat: repeat-x;
  opacity: 0.6;
}

.dark-bg { background: #000; }
.castle-bg { background: #1a1a1a; }

/* UI Overlay */
.ui-overlay {
  position: absolute; top: 40px; width: 100%;
  display: flex; justify-content: space-between; padding: 0 40px;
  font-size: 0.7rem; line-height: 1.5; color: #fff;
}

.greeting-message { text-align: center; z-index: 10; padding: 0 20px; }
.pixel-title { font-size: 2.2rem; margin-bottom: 20px; text-shadow: 4px 4px #ff0000; }
.pixel-sub { font-size: 0.7rem; color: #ffff00; }

/* Fixed Mario */
.fixed-mario-wrapper {
  position: fixed;
  top: 0; left: 0; width: 100%; height: 100vh;
  pointer-events: none;
  display: flex; justify-content: center; align-items: flex-end;
  padding-bottom: 80px;
  z-index: 1000;
}

.jian-mario {
  width: 100px; height: 120px;
  transition: transform 0.1s linear;
}

.mario-costume { position: relative; width: 100%; height: 100%; }
.mario-costume img { width: 100%; height: 100%; object-fit: contain; image-rendering: pixelated; position: relative; z-index: 10; }
.face-circle {
  position: absolute; 
  top: 15px; 
  left: 55%; 
  transform: translateX(-50%);
  width: 44px; 
  height: 44px; 
  background: #fff; 
  border-radius: 50%; 
  overflow: hidden; 
  border: none;
  z-index: 5; /* Place face BEHIND the hollow sprite if possible, or as a tight fit */
  display: flex;
  align-items: center;
  justify-content: center;
}
.pixel-blend img { 
  width: 140%; /* Zoom in on face */
  height: 140%;
  object-fit: cover; 
  border-radius: 50%;
  /* High-quality cutout effect using mask */
  -webkit-mask-image: radial-gradient(circle, black 60%, transparent 75%);
  mask-image: radial-gradient(circle, black 60%, transparent 75%);
  filter: contrast(1.1) brightness(1.1);
  image-rendering: crisp-edges;
}

.mario-walk { animation: walkSwing 0.2s infinite steps(2); }
@keyframes walkSwing { 0% { transform: scaleX(1); } 50% { transform: scaleX(0.9) skewY(2deg); } 100% { transform: scaleX(1); } }

/* Elements */
.pixel-elements { position: absolute; bottom: 60px; left: 0; width: 300%; display: flex; align-items: flex-end; }
.brick-row { display: flex; gap: 0; position: absolute; }
.brick { width: 40px; height: 40px; background: #944200; border: 3px solid #000; }
.q-block { width: 40px; height: 40px; background: #ff9441; border: 3px solid #000; position: relative; cursor: pointer; }
.q-block::after { content: '?'; position: absolute; inset: 0; display: flex; align-items: center; justify-content: center; font-size: 1.2rem; color: #fff; }

.pipe { width: 80px; height: 100px; background: #00b000; border: 4px solid #000; border-radius: 10px 10px 0 0; position: absolute; }

/* Gallery */
.scene-title { font-size: 0.8rem; color: #00ffff; margin-bottom: 50px; }
.photo-conveyor { display: flex; gap: 40px; padding: 0 50vw; }
.photo-brick { 
  flex-shrink: 0; width: 250px; height: 250px; border: 5px solid #fff; position: relative;
  background: #333; overflow: hidden;
}
.photo-brick img { width: 100%; height: 100%; object-fit: cover; }
.brick-frame { position: absolute; inset: 0; pointer-events: none; }

/* Finish & Card */
.big-q { width: 80px; height: 80px; font-size: 2rem; }
.hit-anim { animation: hitBlock 0.3s; }
@keyframes hitBlock { 0% { transform: translateY(0); } 50% { transform: translateY(-40px); } 100% { transform: translateY(0); } }

.party-info-card {
  position: absolute; top: 15%; width: 90%; max-width: 400px;
  background: #fff; border: 6px solid #000; padding: 25px; color: #333;
  box-shadow: 12px 12px #ff0000; z-index: 2000; text-align: center;
}
.card-title { font-size: 0.9rem; color: #ff0000; margin-bottom: 20px; border-bottom: 3px solid #eee; padding-bottom: 15px; }
.details { font-size: 0.7rem; line-height: 2; margin-bottom: 30px; text-align: left;}

.btn-group { display: flex; flex-direction: column; gap: 15px; }
.pixel-btn { padding: 15px; text-decoration: none; font-size: 0.6rem; color: #fff; border: 4px solid #000; text-align: center; }
.blue { background: #0055BF; }
.green { background: #33A11D; }

/* Modern BGM Bar */
.bgm-bar {
  position: fixed; top: 16px; right: 16px; z-index: 2100;
  display: flex; align-items: center; gap: 8px;
  background: rgba(0,0,0,0.55);
  backdrop-filter: blur(12px); -webkit-backdrop-filter: blur(12px);
  padding: 8px 14px; border-radius: 30px;
  cursor: pointer; color: rgba(255,255,255,0.7);
  border: 1px solid rgba(255,255,255,0.1);
  transition: all 0.3s ease;
  font-family: -apple-system, BlinkMacSystemFont, sans-serif;
}
.bgm-bar:hover, .bgm-bar:active { background: rgba(0,0,0,0.7); }
.bgm-bar.active { border-color: rgba(255,200,0,0.3); color: #ffcc00; }
.bgm-icon { display: flex; align-items: center; flex-shrink: 0; }
.bgm-label { font-size: 10px; letter-spacing: 0.5px; white-space: nowrap; }
.bgm-eq { display: flex; align-items: flex-end; gap: 2px; height: 14px; }
.bgm-eq span {
  display: block; width: 3px; background: #ffcc00; border-radius: 2px;
  animation: eqBounce 0.6s infinite ease-in-out alternate;
}
.bgm-eq span:nth-child(1) { height: 6px; animation-delay: 0s; }
.bgm-eq span:nth-child(2) { height: 10px; animation-delay: 0.15s; }
.bgm-eq span:nth-child(3) { height: 4px; animation-delay: 0.3s; }
.bgm-eq span:nth-child(4) { height: 8px; animation-delay: 0.45s; }
@keyframes eqBounce {
  0% { height: 3px; }
  100% { height: 14px; }
}

/* Retro Modal */
.retro-modal { position: fixed; inset: 0; background: rgba(0,0,0,0.92); z-index: 3000; display: flex; align-items: center; justify-content: center; padding: 20px; }
.modal-box { background: #000; padding: 10px; text-align: center; max-width: 95%; max-height: 90vh; border-radius: 4px; border: 4px solid rgba(255,255,255,0.3); }
.modal-box img { width: 100%; max-height: 75vh; object-fit: contain; margin-bottom: 15px; border-radius: 2px; }
.close-txt { font-size: 0.5rem; color: rgba(255,255,0,0.6); font-family: 'Press Start 2P', cursive; }

/* ===== MOBILE RESPONSIVE ===== */
@media (max-width: 768px) {
  .pixel-title { font-size: 1.4rem; margin-bottom: 12px; }
  .pixel-sub { font-size: 0.55rem; }
  .ui-overlay { top: 20px; padding: 0 20px; font-size: 0.5rem; }
  .jian-mario { width: 70px; height: 85px; }
  .face-circle { width: 30px; height: 30px; top: 10px; }
  .pixel-blend img { width: 130%; height: 130%; }
  .fixed-mario-wrapper { padding-bottom: 60px; }
  .photo-conveyor { gap: 20px; padding: 0 30vw; }
  .photo-brick { width: 180px; height: 180px; border-width: 3px; }
  .scene-title { font-size: 0.6rem; margin-bottom: 30px; }
  .party-info-card { top: 10%; width: 92%; padding: 18px; box-shadow: 8px 8px #ff0000; }
  .card-title { font-size: 0.7rem; margin-bottom: 15px; padding-bottom: 10px; }
  .details { font-size: 0.55rem; line-height: 2; margin-bottom: 20px; }
  .pixel-btn { padding: 12px; font-size: 0.5rem; border-width: 3px; }
  .bgm-bar { top: 10px; right: 10px; padding: 6px 10px; gap: 6px; border-radius: 24px; }
  .bgm-label { font-size: 8px; }
  .bgm-eq { height: 10px; }
  .bgm-eq span { width: 2px; }
  .brick { width: 30px; height: 30px; }
  .q-block { width: 30px; height: 30px; }
  .q-block::after { font-size: 0.9rem; }
  .pipe { width: 60px; height: 75px; }
  .big-q { width: 60px; height: 60px; }
  .parallax-hills { height: 150px; }
}

@media (max-width: 375px) {
  .pixel-title { font-size: 1.1rem; }
  .jian-mario { width: 55px; height: 70px; }
  .face-circle { width: 24px; height: 24px; top: 8px; }
  .photo-brick { width: 150px; height: 150px; }
  .party-info-card { padding: 14px; }
  .card-title { font-size: 0.6rem; }
  .details { font-size: 0.5rem; }
}
</style>
